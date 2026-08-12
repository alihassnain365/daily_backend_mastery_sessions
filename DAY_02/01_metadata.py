"""we import metadat class from sqlalchemy, then create an object of that 
    class, each time we create a table , we associates that metadat object to
    that table, so that it know the struncture of that table

"""

from sqlalchemy import create_engine,MetaData,text, Table, Integer, Column, String

engine = create_engine("sqlite:///:memory:")
metadata = MetaData()

# defining the structure of the table
# no primary key setted
users = Table(
    "users",
    metadata,
    Column("id", Integer),

    Column("name", String)
)

# user 2 - with primary key setted up in the seperate metdata

metadata2 = MetaData()

users = Table(
    "users",
    metadata2,
    Column("id",Integer, primary_key=True),
    Column('name',String, nullable=False)
)

# now creating that above table
metadata.create_all(engine)
metadata2.create_all(engine)
with engine.connect() as conn:
    result = conn.execute(text("SELECT name FROM sqlite_master WHERE type = 'table'"))
    print(result.fetchall())

with engine.connect() as conn:
    result = conn.execute(text("PRAGMA table_info(users)"))
    print(result.fetchall())


"""

CONCLUSION : create_all() just see the name of the table, no matter you
             created the new metadata object, if the name already exists
             it would never create that table.
             
"""



