intro = """
\"\"\"
Attention  : fichier autogénéré.
Ne pas l'éditer à la main.
Pour l'éditer, utiliser parseur
Il faut configurer host, dbn user et password à la main.

\"\"\"
"""

import_and_nametupple_def = """
# Standard Libraries
from collections import namedtuple

ProcApi = namedtuple('ProcApi', 'name input_type genre')


"""

base_func = """
def {name}(*req):
    return {appel}(\"{name}\", req, {params})
"""
