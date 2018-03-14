# Third Party Libraries
import pytest

# pythonthesorimed
from pythonthesorimed.api import ProcApi, thesoapi
from pythonthesorimed.exceptions import ThesorimedError
from pythonthesorimed.thesoitem import ThesoItem

instance = ThesoItem("1", "3", "4", "5")


class TestValidReq:
    def test_has_not_equals_args_number_raises(self):
        with pytest.raises(ThesorimedError) as e:
            ThesoItem._valide_req(thesoapi['get_cip'], [1, 2, 3])
        assert str(e.value) == "Le nombre d'argument est invalide"

    def test_has_equals_argq_number_pass(self):
        assert ThesoItem._valide_req(thesoapi['get_cip'], [1])

    def test_str_int_is_iterable(self):
        assert ThesoItem._valide_req(thesoapi['get_the_spe_details'],
                                     [(1, 2), 1])

    def test_str_int_not_iterable_via_int(self):
        with pytest.raises(ThesorimedError) as e:
            ThesoItem._valide_req(thesoapi['get_the_spe_details'], [1, 1])
        assert str(e.value) == "Le premier argument doit être iterable"

    def test_str_int_is_integer_list(self):
        assert ThesoItem._valide_req(thesoapi['get_the_spe_details'],
                                     [(1, 2), 1])

    def test_str_int_not_list_of_integer(self):
        with pytest.raises(ThesorimedError) as e:
            assert ThesoItem._valide_req(thesoapi['get_the_spe_details'],
                                         [("o", "oi"), 1])
        assert str(e.value) == "L'argument attendu est une liste d'entier"

    def test_int_alone_is_not_integer_raises(self):
        with pytest.raises(ThesorimedError) as e:
            assert ThesoItem._valide_req(thesoapi['get_the_cim10'], ["lij"])
        assert str(e.value) == "L'argument doit être un entier"

    # def test_int_alone_with_lentgh_is_not_integer_raises(self):
    #     with pytest.raises(ThesorimedError) as e:
    #         assert ThesoItem._valide_req(thesoapi['get_cip'], ["lij"])
    #     assert str(e.value) == "L'argument doit être un entier"

    def test_longueur_req_trop_grande_raises(self):
        with pytest.raises(ThesorimedError) as e:
            assert ThesoItem._valide_req(thesoapi['get_cip'], [1234567])
        assert str(e.value) == "Longueur de requête limité à 6"

    def test_longueur_ok_pass(self):
        assert ThesoItem._valide_req(thesoapi['get_cip'], [123456])


@pytest.mark.parametrize(
    'name,req,expected',
    [('get_cons', [1], ['1']), ('get_the_spe_details', [[1], 1], ['1', 1]),
     ('get_the_info_spe', [[3, 4, 5, 6, 7, 8], 1], ["3,4,5,6,7,8", 1]),
     ('get_the_code_cim10', ["bla"], ["bla"])])
def test_normalize_pass(name, req, expected):
    assert instance._normalize_req(thesoapi[name], req) == expected


def test_normalize_raises():
    a = list(thesoapi['get_cip'])
    a[2] = "fake"
    nt = ProcApi(*a)

    with pytest.raises(ThesorimedError) as e:
        instance._normalize_req(nt, [1])
    assert str(e.value) == "genre invalide"


def test_proc_raises():
    with pytest.raises(ThesorimedError) as e:
        instance.proc("blabalbal", [1])
    assert str(e.value) == "La procédure appelée n'existe pas"
