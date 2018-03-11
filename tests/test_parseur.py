import io
import re
from pathlib import Path

import pytest
from parseur import NB_API, ThesorimedApiParseur
from prototype import appel_character, appel_refcursor, connect, intro

from .gabarit import apicleaned, cleaned, written_func, extracted, lines


class TestThesorimedAPiParseur:
    def test_init(self, parseur):
        assert parseur.fichier

    def test_read_lines(self):
        p = ThesorimedApiParseur(fichier=io.StringIO(lines))

        p.read_lines()
        expected = [
            "CREATE OR REPLACE FUNCTION GET_THE_SPE_DETAILS (VARCHAR,NUMERIC) RETURNS REFCURSOR AS",
            "CREATE OR REPLACE FUNCTION thesorimed.get_cip (NUMERIC(6)) RETURNS character varying AS",
            "CREATE OR REPLACE FUNCTION thesorimed.get_frm (NUMERIC(6)) RETURNS character varying AS",
            "CREATE OR REPLACE FUNCTION GET_THE_ANXIO_SPE (VARCHAR,NUMERIC) RETURNS REFCURSOR AS"
        ]

        # x = [tuple(lst) for lst in p.lignes_lues]
        # y = [tuple(lst) for lst in expected]
        for x, y in zip(p.lignes_lues, expected):
            print(x, y.lower())
        for x, y in zip(p.lignes_lues, expected):
            assert x.rstrip() == y.lower()  #rstrip because of the trailing \n"

    def test_extraction(self, parseur):
        p = ThesorimedApiParseur(fichier=io.StringIO(lines))
        p.read_lines()
        p.extraction()

        for x, y in zip(p.extracted, extracted):
            assert x == y

    def test_read_lines_nb(self, parseur):
        parseur.read_lines()
        assert len(parseur.lignes_lues) == NB_API

    def test_LIGNE_MOTIF(self, parseur):
        assert parseur.ligne_motif.islower()

    def test_get_func_name(self, parseur):
        "verifice que chaque fonction trouvé est dans le fichier"
        parseur.read_lines()
        parseur.extraction()
        for x, y in zip(parseur.lignes_lues, parseur.extracted):
            assert re.search(re.escape(
                y[0]), x) is not None, "toutes fcontions  pas trouvéestrouvées"

    def test_get_params(self, parseur):
        parseur.read_lines()
        parseur.extraction()
        for x, y in zip(parseur.lignes_lues, parseur.extracted):
            print(x, y)
            assert re.search(re.escape(y[1]), x) is not None and re.search(
                re.escape(y[0]),
                x) is not None, "paramas presont pour bonne ligne"

    def test_get_retour(self, parseur):
        parseur.read_lines()
        parseur.extraction()
        for x, y in zip(parseur.lignes_lues, parseur.extracted):
            print(x, y)
            assert re.search(re.escape(y[2]), x) is not None and re.search(
                re.escape(y[0]),
                x) is not None, "retour presont pour bonne fonction"

    def test_clean_func_name(self, parseur_gabarit_extracted):
        parseur = parseur_gabarit_extracted
        parseur.clean_func_name()
        for i, j in zip(parseur.extracted, cleaned):
            assert i[0] == j[0]

    def test_clean_params(self, parseur_gabarit_extracted):
        p = parseur_gabarit_extracted
        p.clean_params()
        for i, j in zip(p.extracted, cleaned):
            assert i[1] == j[1]

    def test_clean_retour(self, parseur_gabarit_extracted):
        p = parseur_gabarit_extracted
        p.clean_retour()
        for i, j in zip(p.extracted, cleaned):
            assert i[2] == j[2]

    def test_clean_retour_raises(self, parseur_gabarit_extracted):
        p = parseur_gabarit_extracted
        p.extracted[2][2] = "mok"  #on change le retourne
        with pytest.raises(Exception):
            p.clean_retour()

    def test_create_apicleaned(self, parseur_gabarit_extracted):
        p = parseur_gabarit_extracted
        p.clean_func_name()
        p.clean_params()
        p.clean_retour()
        p.create_apicleaned()
        assert p.apicleaned[0].name == cleaned[0][0]
        assert p.apicleaned[0].params[0] == cleaned[0][1][0]
        assert p.apicleaned[0].params[0] == cleaned[0][1][0]
        assert p.apicleaned[0].params[1] == cleaned[0][1][1]
        assert p.apicleaned[0].retour == cleaned[0][2]

    def test_clean_all(self, parseur_gabarit_extracted):
        p = parseur_gabarit_extracted
        p.clean_all()
        assert p.apicleaned == apicleaned

    def test_write_base(self, parseur):
        parseur.write_base()
        assert parseur.stream == intro + connect + appel_refcursor + appel_character

    def test_write_func(self, parseur):
        parseur.apicleaned = apicleaned
        parseur.stream = ""
        parseur.write_func()
        assert parseur.stream == written_func

    def test_write_to_file(self, parseur, tmpdir_factory):
        parseur.save_api_dir = tmpdir_factory.getbasetemp().__str__()
        parseur.apicleaned = apicleaned
        parseur.stream = "gf f hgj hg j hkk "
        parseur.write_to_file()
        a = Path(parseur.save_api_dir) / parseur.save_api_name
        assert a.read_text(), "file should be here usable"

    def test_create_thesorimed(self, tmpdir_factory):
        a = ThesorimedApiParseur(
            fichier=io.StringIO(lines),
            save_api_dir=tmpdir_factory.getbasetemp().__str__())
        a.create_thesorimed()
        b = Path(a.save_api_dir) / a.save_api_name
        assert b.read_text(
        ) == intro + connect + appel_refcursor + appel_character + written_func
