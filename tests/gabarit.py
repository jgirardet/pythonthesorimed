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

from collections import namedtuple

ApiCleaned = namedtuple("ApiCleaned", ['name', 'params', 'retour'])
apicleaned = [
    ApiCleaned(
        name='get_the_spe_details', params=['str', 'int'], retour='cursor'),
    ApiCleaned(name='get_cip', params=['int6'], retour='char'),
    ApiCleaned(name='get_frm', params=['int6'], retour='char'),
    ApiCleaned(
        name='get_the_anxio_spe', params=['str', 'int'], retour='cursor')
]

written_func = """
def get_the_spe_details(*req):
    return appel_refcursor("get_the_spe_details", req, ['str', 'int'])

def get_cip(*req):
    return appel_character("get_cip", req, ['int6'])

def get_frm(*req):
    return appel_character("get_frm", req, ['int6'])

def get_the_anxio_spe(*req):
    return appel_refcursor("get_the_anxio_spe", req, ['str', 'int'])
"""
