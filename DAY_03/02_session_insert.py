from sqlalchemy import create_engine, text, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

engine = create_engine("sqlite:///:memory:")

class Base(DeclarativeBase):
    """ORM model"""
    pass

class User(Base):
    """Models the users Table"""
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str | None]

Base.metadata.create_all(engine)

with Session(engine) as session:
    user_ali = User(name="Ali Hassnain")
    session.add(user_ali)
    print(user_ali.id) # should print None, as id is not assigned yet
    session.commit()
    print(user_ali.id) # this time print 1 as  changed occur in data base

with engine.connect() as conn:
    print(conn.execute(text("SELECT * FROM users")).fetchall())

