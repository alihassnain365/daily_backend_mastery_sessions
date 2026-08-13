from sqlalchemy import create_engine, text, select
from sqlalchemy.orm import Mapped,  Session, DeclarativeBase, mapped_column

engine = create_engine("sqlite:///:memory:")

class Base(DeclarativeBase):
    """Models ORM"""
    pass

class User(Base):
    """Models user table"""
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str | None]

    def __repr__(self):
        return f"User({self.id},{self.name})"

# now creating the tables
Base.metadata.create_all(engine)

with Session(engine) as session:
    user_ali = User(id = 1, name = 'Ali Hassnain')
    user_shami = User(id = 2,name = 'Shami')
    user_sunny = User(id = 3,name = 'Sunny')
    # now adding the changes to session to be tracked
    session.add(user_ali)
    session.add(user_shami)
    session.add(user_sunny)
    # now committing the tracked changes
    session.commit()
    result1 = session.get(User,1)
    result2 = session.get(User,99)
    result3 = session.execute(select(User))
    greater_users = session.execute(select(User).where(User.id > 1))

    # now printing every results
    print(result1)
    print(result2)
    print(result3.scalars().all())
    print(greater_users.scalars().all())


    
