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

"""Now update the name to Ulfat where id == 4"""

update_stmt = update(users).values(
    name = 'Ulfat'
    ).where(users.c.id==4)

with engine.connect() as conn_update:
    conn_update.execute(update_stmt)
    conn_update.commit()


"""Now delete where id == 5"""
with engine.connect() as delete_conn:
    stmt = delete(users).where(users.c.id==5)
    delete_conn.execute(stmt)
    delete_conn.commit()

with engine.connect() as conn:
    select_stmt = select(users)
    result = conn.execute(select_stmt)
    print(result.fetchall())

