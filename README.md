# Pythothesorimed


[![](https://travis-ci.org/jgirardet/pythonthesorimed.svg?branch=master)](https://travis-ci.org/jgirardet/pythonthesorimed)


Interface python pour thesorimed


* License : GNU General Public License v3 
    * [Documentation: ](https://pythonthesorimed.readthedocs.org/en/latest/)
* Source: [[https://github.com/jgirardet/pythonthesorimed]]


Simple Interface Python pour utiliser l'api thesorimed compatible postgresql


## Features


* Génère l'API python depuis le fichier thesormed api.sql
* Fournit la class ThesoItem pour les appels à la base

## Installation


    pipenv install pythonthesorimed
    ou
    pip install pythonthesorimed
## Usage

### Initialisation


    from pythonthesorimed.thesoitem import ThesoItem
    session = ThesoItem(host, base, user, password)

gergerg
```python
from pythonthesorimed.thesoitem import ThesoItem
session = ThesoItem(host, base, user, password)
```

	

### Utilisation des API thesorimed

result = session.proc('api_name', param1, param2, param3)

Le retour est un Record ou un liste de Record. Record est un object possédant comme attribut les colonnes associées à la requète

par exemple : 

{{{
#python

>>> session.proc('get_the_gen_equiv', 3, 1)
[Record(gsp_nom='RIFADINE 300MG GELULE', sp_code_equiv=4793, lib_virt='Rifampicine 300 mg gelule', sp_param='RIMACTAN 300MG GELULE', sp_code_sq_pk=3),
Record(gsp_nom='RIMACTAN 300MG GELULE', sp_code_equiv=3, lib_virt='Rifampicine 300 mg gelule', sp_param='RIMACTAN 300MG GELULE', sp_code_sq_pk=3)]
>>> result[0].gsp_nom
'RIFADINE 300MG GELULE'
}}}