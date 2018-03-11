# Standard Libraries
from collections.abc import Iterable
from exceptions import ThesorimedError

# Third Party Libraries
import psycopg2
from api import thesoapi
from psycopg2.extras import NamedTupleCursor


class ThesoItem:
    """
    Base classe interface pour thesorimed
    """

    @staticmethod
    def _connect():
        """
        Base fonction to connect to database.
        Return a pscipg connection
        should return psycopg2.connect
        """
        # raise NotImplementedError
        return psycopg2.connect(
            host="127.0.0.1", dbname="thesorimed", user="j", password="j")

    def _appel_char(self, obj_api, req):
        """
        Pour les précédure 'char' retournant une valeur simple
        """

        req = list(req)  # list to modify tupple
        if 'str' in obj_api.input_type[0]:  # turn arg to str if varchar
            req[0] = str(req[0])

        with self._connect() as con:
            with con.cursor(cursor_factory=NamedTupleCursor) as curs:
                curs.execute("SET search_path TO thesorimed, public")
                curs.callproc("thesorimed." + obj_api.name, req)
                res = curs.fetchone()
                cc = getattr(res, obj_api.name)
                return cc

    def _appel_refcursor(self, obj_api, req):
        """
        Pour les procédures "cursor" reournant un liste
        """
        # convert [int,int,int] to 'int,int, int'
        req = list(req)
        for i in range(len(req)):
            if 'str' in obj_api.input_type[i]:
                req[i] = ','.join(map(str, req[i]))
        # create connection
        with self._connect() as con:
            with con.cursor(cursor_factory=NamedTupleCursor) as curs:
                curs.execute("SET search_path TO thesorimed, public")
                curs.callproc("thesorimed." + obj_api.name, req)

                portal_name = curs.fetchone()[0]  # get the cursor
                portal_name = '"' + portal_name + '"'
                f = "FETCH ALL IN {0};".format(
                    portal_name)  # retrieve from cursor
                curs.execute(f)
                cc = curs.fetchall()
        return cc

    def _appel_proc(self, obj_api):
        if obj_api.genre == "char":
            return self._appel_char
        elif obj_api.genre == "cursor":
            return self._appel_refcursor
        else:
            raise ThesorimedError('Genre de la procédure inconnu')

    @staticmethod
    def _valide_req(obj, req):
        if len(req) != len(obj.input_type):
            raise ThesorimedError("Le nombre d'argument est invalide")

        if obj.input_type == ['str', 'int']:
            if not isinstance(req[0], Iterable):
                raise ThesorimedError("Le premier argument doit être iterable")
            for item in req[0]:
                try:
                    int(item)
                except ValueError:
                    raise ThesorimedError(
                        "L'argument attendu est une liste d'entier")

        for x, y in zip(obj.input_type, req):
            if x == 'int':
                if type(y) != int:
                    raise ThesorimedError("L'argument doit être un entier")
            import re
            longueur_champs = re.findall(r"(?:int|str)([0-9]+)", x)
            if longueur_champs:
                if y > pow(10, int(longueur_champs[0])):
                    raise ThesorimedError(
                        f"Longueur de requête limité à {longueur_champs}")

    @classmethod
    def proc(cls, name, *req):
        try:
            obj_api = thesoapi[name]
        except KeyError:
            raise ThesorimedError("La procédure appelé n'existe pas")

        cls._valide_req(obj_api, req)

        return cls._appel_proc(cls, obj_api)(cls, obj_api, req)


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
