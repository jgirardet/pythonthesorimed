# Standard Libraries
from collections import OrderedDict, namedtuple
from unittest.mock import MagicMock

# pythonthesorimed
from pythonthesorimed.parseur.parseur import ProcApi

lines = """
CREATE OR REPLACE FUNCTION GET_THE_SPE_DETAILS (VARCHAR,NUMERIC) RETURNS REFCURSOR AS
CREATE OR REPLACE FUNCTION thesorimed.get_cip (NUMERIC(6)) RETURNS character varying AS
fzefzef zef ze f zefz ef zef zef zef zefz ef
zefz efz efz efz efz ef
CREATE OR REPLACE FUNCTION thesorimed.get_frm (NUMERIC(6)) RETURNS character varying AS
CREATE OR REPLACE FUNCT
ION thesorimed.get_frm (NUMERIC(6)) RETURNS character varying AS
CREATE OR REPLACE FUNCTION GET_THE_ANXIO_SPE (VARCHAR,NUMERIC) RETURNS REFCURSOR AS"""

extracted = [
    ['get_the_spe_details', 'varchar,numeric', 'refcursor'],
    ['thesorimed.get_cip', 'numeric(6)', 'character varying'],
    ['thesorimed.get_frm', 'numeric(6)', 'character varying'],
    ['get_the_anxio_spe', 'varchar,numeric', 'refcursor'],
]

cleaned = [
    ['get_the_spe_details', ['str', 'int'], 'cursor'],
    ['get_cip', ['int6'], 'char'],
    ['get_frm', ['int6'], 'char'],
    ['get_the_anxio_spe', ['str', 'int'], 'cursor'],
]

thesoapi_test = {
    'get_the_spe_details':
    ProcApi(
        name='get_the_spe_details', input_type=['str', 'int'], genre='cursor'),
    'get_cip':
    ProcApi(name='get_cip', input_type=['int6'], genre='char'),
    'get_frm':
    ProcApi(name='get_frm', input_type=['int6'], genre='char'),
    'get_the_anxio_spe':
    ProcApi(
        name='get_the_anxio_spe', input_type=['str', 'int'], genre='cursor')
}

Record = namedtuple("Record", "gsp_nom gsp_code_virtuel gsp_code_sq_pk")
Record2 = namedtuple("Record2",
                     "sp_nom sp_cipucd sp_code_sq_pk sp_gsp_code_fk")

# requete "paracetamol 1000"
gsp = [{
    'gsp_nom': 'Paracetamol 1000 mg comprime',
    'gsp_code_virtuel': '0001052',
    'gsp_code_sq_pk': 1052
}, {
    'gsp_nom': 'Paracetamol 1000 mg gelule',
    'gsp_code_virtuel': '0007067',
    'gsp_code_sq_pk': 7067
}, {
    'gsp_nom': 'Paracetamol 1000 mg granule voie orale',
    'gsp_code_virtuel': '0006410',
    'gsp_code_sq_pk': 6410
}, {
    'gsp_nom': 'Paracetamol 1000 mg suppositoire',
    'gsp_code_virtuel': '0002313',
    'gsp_code_sq_pk': 2313
}]

spe = [{
    'sp_nom': 'PARACETAMOL BBM 1000 MG INJ',
    'pre_code_pk': '3400958308123',
    'sp_code_sq_pk': 32226,
    'sp_gsp_code_fk': 2573,
    'pre_etat_commer': 'D'
}, {
    'sp_nom': 'PARACETAMOL KBI 1000 MG INJ',
    'pre_code_pk': '3400958007804',
    'sp_code_sq_pk': 32376,
    'sp_gsp_code_fk': 2573,
    'pre_etat_commer': 'D'
}, {
    'sp_nom': 'PARACETAMOL KBI 1000 MG POCHE',
    'pre_code_pk': '3400958249297',
    'sp_code_sq_pk': 34612,
    'sp_gsp_code_fk': 2573,
    'pre_etat_commer': 'D'
}, {
    'sp_nom': 'PARACETAMOL PAN 1000 MG INJ',
    'pre_code_pk': '3400957186241',
    'sp_code_sq_pk': 22605,
    'sp_gsp_code_fk': 2573,
    'pre_etat_commer': 'D'
}, {
    'sp_nom': 'PARACETAMOL PAN 1000 MG INJ',
    'pre_code_pk': '3400957299705',
    'sp_code_sq_pk': 22605,
    'sp_gsp_code_fk': 2573,
    'pre_etat_commer': 'D'
}, {
    'sp_nom': 'PARACETAMOL TVS 1000MG CPR EFF',
    'pre_code_pk': '3400926885328',
    'sp_code_sq_pk': 37062,
    'sp_gsp_code_fk': 1052,
    'pre_etat_commer': 'D'
}, {
    'sp_nom': 'PARACETAMOL ZEN 1000MG CPR EFF',
    'pre_code_pk': '3400956318346',
    'sp_code_sq_pk': 34388,
    'sp_gsp_code_fk': 1052,
    'pre_etat_commer': 'D'
}]

fuzzy_result = [{
    'cip': '3400892621388',
    'code': 17082,
    'gsp_code': 1052,
    'nom': 'Paracetamol 1000 mg comprime'
}, {
    'cip': '3400891297706',
    'code': 1181,
    'gsp_code': 2313,
    'nom': 'Paracetamol 1000 mg suppositoire'
}, {
    'cip': '3400894091271',
    'code': 37637,
    'gsp_code': 6410,
    'nom': 'Paracetamol 1000 mg granule voie orale'
}, {
    'cip': '3400893739846',
    'code': 30798,
    'gsp_code': 7067,
    'nom': 'Paracetamol 1000 mg gelule'
}, {
    'cip': '3400958308123',
    'code': 32226,
    'gsp_code': 2573,
    'nom': 'PARACETAMOL BBM 1000 MG INJ'
}]

dict_add_valid_spe = [{
    'sp_code_sq_pk': 17082,
    'pre_code_pk': '3400892621388',
    'gsp_nom': 'Paracetamol 1000 mg comprime',
    'gsp_code_virtuel': '0001052',
    'gsp_code_sq_pk': 1052
}, {
    'sp_code_sq_pk': 1181,
    'pre_code_pk': '3400891297706',
    'gsp_nom': 'Paracetamol 1000 mg suppositoire',
    'gsp_code_virtuel': '0002313',
    'gsp_code_sq_pk': 2313
}, {
    'sp_code_sq_pk': 37637,
    'pre_code_pk': '3400894091271',
    'gsp_nom': 'Paracetamol 1000 mg granule voie orale',
    'gsp_code_virtuel': '0006410',
    'gsp_code_sq_pk': 6410
}, {
    'sp_code_sq_pk': 30798,
    'pre_code_pk': '3400893739846',
    'gsp_nom': 'Paracetamol 1000 mg gelule',
    'gsp_code_virtuel': '0007067',
    'gsp_code_sq_pk': 7067
}]
