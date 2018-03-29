from pythonthesorimed.thesoitem import ThesoItem

a = ThesoItem('localhost', 'thesorimed', 'j', 'j')

import time

nom = ""
for i in "paracetamol":
    nom = nom + i
    print(nom)
    e = a.get_by_gsp(nom)
    z = [x.gsp_nom for x in sorted(e)]
    print([r for r in z])
    time.sleep(1)

# from psycopg2.extras import NamedTupleCursor
# from theso import connect, get_the_spe_details

# def chercheMed():
#     x='1'
#     x = input("entrez la chaine : \n")
#     a = get_the_spe_details([x],0)
#     for i in a:
#         print(i)
#     return

# def recherche_par_nom_spe(var):
#     """
#     requete sql direct
#     """

#     with connect() as con:
#         with con.cursor(cursor_factory=NamedTupleCursor) as curs:
#             curs.execute("""
#             SELECT sp_nom, SP_CIPUCD_LONG
#             FROM thesorimed.sp_specialite s
#             WHERE s.sp_nom LIKE '{}%'
#             """.format(var))
#             # f = "FETCH ALL IN {0};".format(a) #retrieve from cursor
#             # curs.execute(f)
#             cc = curs.fetchall()
#     return cc

# def recherche_par_virtuel(var):
#     """
#     requete sql direct
#     """

#     with connect() as con:
#         with con.cursor(cursor_factory=NamedTupleCursor) as curs:
#             curs.execute("""
#             SELECT gsp_nom
#             FROM thesorimed.GSP_GENERIQUE_SPECIALITE g
#             WHERE g.gsp_nom LIKE '{}%'
#             """.format(var))
#             # f = "FETCH ALL IN {0};".format(a) #retrieve from cursor
#             # curs.execute(f)
#             cc = curs.fetchall()
#     return cc

# # chercheMed()

# x=1

# while x != '0':
#     x = input('Entrez une chaine : \n')
#     print(recherche_par_virtuel(x))