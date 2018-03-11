import copy

import pytest
from parseur import ThesorimedApiParseur

from .gabarit import extracted
from pathlib import Path


@pytest.fixture(scope='function', autouse=True)
def parseur():
    return ThesorimedApiParseur(
        fichier=Path(__file__).parent / "api.sql").main()


@pytest.fixture(scope='function', autouse=True)
def parseur_gabarit_extracted(parseur):
    p = ThesorimedApiParseur()
    p.extracted = extracted
    return copy.deepcopy(p)


# @pytest.fixture(scope='session', autouse=True, tmpdir_factory)
#     parseur = (fichier=THESORIMED_API, save_api_dir=tmpdir_factory.getbasetemp().__str__())
