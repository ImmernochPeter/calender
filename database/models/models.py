"""Models File"""
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


# pylint:disable=too-few-public-methods
class User(Base):  # type:ignore
    "DB Model for User"
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)


# pylint:disable=too-few-public-methods
class Note(Base):  # type:ignore
    """DB Model for Note"""

    __tablename__ = "note"

    id = Column(Integer, primary_key=True)
    header = Column(String, nullable=False)
    content = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", backref="notes")
