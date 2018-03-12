# Third Party Libraries
import pytest

# pythonthesorimed
from pythonthesorimed.exceptions import ThesorimedError
from pythonthesorimed.thesoitem import ThesoItem

base_get_cip = {
    1: ['3400933354978'],
    2: None,
    3: ['3400930916292'],
    8: ['3400933449582', '3400936003736', '3400937224321'],
    9: None
}

base_is_atu = {
    7087: 'O',
    8849: 'N',
}

a = ThesoItem("localhost", "thesorimed", "j", "j")


class TestAppelChar:
    def test_get_cip(self):
        for i in [1, 2, 3, 8, 9]:
            assert a.proc('get_cip', i) == base_get_cip[i]

    def test_is_atu(self):
        for k, v in base_is_atu.items():
            assert a.proc('is_atu', k) == [v]
