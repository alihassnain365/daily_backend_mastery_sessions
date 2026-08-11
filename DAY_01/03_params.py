from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///:memory:")

with engine.connect() as conn:
    conn.execute(text("CREATE TABLE users (id INTEGAR, name TEXT)"))
    conn.execute(text("INSERT INTO users VALUES (1, 'alice')"))
    conn.execute(text("INSERT INTO users VALUES (2,'bob')"))
    conn.commit()


# suppose somone give you this query

user_input = "1 OR 1=1"
unsafe_query = f"SELECT * FROM users WHERE id = {user_input}"

with engine.connect() as fault:
    result = fault.execute(text(unsafe_query))
    print(result.fetchall())


# safe version

# with engine.connect() as good:
#     result = good.execute(text("SELECT * FROM users WHERE id = :id")
#                           ,{"id" : user_input})
#     print(result.fetchall())

