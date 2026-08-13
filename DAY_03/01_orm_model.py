from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///:memory:")
class Base(DeclarativeBase):
    """Maps the ORM"""
    pass

class User(Base):
    """Models the users Table"""
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] 

"""IN orm, if we dont mention the optional , then that columns is considered 
    Not Null, 
    name: Mapped[str] -> is considered automatically not null
    while,
    name: Mapped[str | None] -> is treated normally can be null

"""

# now creating the tables via orm model
Base.metadata.create_all(engine)

# now verifying the table existence
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM sqlite_master WHERE type = 'table'"))
    print(result.fetchall())


