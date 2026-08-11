from sqlalchemy import create_engine, text


engine = create_engine("sqlite:///:memory:")

with engine.connect() as conn:
    result = conn.execute(text("Select 1"))
    print(result.fetchone())


