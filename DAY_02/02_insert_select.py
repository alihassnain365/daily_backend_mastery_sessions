from sqlalchemy import create_engine,select, MetaData,Insert, Integer,Select, String, Table, Column

engine = create_engine("sqlite:///:memory:")
metadata = MetaData()

# creating the table structure
users = Table(
    'users',
    metadata,
    Column('id',Integer, primary_key=True),
    Column('name',String, nullable=False)
)

# creating the above table
metadata.create_all(engine)

# now inserting data into those tables
with engine.connect() as conn:
    stmt = users.insert().values(
        name = 'Alice'
    )
    conn.execute(stmt)
    conn.commit()


# viewing the users table contents
with engine.connect() as conn:
    stmt = Select(users)
    result = conn.execute(stmt)
    print(result.fetchall())

"""inserting the five names one by one for pracitce"""

with engine.connect() as conn:
    stmt = Insert(users).values(
        id = 2,
        name = 'ali'
    )
    stmt2 = users.insert().values(
        id = 3,
        name = 'shami'
    )
    stmt3 = Insert(users).values(
        id = 4,
        name = 'shehri'
    )
    stmt4 = Insert(users).values(
        id = 5,
        name = 'sunny'
    )

    l = [stmt,stmt2,stmt3,stmt4]
    for st in l:
        conn.execute(st)
    conn.commit()

# now viewing the results
with engine.connect() as conn:
    stmt = Select(users)
    result = conn.execute(stmt)
    print(result.fetchall())

# now filtering thoroug where

with engine.connect() as conn:
    stmt = select(users).where(users.c.id==2)
    result = conn.execute(stmt)
    print(result.fetchall())
