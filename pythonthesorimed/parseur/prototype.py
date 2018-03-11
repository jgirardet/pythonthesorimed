
intro = """
\"\"\"
Attention  : fichier autogénéré.
Ne pas l'éditer à la main.
Pour l'éditer, utiliser parseur
Il faut configurer host, dbn user et password à la main.

\"\"\"



import psycopg2
from psycopg2.extras import NamedTupleCursor
"""


connect = """
def connect():
    \"\"\"
    Base fonction to connect to database.
    Return a pscipg connection
    \"\"\"

    return psycopg2.connect(host="127.0.0.1", dbname="aaa", user="j", password="j")
"""

appel_refcursor = """
def appel_refcursor(name, req, params):
    \"\"\"
    Deal with procedure wich returns refcursor
    \"\"\"

    # convert [int,int,int] to 'int,int, int'
    req = list(req)
    for i in range(len(req)):
        if 'str' in params[i]:
            req[i] = ','.join(map(str,req[i]))
    #create connection
    with connect() as con:
        with con.cursor(cursor_factory=NamedTupleCursor) as curs:
            curs.execute("SET search_path TO thesorimed, public")
            curs.callproc("thesorimed."+name,req)

            cc = curs.fetchone()[0] #get the cursor
            a = '"' + cc + '"'
            f = "FETCH ALL IN {0};".format(a) #retrieve from cursor
            curs.execute(f)
            cc = curs.fetchall()
    return cc
"""

appel_character = """
def appel_character(name, req, params):
    \"\"\"
    DEal With procedure wich retruns a value
    \"\"\"

    req = list(req) #list to modify tupple
    if 'str' in params[0]:  # turn arg to str if varchar
        req[0]=str(req[0])


    with connect() as con:
        with con.cursor(cursor_factory=NamedTupleCursor) as curs:
            curs.execute("SET search_path TO thesorimed, public")
            curs.callproc("thesorimed."+name, req)
            res = curs.fetchone()
            cc = getattr(res, name)
    return cc
"""


appel_refcursor="""
def appel_refcursor(name, req, params):

    # convert [int,int,int] to 'int,int, int'
    req = list(req)
    for i in range(len(req)):
        if 'str' in params[i]:
            req[i] = ','.join(map(str,req[i]))
    #create connection
    with connect() as con:
        with con.cursor(cursor_factory=NamedTupleCursor) as curs:
            curs.execute("SET search_path TO thesorimed, public")
            curs.callproc("thesorimed."+name,req)

            cc = curs.fetchone()[0] #get the cursor
            a = '"' + cc + '"'
            f = "FETCH ALL IN {0};".format(a) #retrieve from cursor
            curs.execute(f)
            cc = curs.fetchall()
    return cc
"""

base_func = """
def {name}(*req):
    return {appel}(\"{name}\", req, {params})
"""
