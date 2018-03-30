# Third Party Libraries
from pony.orm import Database, Required

# pythonthesorimed
from pythonthesorimed.thesoitem import ThesoItem

# a = ThesoItem('localhost', 'thesorimed', 'j', 'j')

# print(a.fuzzy('bisoprolol'))


db = Database()


class Virtuel(db.Entity):
    _table_ = "get_cip"
    listid = Required(str)
    typid = Required(int)


db.bind(
    provider="postgres",
    database="thesorimed",
    host="localhost",
    user="j",
    password="j", )

db.generate_mapping(create_tables=False)
