from sqlalchemy import create_engine, ForeignKey, select, Table, Column
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
    tags: Mapped[list["Tag"]] = relationship("Tag", secondary="post_tag", back_populates='posts')

    def __repr__(self):
        return f"Post({self.id},{self.title},{self.user_id})"

class Tag(Base):
    """Models the tag table"""
    __tablename__ = "tags"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    posts: Mapped[list["Post"]] = relationship("Post", secondary="post_tag", back_populates='tags')

post_tag = Table(
    "post_tag",
    Base.metadata,
    Column("post_id", ForeignKey("posts.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True)
)

engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)

with Session(engine) as session:
    user_ali = User(name= 'Ali Hassnain')
    p1 = Post(title= 'First Post')
    tag1 = Tag(name = '#fyp')
    tag2 = Tag(name = '#foryou')
    session.add(user_ali)
    p1.tags.append(tag1)
    p1.tags.append(tag2)
    session.add(p1)
    session.commit()

    result = session.execute(select(Tag)).scalars().all()
    for tag in result:
        print(tag.name, [p.title for p in tag.posts])
