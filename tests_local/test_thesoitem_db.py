# Standard Libraries
import copy

# Third Party Libraries
import pytest
from tests.gabarit import dict_add_valid_spe, fuzzy_result, gsp, spe

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

instance = ThesoItem("localhost", "thesorimed", "j", "j", "theso_id",
                     "theso_pass")

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
                         'INSOMNIE')[0]['cim_code'] == 'G47.0'


def test_get_the_gen_equiv():
    r = instance.proc('get_the_gen_equiv', 3, 1)
    assert r == [{
        'gsp_nom': 'RIFADINE 300MG GELULE',
        'lib_virt': 'Rifampicine 300 mg gelule',
        'sp_code_equiv': 4793,
        'sp_code_sq_pk': 3,
        'sp_param': 'RIMACTAN 300MG GELULE'
    }, {
        'gsp_nom': 'RIMACTAN 300MG GELULE',
        'lib_virt': 'Rifampicine 300 mg gelule',
        'sp_code_equiv': 3,
        'sp_code_sq_pk': 3,
        'sp_param': 'RIMACTAN 300MG GELULE'
    }]


def test_proc_launch_validation():
    with pytest.raises(ThesorimedError):
        instance.proc('get_cip', 1, 2, 3)


def test_get_by_gsp():
    req = instance.get_by('gsp', "paracetamol")
    assert "gsp_nom" in req[0]


def test_get_by_spe():
    req = instance.get_by('spe', "paracetamol")
    assert "sp_nom" in req[0]


def test_fuzzy(monkeypatch):
    def f_proc(self, mode, var):
        if mode == "gsp":
            return list(gsp)
        elif mode == "spe":
            return list(spe)

    monkeypatch.setattr(ThesoItem, 'get_by', f_proc)

    assert fuzzy_result == instance.fuzzy("paracetamol 1000")


def test_fuzzy_cases():

    assert instance.fuzzy("paracetamol 100")
    assert instance.fuzzy("paracetamol 10"), "fail if no spe"
    assert instance.fuzzy('xarelto'), "one spe hase no gsp"
    assert instance.fuzzy('doliprane'), "gsp empty"
    assert list(instance._gsp_add_valid_spe(gsp)) == dict_add_valid_spe
