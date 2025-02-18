from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, ForeignKey, String, Date
from sqlalchemy.orm import relationship, mapped_column
from datetime import datetime

class Base(DeclarativeBase):
    pass

class Books(Base):
    __tablename__ = "Books"
    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String, nullable=False, unique=True)
    author = mapped_column(String, nullable=False)
    year = mapped_column(Integer, nullable=False)

    borrowed_books = relationship("BorrowedBooks", back_populates="book")

class Friends(Base):
    __tablename__ = "Friends"
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, nullable=False)
    email = mapped_column(String, nullable=False, unique=True)

    borrowed_books = relationship("BorrowedBooks", back_populates="friend")

class BorrowedBooks(Base):
    __tablename__ = "BorrowedBooks"
    id = mapped_column(Integer, primary_key=True)
    book_id = mapped_column(Integer, ForeignKey('Books.id'), nullable=False)
    friend_id = mapped_column(Integer, ForeignKey('Friends.id'), nullable=False)
    borrow_date = mapped_column(Date, default=datetime.now)
    return_date = mapped_column(Date, nullable=True)

    book = relationship("Books", back_populates="borrowed_books")
    friend = relationship("Friends", back_populates="borrowed_books")