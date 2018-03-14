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

instance = ThesoItem("localhost", "thesorimed", "j", "j")

# test appel_cher


def test_get_cip():
    for i in [1, 2, 3, 8, 9]:
        assert instance.proc('get_cip', i) == base_get_cip[i]


def test_is_atu():
    for k, v in base_is_atu.items():
        assert instance.proc('is_atu', k) == [v]


# test _refcursor
def test_get_the_code_cim10():
    assert instance.proc('get_the_code_cim10',
                         'INSOMNIE')[0].cim_code == 'G47.0'


def test_get_the_gen_equiv():
    r = instance.proc('get_the_gen_equiv', 3, 1)
    assert [list(i) for i in r] == [[
        'RIFADINE 300MG GELULE', 4793, 'Rifampicine 300 mg gelule',
        'RIMACTAN 300MG GELULE', 3
    ], [
        'RIMACTAN 300MG GELULE', 3, 'Rifampicine 300 mg gelule',
        'RIMACTAN 300MG GELULE', 3
    ]]


def test_proc_launch_validation():
    with pytest.raises(ThesorimedError):
        instance.proc('get_cip', 1, 2, 3)


def test_appel_proc_check_string():
    pass
