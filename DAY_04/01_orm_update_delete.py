from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

engine = create_engine("sqlite:///:memory:")

class Base(DeclarativeBase):
    """Maps the ORM"""
    pass

class User(Base):
    """Modles the users Table"""
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str | None]

    def __repr__(self):
        return f"User({self.id},{self.name})"

# now creating the table 
Base.metadata.create_all(engine)

with Session(engine) as session:
    user_ali = User(name="Ali Hassnain")
    session.add(user_ali)
    User_shami = User(name = "Shami")
    session.add(User_shami)
    user_sunny = User(name= "Sunny")
    session.add(user_sunny)
    user_shehri = User(name = "Shehri")
    session.add(user_shehri)

    session.commit()

    # displaying the user table
    result = session.execute(select(User))
    print(result.scalars().all())

    """Now updating the shami to ihtisham"""
    user = session.get(User,2)
    user.name = 'Ihtisham'
    session.commit()

    # now displaying the user table again
    result = session.execute(select(User))
    print(result.scalars().all())

    """NOW DELETING THE USER SUNNY ID = 3"""
    user = session.get(User,3)
    session.delete(user)
    session.commit()

    # now displaying the user table again
    result = session.execute(select(User))
    print(result.scalars().all())


