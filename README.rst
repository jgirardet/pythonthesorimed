===============================
pythonthesorimed
===============================

.. image:: https://travis-ci.org/jgirardet/pythonthesorimed.svg?branch=master
    :target: https://travis-ci.org/jgirardet/pythonthesorimed
.. image:: https://readthedocs.org/projects/pythonthesorimed/badge/?version=latest
   :target: http://pythonthesorimed.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
.. image:: https://coveralls.io/repos/github/jgirardet/pythonthesorimed/badge.svg
   :target: https://coveralls.io/github/jgirardet/pythonthesorimed
.. image:: https://badge.fury.io/py/pythonthesorimed.svg
   :target: https://pypi.python.org/pypi/pythonthesorimed/
   :alt: Pypi package


Interface python pour thesorimed


* License : GNU General Public License v3 
* Documentation: https://pythonthesorimed.readthedocs.org/en/latest/
* Source: https://github.com/jgirardet/pythonthesorimed


Simple Interface Python pour utiliser l'api thesorimed compatible postgresql


Features
--------

* Génère l'API python depuis le fichier thesormed api.sql
* Fournit la class ThesoItem pour les appels à la base


Installation
-------------

.. code-block:: shell

    pipenv install pythonthesorimed
    ou
    pip install pythonthesorimed

Usage
-----

.. code-block:: python

	from pythonthesorimed.thesoitem import ThesoItem
	session = ThesoItem(host, base, user, password)
	result = session.proc('api_name', param1, param2, param3)

Le retour est un Record ou un liste de Record. Record est un object possédant comme attribut les colonnes associées à la requète

par exemple : 

.. code-block:: python

    >>> session.proc('get_the_gen_equiv', 3, 1)
	[Record(gsp_nom='RIFADINE 300MG GELULE', sp_code_equiv=4793, lib_virt='Rifampicine 300 mg gelule', sp_param='RIMACTAN 300MG GELULE', sp_code_sq_pk=3),
 	Record(gsp_nom='RIMACTAN 300MG GELULE', sp_code_equiv=3, lib_virt='Rifampicine 300 mg gelule', sp_param='RIMACTAN 300MG GELULE', sp_code_sq_pk=3)]
 	
 	>>> result[0].gsp_nom
	'RIFADINE 300MG GELULE'

Parseur
--------

Cloner le dépot puis : 

.. code-block:: shell

    make dev
    pr python build.py path/to/api.sql

api.py est maintenant dans pythonthesorimed

Testing
---------

make test : toutes les fonctionnalitées ne nécessitant pas le base de donnée thesorimed
make test-local : tests avec des appels à thesorimed
make all : tout

Travis utilise la version "make test"

Coverage
------------
make test-coverage
make test-coverage-all
