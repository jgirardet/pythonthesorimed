# Third Party Libraries
from parseur.parseur import ProcApi

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
