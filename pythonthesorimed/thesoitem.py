# Standard Libraries
import json
from collections import defaultdict
from collections.abc import Iterable
from itertools import chain
from typing import Iterable

# Third Party Libraries
import psycopg2
from psycopg2.extras import RealDictConnection

from .api import thesoapi
from .exceptions import ThesorimedError


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
            password=self.password,
            connection_factory=RealDictConnection)

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
            with con.cursor() as curs:
                curs.execute("SET search_path TO thesorimed, public")
                curs.callproc("thesorimed." + obj_api.name, requete)
                resu = curs.fetchone()

                res = resu[obj_api.name]

                if not res:
                    return

                if res.startswith("<unnamed portal"):
                    f = f'FETCH ALL IN "{res}"'
                    curs.execute(f)
                    res = curs.fetchall()
                    return res

                else:
                    return res.split(', ')

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
                    raise ThesorimedError("L'argument attendu est une liste d'entier")

        for x, y in zip(obj.input_type, req):
            if x.startswith('int'):
                if type(y) != int:
                    raise ThesorimedError("L'argument doit être un entier")
            import re
            longueur_champs = re.findall(r"(?:int|str)([0-9]+)", x)
            if longueur_champs:
                if y > pow(10, int(longueur_champs[0])):
                    raise ThesorimedError(f"Longueur de requête limité à {longueur_champs[0]}")
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

                SELECT DISTINCT sp_nom, pre_code_pk, sp_code_sq_pk, sp_gsp_code_fk, pre_etat_commer
                FROM thesorimed.sp_specialite s, thesorimed.pre_presentation p
                WHERE s.sp_code_sq_pk = p.pre_sp_code_fk
                AND LOWER(s.sp_nom) LIKE %s
                AND p.pre_etat_commer = 'D'
                ORDER BY sp_nom
                """,
        }

        with self._connect() as con:
            with con.cursor() as curs:
                curs.execute(requete[mode], (var, ))
                cc = curs.fetchall()

        return cc

    def gsp_add_valid_spe(self, gsp):
        """
        prend une liste de  gsp issu de get_by, trouve une spé commercialisée
        correspondante et append le numéro et le cip de cette spé
        """
        # On crée un dico avec gsp_code comme clée
        dico_gsp = {x['gsp_code_sq_pk']: x for x in gsp}

        # groupe_generiques = tous les médicaments concernées par tous les gsp
        groupe_generiques = self.proc('get_the_virtuel', dico_gsp.keys(), 2)

        # on class dans dico_generiques tous les éléments de groupe_generiques par gsp_code
        # {codegsp: [{code_spe:spe}, ....]}
        dico_generiques_par_gsp = defaultdict(list)
        for x in groupe_generiques:
            dico_generiques_par_gsp[x['code_gsp']].append(x)

        # Requete de tous les états de commericalisation via tous les codes génériques
        # on ajoute sp_cipucd_long pour l'avoir pour plus tard
        codes_generiques = [x['sp_code_sq_pk'] for x in groupe_generiques]
        etat_commer = {
            i['sp_code_sq_pk']: (i['etat_commercialisation'], i['sp_cipucd_long'])
            for i in self.proc('get_the_etat_commer_spe', codes_generiques, 1)
        }

        # on pour boucle sur les spe classées dans chaque gsp. Si une correspondance
        # est trouvée, on ajoute son code et son cip, aux valeurs connues
        nouveau_gsp = defaultdict(dict)
        for code_gsp, spes in dico_generiques_par_gsp.items():
            for spe in spes:
                if etat_commer[spe['sp_code_sq_pk']][0] == 'D':
                    nouveau_gsp[code_gsp]['sp_code_sq_pk'] = spe['sp_code_sq_pk']
                    nouveau_gsp[code_gsp]['pre_code_pk'] = etat_commer[spe['sp_code_sq_pk']][1]
                    nouveau_gsp[code_gsp].update(dico_gsp[code_gsp])
                    # final.append(item)
                    break

        # on retourne uniquement un liste de dict
        return nouveau_gsp.values()

    def fuzzy(
            self,
            chaine: str,
    ):
        """
        Fuzzy search dans les gsp et spe. Les réultats gsp sont affichés en premier.

        Principe:
            - le nom d'un gsp est prioritaire sur le choix
            - les noms princeps sont affichés s'ils ne rentrent pas dans un gsp
            - offre un interface de retour commune à gsp et spe
        """

        # on recupere par spe et par groupe
        gsp = self.get_by('gsp', chaine)
        spe = self.get_by('spe', chaine)

        if gsp:
            # on retire les spes dont le groupe est déjà dans gsp (ex : PARACETAMOL mylan)
            gsp_codes = [x['gsp_code_sq_pk'] for x in gsp]  # on extrait les gsp
            gsp_new_spe = [x for x in spe if x['sp_gsp_code_fk'] not in gsp_codes]

        else:
            gsp_new_spe = spe

        # ensuite pour chaque spe ayant le même gspn on garde que la première
        # les None sont gardés car incertain
        spe_restant = []
        gsp_codes_restant = []
        for x in gsp_new_spe:
            if x['sp_gsp_code_fk'] is None:
                spe_restant.append(x)
                continue
            elif x['sp_gsp_code_fk'] in gsp_codes_restant:
                continue
            gsp_codes_restant.append(x['sp_gsp_code_fk'])
            spe_restant.append(x)

        gsp_new_spe = spe_restant

        # on recherche un code de spe valable pour ajouter au gsp
        gsp_en_dico = [] if not gsp else self.gsp_add_valid_spe(gsp)

        # formattage uniforme des valeurs retours pour gsp et spé
        merged = []
        for x in gsp_en_dico:
            d = {
                'nom': x['gsp_nom'],
                'cip': x['pre_code_pk'],
                'code': x['sp_code_sq_pk'],
                'gsp_code': x['gsp_code_sq_pk']
            }
            merged.append(d)

        for x in gsp_new_spe:
            d = {
                'nom': x['sp_nom'],
                'cip': x['pre_code_pk'],
                'code': x['sp_code_sq_pk'],
                'gsp_code': x['sp_gsp_code_fk']
            }
            merged.append(d)

        return merged
