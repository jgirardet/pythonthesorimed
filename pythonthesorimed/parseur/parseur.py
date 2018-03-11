import io
import re
from collections import namedtuple
from pathlib import Path
from .prototype import intro, connect, appel_character, appel_refcursor, base_func

THESORIMED_API = Path(__file__).parent / "api.sql"
THESORIMED_API = str(THESORIMED_API.absolute())
LIGNE_MOTIF = "CREATE OR REPLACE FUNCTION "

NB_API = 131

SAVE_API_DIR = "../build"
SAVE_API_NAME = "api.py"
"""

Crrer une app lanceur du parsing
parseur nb_api fichier.sql


Creer :

func.py
ThesoProc =  namedtupple("ThesoProc", "name, genre, params")

funcs : {
    name: ThesoProc(name, genre, params), etc
    }


from funcs import funcs

class ThesoItem:
    def __init__(self, cip):
        self.cip = cip

    def _appel_char
    def _connection
    def _ appel_cursor
    def _select_appel

    @property
    def mographie

    def proc(self, name, reqete):
        connect
        attributes = list_func['name']
        return  selectappel(genre)(attr.name, requete, attr.params)

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


class ThesorimedApiParseur:
    """
    Class générale permettant de parser l'api Thesorimed
    et la convertir en api python
    """

    def __init__(self,
                 fichier=THESORIMED_API,
                 ligne_motif=LIGNE_MOTIF,
                 save_api_dir=SAVE_API_DIR,
                 save_api_name=SAVE_API_NAME):
        """
        fichier : cheminr vers l'api.sql
        api : dictionnaire qui contiendra nom/params/retour des fonctions
        ligne_motif : LIGNE_MOTIF des parametres
        """
        self.fichier = fichier
        self.api = {}  #on initialise l'api de base
        self.ligne_motif = ligne_motif.lower()
        self.save_api_dir = save_api_dir
        self.save_api_name = SAVE_API_NAME

    def read_lines(self):
        """
        collecte chaque ligne de déclaration d'api selon motif
        """
        if isinstance(self.fichier, io.StringIO):  #monkeypatch dont like open
            f = self.fichier
        else:
            f = open(self.fichier)

        self.lignes_lues = []
        for ligne in f:
            ligne = ligne.lower()
            if ligne.startswith(self.ligne_motif):
                self.lignes_lues.append(ligne)

    def extraction(self):
        """
        extract [func_name, params, retour]
        """
        x = []
        for l in self.lignes_lues:
            a = []
            b = "CREATE OR REPLACE FUNCTION (.*) \(".lower()
            a.append(re.findall(b, l)[0])

            c = " \((.*)\) ".lower()
            a.append(re.findall(c, l)[0])

            d = "RETURNS (.*) AS".lower()
            a.append(re.findall(d, l)[0])

            x.append(a)
        self.extracted = x

    def clean_func_name(self):
        #remove "thesorimds"
        cle = 'thesorimed.'
        for f in self.extracted:
            if cle in f[0]:
                f[0] = f[0][len(cle):]

    def clean_params(self):
        #change numeric with int, varchar to str
        for f in self.extracted:
            sp = f[1].split(',')
            l = []
            for s in sp:
                x = re.findall("[0-9]+", s)
                x = x[0] if x else ''
                if 'numeric' in s:
                    l.append('int' + x)
                if 'varchar' in s:
                    l.append('str' + x)
            f[1] = l

    def clean_retour(self):
        #cursor or char
        for f in self.extracted:
            if 'refcursor' in f[2]:
                f[2] = "cursor"
            elif 'character' in f[2]:
                f[2] = "char"
            else:
                raise Exception(
                    "le Retour d'entrée n'est pas connu pour {} ".format(f[0]))

    def create_apicleaned(self):
        #turn extracted to namedtupple for convinience
        self.apicleaned = []
        ApiCleaned = namedtuple("ApiCleaned", ['name', 'params', 'retour'])
        for i in self.extracted:
            self.apicleaned.append(ApiCleaned(i[0], i[1], i[2]))

    def clean_all(self):
        #run all cleaning function
        self.clean_func_name()

        self.clean_params()
        self.clean_retour()
        self.create_apicleaned()

    def write_base(self):
        #pick base function
        chaine = intro + connect + appel_refcursor + appel_character
        self.stream = chaine

    def write_func(self):
        #write function returnnong character
        for i in self.apicleaned:
            if i.retour == "char":
                ch = base_func.format(
                    name=i.name, appel="appel_character", params=i.params)
                self.stream = self.stream + ch
            elif i.retour == "cursor":
                ch = base_func.format(
                    name=i.name, appel="appel_refcursor", params=i.params)
                self.stream = self.stream + ch

    def write_to_file(self):
        path = Path(self.save_api_dir)
        path.mkdir(exist_ok=True)
        path = path / self.save_api_name
        path.write_text(self.stream)

    def write_api(self):
        self.write_base()
        self.write_func()
        self.write_to_file()

    def create_thesorimed(self):
        #run the whole process
        self.read_lines()
        self.extraction()
        self.clean_all()
        self.write_api()


def main():
    import sys
    a = ThesorimedApiParseur(fichier=sys.argv[1], save_api_dir=sys.argv[2])
    a.create_thesorimed()


# if __name__ == '__main__':
#     parse = ThesorimedApiParseur(fichier='api.py', save_api_dir='.')
#     parse.create_thesorimed()