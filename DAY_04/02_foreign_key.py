from sqlalchemy import create_engine, select, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship

engine = create_engine("sqlite:///:memory:")

class Base(DeclarativeBase):
    """Models orm"""
    pass

class User(Base):
    """Models Users table"""
    __tablename__ = "users"
    id : Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str|None]
    posts: Mapped[list["Post"]] = relationship(back_populates="user")

class Post(Base):
    """Models posts table """
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    user_id : Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="posts")

    def __repr__(self):
        return f"Post({self.id},{self.title})"
Base.metadata.create_all(engine)

with Session(engine) as session:
    user_ali = User(name = 'Ali Hassnain')
    session.add(user_ali)
    session.commit()
    post_ali = Post(user_id = user_ali.id ,title = "I love el")
    session.add(post_ali)
    session.commit()
    result = session.get(Post, post_ali.id)
    print(result.user.name)

    temp = session.get(User,1)
    temp.name = 'Ihtisham'
    session.commit()
    result = session.get(Post, 1)
    print(result.user.name)



