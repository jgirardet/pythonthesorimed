# Standard Libraries
from collections.abc import Iterable
from typing import Iterable

# Third Party Libraries
import psycopg2
from psycopg2.extras import NamedTupleCursor

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
            host=self.host, dbname=self.dbname, user=self.user, password=self.password)

    def _normalize_req(self, obj_api, req):
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
        try:
            obj_api = thesoapi[name]
        except KeyError:
            raise ThesorimedError("La procédure appelée n'existe pas")

        self._valide_req(obj_api, req)

        return self._appel_proc(obj_api, req)


"""
usage dans Django:

from theso import ThesoItem

class Medicament:
    name
    cip

    detail(self, name, req):
        a = ThesoItem(self.cip)
        return a.proc(name, req)

    def monographie:
        retruen a.ThesoItem(self.cip).monographe


"""
