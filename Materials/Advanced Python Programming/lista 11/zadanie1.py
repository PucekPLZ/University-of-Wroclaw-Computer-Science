from __future__ import annotations
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, ForeignKey, String, Date
from sqlalchemy.orm import relationship, mapped_column
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import argparse

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

engine = create_engine('sqlite:///zadanie1.db', echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def parse_args():
    parser = argparse.ArgumentParser(description="Books DB")
    subparsers = parser.add_subparsers(dest='command', required=True)

    add_book_parser = subparsers.add_parser('add_book', help="Add a new book")
    add_book_parser.add_argument('--title', required=True, help="Title of the book")
    add_book_parser.add_argument('--author', required=True, help="Author of the book")
    add_book_parser.add_argument('--year', type=int, required=True, help="Year of publication")

    add_friend_parser = subparsers.add_parser('add_friend', help="Add a new friend")
    add_friend_parser.add_argument('--name', required=True, help="Name of a friend")
    add_friend_parser.add_argument('--email', required=True, help="Email of a friend")

    borrow_book_parser = subparsers.add_parser('borrow_book', help="Borrow a book")
    borrow_book_parser.add_argument('--book_id', type=int, required=True, help="ID of the book to borrow")
    borrow_book_parser.add_argument('--friend_id', type=int, required=True, help="ID of the friend borrowing the book")

    return_book_parser = subparsers.add_parser('return_book', help="Return a borrowed book")
    return_book_parser.add_argument('--borrow_id', type=int, required=True, help="ID of the borrowed book record")

    books_parser = subparsers.add_parser('books', help="List all books")
    friends_parser = subparsers.add_parser('friends', help="List all friends")
    borrowed_parser = subparsers.add_parser('borrowed', help="List all borrowed books")

    clear_parser = subparsers.add_parser('clear', help="Clear all data from the database")

    return parser.parse_args()

def add_book(title, author, year):
    session = Session()
    new_book = Books(title=title, author=author, year=year)
    session.add(new_book)
    session.commit()
    print(f"Book '{title}' by {author} in {year} added.")
    session.close()

def add_friend(name, email):
    session = Session()
    new_friend = Friends(name=name, email=email)
    session.add(new_friend)
    session.commit()
    print(f"Friend {name} {email} added.")
    session.close()

def borrow_book(book_id, friend_id):
    session = Session()

    friend = session.query(Friends).filter(Friends.id == friend_id).one_or_none()
    if not friend:
        print(f"No friend found with ID {friend_id}.")
        session.close()
        return

    book = session.query(Books).filter(Books.id == book_id).one_or_none()
    if not book:
        print(f"No book found with ID {book_id}.")
        session.close()
        return

    already_borrowed = session.query(BorrowedBooks).filter(
        BorrowedBooks.book_id == book_id, BorrowedBooks.return_date.is_(None)).one_or_none()
    
    if already_borrowed:
        print(f"Book ID {book.title} is already borrowed and not yet returned.")
        session.close()
        return

    new_borrow = BorrowedBooks(book_id=book_id, friend_id=friend_id)
    borrow_record = session.query(BorrowedBooks).get(book_id)
    session.add(new_borrow)
    session.commit()
    print(f"Book ID {book.title} borrowed by Friend ID {friend.name} at {borrow_record.borrow_date}.")
    session.close()

def return_book(borrow_id):
    session = Session()
    borrow_record = session.query(BorrowedBooks).get(borrow_id)
    if borrow_record:
        borrow_record.return_date = datetime.now()
        session.commit()
        print(f"Borrowed record ID {borrow_id} marked as returned at {borrow_record.return_date}.")
    else:
        print(f"No borrowed record found with ID {borrow_id}")
    session.close()

def books():
    session = Session()
    books = session.query(Books).all()
    for book in books:
        print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}")
    session.close()

def friends():
    session = Session()
    friends = session.query(Friends).all()
    for friend in friends:
        print(f"ID: {friend.id}, Name: {friend.name}, Email: {friend.email}")
    session.close()

def borrowed():
    session = Session()
    borrowed_books = session.query(BorrowedBooks).filter(BorrowedBooks.return_date.is_(None)).all()
    for record in borrowed_books:
        book = session.query(Books).get(record.book_id)
        friend = session.query(Friends).get(record.friend_id)
        print(f"Borrow ID: {record.id} Book ID: {record.book_id}, Title: {book.title}, Borrowed by: {friend.name}, Borrow Date: {record.borrow_date}")
        
    session.close()

def clear():
    session = Session()
    session.query(BorrowedBooks).delete()
    session.query(Friends).delete()
    session.query(Books).delete()
    session.commit()
    print("All data cleared.")
    session.close()

def main():
    args = parse_args()
    if args.command == 'add_book':
        add_book(args.title, args.author, args.year)
    elif args.command == 'add_friend':
        add_friend(args.name, args.email)
    elif args.command == 'borrow_book':
        borrow_book(args.book_id, args.friend_id)
    elif args.command == 'return_book':
        return_book(args.borrow_id)
    elif args.command == 'books':
        books()
    elif args.command == 'friends':
        friends()
    elif args.command == 'borrowed':
        borrowed()
    elif args.command == 'clear':
        clear()

if __name__ == "__main__":
    main()