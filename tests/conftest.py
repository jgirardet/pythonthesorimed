# Standard Libraries
import copy
import io

# Third Party Libraries
import pytest

# pythonthesorimed
from pythonthesorimed.parseur.parseur import ThesorimedApiParseur

from .gabarit import extracted, lines


@pytest.fixture(scope='function', autouse=True)
def parseur():
    return ThesorimedApiParseur(fichier=io.StringIO(lines), nb_api=4)


@pytest.fixture(scope='function', autouse=True)
def parseur_gabarit_extracted(parseur):
    p = ThesorimedApiParseur(fichier="lijl", nb_api=4)
    p.extracted = extracted
    return copy.deepcopy(p)


# @pytest.fixture(scope='session', autouse=True, tmpdir_factory)
#     parseur = (fichier=THESORIMED_API, save_api_dir=tmpdir_factory.getbasetemp().__str__())
