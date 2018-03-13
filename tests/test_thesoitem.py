# Third Party Libraries
import pytest

# pythonthesorimed
from pythonthesorimed.api import thesoapi
from pythonthesorimed.exceptions import ThesorimedError
from pythonthesorimed.thesoitem import ThesoItem

instance = ThesoItem("1", "3", "4", "5")


@pytest.mark.parametrize(
    'obj,func', [(thesoapi['get_cip'], instance._appel_char),
                 (thesoapi['get_the_gen_equiv'], instance._appel_refcursor)])
def test_appel_proc(obj, func):
    a = instance._appel_proc(obj)
    assert a == func


class TestValidReq:
    def test_has_not_equals_args_number_raises(self):
        with pytest.raises(ThesorimedError):
            ThesoItem._valide_req(thesoapi['get_cip'], [1, 2, 3])

    def test_has_equals_argq_number_pass(self):
        assert ThesoItem._valide_req(thesoapi['get_cip'], [1])

    def test_str_int_is_iterable(self):
        assert ThesoItem._valide_req(thesoapi['get_the_spe_details'],
                                     [(1, 2), 1])

    def test_str_int_not_iterable(self):
        with pytest.raises(ThesorimedError):
            assert ThesoItem._valide_req(thesoapi['get_the_spe_details'],
                                         [1, 1])

    def test_str_int_is_integer_list(self):
        assert ThesoItem._valide_req(thesoapi['get_the_spe_details'],
                                     [(1, 2), 1])

    def test_str_int_not_iterable(self):
        with pytest.raises(ThesorimedError):
            assert ThesoItem._valide_req(thesoapi['get_the_spe_details'],
                                         [("o", "oi"), 1])

    def test_int_alone_is_not_integer_raises(self):
        with pytest.raises(ThesorimedError):
            assert ThesoItem._valide_req(thesoapi['get_the_cipemg_id'],
                                         ["lij"])

    def test_int_alone_with_lentgh_is_not_integer_raises(self):
        with pytest.raises(ThesorimedError):
            assert ThesoItem._valide_req(thesoapi['get_cip'], ["lij"])

    def test_longueur_req_trop_grande_raises(self):
        with pytest.raises(ThesorimedError):
            assert ThesoItem._valide_req(thesoapi['get_cip'], [1234567])

    def test_longueur_ok_pass(self):
        assert ThesoItem._valide_req(thesoapi['get_cip'], [123456])


def test_proc_procedure_inconnue_raises():
    try:
        instance.proc('blabal')
    except ThesorimedError as e:
        assert str(e) == "La procédure appelé n'existe pas"
