from sqlalchemy import create_engine,MetaData, Table, select, Integer, String, Column,insert,update, delete

engine = create_engine("sqlite:///:memory:")
metadata = MetaData()

users = Table(
    'users',
    metadata,
    Column('id',Integer,primary_key=True),
    Column('name',String)
)
metadata.create_all(engine)

# inserting the data in the table

with engine.connect() as conn:

    for i in range(0,5):
        user_id:int = int(input("Enter user id : "))
        user_name:str = input("Enter user name : ")
        stmt = insert(users).values(
                id = user_id,
                name = user_name
            ) 
        conn.execute(stmt)
    conn.commit()

"""updating and roll backing"""

with engine.connect() as conn:
    conn.execute(update(users).where(users.c.id==4).values(name = 'dumdum'))
    conn.rollback() # transaction is roll backed, so no change to the databse

    # now displaying the user content
    result = conn.execute(select(users))
    print(result.fetchall())

    # now doing the change then committing
    conn.execute(update(users).where(users.c.id==5).values(name = 'dumdum'))
    conn.commit() # transaction is commit

    # displaying the result after being commited
    result = conn.execute(select(users))
    print(result.fetchall())

    """now doing the main, part"""
    conn.execute(update(users).where(users.c.id==4).values(name='sorry'))
    try:
        conn.execute(update(users).where(users.id)==values('ali'))
    except Exception as e:
        conn.rollback()
        print(f"Following error happened : {e}")

    # now displaying agin the table
    result = select(users)
    print(result.fetchall())
    

