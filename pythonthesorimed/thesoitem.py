# Standard Libraries
from collections.abc import Iterable
from itertools import chain
from typing import Iterable

# Third Party Libraries
import psycopg2
from psycopg2.extras import NamedTupleCursor

from .api import thesoapi
from .exceptions import ThesorimedError
import json


class ThesoItem:
    """
    Base classe interface pour thesorimed
    """

    def __init__(self, host, dbname, user, password):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password

    def _connect(self):
        """
        Base fonction to connect to database.
        Return a pscipg connection
        should return psycopg2.connect
        """
        # raise NotImplementedError
        return psycopg2.connect(
            host=self.host,
            dbname=self.dbname,
            user=self.user,
            password=self.password)

    def _normalize_req(self, obj_api, req):
        """
        globalement transforme les listes en str
        """
        req = list(req)
        if isinstance(req[0], str):
            return req
        if obj_api.genre == "char":
            req[0] = str(req[0])
        elif obj_api.genre == "cursor":
            req[0] = ','.join(map(str, req[0]))
        else:
            raise ThesorimedError('genre invalide')
        return req

    def _appel_proc(self, obj_api, req):

        if 'str' in obj_api.input_type[0]:
            requete = self._normalize_req(obj_api, req)
        else:
            requete = req

        with self._connect() as con:
            with con.cursor(cursor_factory=NamedTupleCursor) as curs:
                curs.execute("SET search_path TO thesorimed, public")
                curs.callproc("thesorimed." + obj_api.name, requete)
                res = curs.fetchone()

                try:
                    result = getattr(res, obj_api.name).split(', ')
                except AttributeError:
                    return None

                if result[0].startswith("<unnamed portal"):
                    f = f'FETCH ALL IN "{result[0]}"'
                    curs.execute(f)
                    result = curs.fetchall()

                return result

    @staticmethod
    def _valide_req(obj, req):
        if len(req) != len(obj.input_type):
            raise ThesorimedError("Le nombre d'argument est invalide")

        if obj.input_type == ['str', 'int']:
            if not isinstance(req[0], Iterable):
                print(req)
                raise ThesorimedError("Le premier argument doit être iterable")
            for item in req[0]:
                try:
                    int(item)
                except ValueError:
                    raise ThesorimedError(
                        "L'argument attendu est une liste d'entier")

        for x, y in zip(obj.input_type, req):
            if x.startswith('int'):
                if type(y) != int:
                    raise ThesorimedError("L'argument doit être un entier")
            import re
            longueur_champs = re.findall(r"(?:int|str)([0-9]+)", x)
            if longueur_champs:
                if y > pow(10, int(longueur_champs[0])):
                    raise ThesorimedError(
                        f"Longueur de requête limité à {longueur_champs[0]}")
        return True

    def proc(self, name, *req):
        """
        Method de base pour l'appel des procédures
        """
        try:
            obj_api = thesoapi[name]
        except KeyError:
            raise ThesorimedError("La procédure appelée n'existe pas")

        self._valide_req(obj_api, req)

        return self._appel_proc(obj_api, req)

    def get_by(self, mode, var):
        """
        Recherche mutli critere sur les noms virtuels et de specialité
        """

        var = var.replace(' ', "%") + "%"

        requete = {
            'gsp':
            """
                SELECT gsp_nom, gsp_code_virtuel, gsp_code_sq_pk
                FROM thesorimed.GSP_GENERIQUE_SPECIALITE g
                WHERE LOWER(g.gsp_nom) LIKE %s
                ORDER BY gsp_nom
                """,
            'spe':
            """
                SELECT sp_nom, sp_cipucd, sp_code_sq_pk, sp_gsp_code_fk
                FROM thesorimed.sp_specialite g
                WHERE LOWER(g.sp_nom) LIKE %s
                ORDER BY sp_nom
                """,
        }

        with self._connect() as con:
            with con.cursor(cursor_factory=NamedTupleCursor) as curs:
                curs.execute(requete[mode], (var, ))
                cc = curs.fetchall()

        return cc

    def fuzzy(
            self,
            chaine: str,
    ):
        """
        Fuzzy search dans les gsp et spe. Les réultats gsp sont affichés en premier.
        """

        # on recupere par spe et par groupe
        gsp = self.get_by('gsp', chaine)
        spe = self.get_by('spe', chaine)

        # on retire les spes dont le groupe est déjà dans gsp (ex : PARACETAMOL mylan)
        gsp_codes = [x.gsp_code_sq_pk for x in gsp]  # on extrait les gsp
        new_spe = [x for x in spe if x.sp_gsp_code_fk not in gsp_codes]

        # ensuite pour chaque spe ayant le même gspn on garde que la première
        # les None sont gardés car incertain
        spe_restant = []
        gsp_codes_restant = []
        for x in new_spe:
            if x.sp_gsp_code_fk is None:
                spe_restant.append(x)
                continue
            elif x.sp_gsp_code_fk in gsp_codes_restant:
                continue
            gsp_codes_restant.append(x.sp_gsp_code_fk)
            spe_restant.append(x)

        # retourne gsp et spe épurés
        return [record._asdict() for record in chain(gsp, spe_restant)]
