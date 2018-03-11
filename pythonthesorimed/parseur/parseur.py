# Standard Libraries
import io
import re
from collections import namedtuple
from pathlib import Path

# pythonthesorimed
from pythonthesorimed.exceptions import ThesorimedParseurError

from .prototype import import_and_nametupple_def, intro

VERSION_API = 2.00

LIGNE_MOTIF = "CREATE OR REPLACE FUNCTION "

NB_API = 130  # dans la version 2, get_the_hyper_to_spe est défini 2 fois

SAVE_API_DIR = str(Path(__file__).parents[1])

SAVE_API_NAME = "api.py"

ProcApi = namedtuple("ProcApi", ['name', 'input_type', 'genre'])


class ThesorimedApiParseur:
    """
    Class générale permettant de parser l'api Thesorimed
    et la convertir en api python
    """

    def __init__(self,
                 fichier,
                 save_api_dir=SAVE_API_DIR,
                 ligne_motif=LIGNE_MOTIF,
                 save_api_name=SAVE_API_NAME,
                 nb_api=NB_API):
        """
        fichier : cheminr vers l'api.sql
        api : dictionnaire qui contiendra nom/params/retour des fonctions
        ligne_motif : LIGNE_MOTIF des parametres
        """
        self.fichier = fichier
        self.api = {}  # on initialise l'api de base
        self.ligne_motif = ligne_motif.lower()
        self.save_api_dir = save_api_dir
        self.nb_api = nb_api
        self.save_api_name = save_api_name

    def read_lines(self):
        """
        collecte chaque ligne de déclaration d'api selon motif
        """
        if isinstance(self.fichier, io.StringIO):  # monkeypatch dont like open
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
        # remove "thesorimds"
        cle = 'thesorimed.'
        for f in self.extracted:
            if cle in f[0]:
                f[0] = f[0][len(cle):]

    def clean_params(self):
        # change numeric with int, varchar to str
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

    def create_procapi(self):
        # turn extracted to namedtupple for convinience
        self.thesoapi = {}
        for i in self.extracted:
            # if i[0] in self.thesoapi:
            #     raise Exception(i[0])
            self.thesoapi[i[0]] = (ProcApi(i[0], i[1], i[2]))
        if len(self.thesoapi) != self.nb_api:
            raise ThesorimedParseurError(
                f'Le nombre Api attendu ({self.nb_api}) ne correspond pas : {len(self.thesoapi)}'
            )

    def clean_all(self):
        # run all cleaning function
        self.clean_func_name()

        self.clean_params()
        self.clean_retour()
        self.create_procapi()

    def write_base(self):
        # debut du fichier final
        chaine = intro + import_and_nametupple_def
        self.stream = chaine + "thesoapi = " + str(self.thesoapi)

    def write_to_file(self):
        path = Path(self.save_api_dir)
        path.mkdir(exist_ok=True)
        path = path / self.save_api_name
        path.write_text(self.stream)

    def write_api(self):
        self.write_base()
        self.write_to_file()

    def create_thesorimed(self):
        # run the whole process
        self.read_lines()
        self.extraction()
        self.clean_all()
        self.write_api()


def main():
    import sys
    a = ThesorimedApiParseur(fichier=sys.argv[1])
    a.create_thesorimed()
