from sqlalchemy import create_engine, ForeignKey, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session

class Base(DeclarativeBase):
    """Modles orm"""
    pass

class User(Base):
    """Models user table"""
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    posts: Mapped[list["Post"]] = relationship(back_populates='user', cascade='all, delete-orphan')

    def __repr__(self):
        return f"User({self.id},{self.name})"


class Post(Base):
    """Models post table"""
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates='posts')

    def __repr__(self):
        return f"Post({self.id},{self.title},{self.user_id})"

engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)


with Session(engine) as session:
    u = User(name = 'Ali')
    session.add(u)
    session.commit()
    p = Post(title = 'First Post', user_id = u.id)
    p1 = Post(title = 'Second Post' , user_id = u.id)
    session.add_all([p,p1])    
    session.commit()

    """Now , if we delete the user 1. Ali, then ses what would happend to the
        table in Posts
    """
    get_user = session.get(User,1)
    session.delete(get_user)
    session.commit()
    result_user = session.execute(select(User))
    result_post = session.execute(select(Post))
    print(result_user.scalars().all())
    print(result_post.scalars().all())


    
    


