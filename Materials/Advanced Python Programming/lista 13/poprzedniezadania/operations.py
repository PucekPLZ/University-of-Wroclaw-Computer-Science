import requests
from program.modules import Books, Friends, BorrowedBooks
from datetime import datetime
from program.api import DBSession
from typing import Optional, NoReturn


API_URL = "http://127.0.0.1:5000"


def add_book(title: str, author: str, year: int) -> None:
    """
    Add a new book to the database.

    :param title: Title of the book
    :param author: Author of the book
    :param year: Publication year of the book
    """
    session = DBSession()
    new_book = Books(title=title, author=author, year=year)
    session.add(new_book)
    session.commit()
    print(f"Book '{title}' by {author} in {year} added.")
    session.close()


def add_friend(name: str, email: str) -> None:
    """
    Add a new friend to the database.

    :param name: Name of the friend
    :param email: Email of the friend
    """
    session = DBSession()
    new_friend = Friends(name=name, email=email)
    session.add(new_friend)
    session.commit()
    print(f"Friend {name} {email} added.")
    session.close()


def borrow_book(book_id: int, friend_id: int) -> None:
    """
    Create a record for borrowing a book in database.

    :param book_id: The ID of the book being borrowed.
    :param friend_id: The ID of the friend borrowing the book.
    """
    session = DBSession()
    book = session.query(Books).filter(Books.id == book_id).one_or_none()
    friend = session.query(Friends).filter(Friends.id == friend_id).one_or_none()

    already_borrowed = (
        session.query(BorrowedBooks)
        .filter(BorrowedBooks.book_id == book_id, BorrowedBooks.return_date.is_(None))
        .one_or_none()
    )

    if already_borrowed:
        print(f"Book ID {book.id} is already borrowed and not yet returned.")
        session.close()
        return

    if not friend:
        print(f"No friend found with ID {friend_id}.")
        session.close()
        return

    if not book:
        print(f"No book found with ID {book_id}.")
        session.close()
        return

    new_borrow = BorrowedBooks(book_id=book_id, friend_id=friend_id)
    borrow_record = session.query(BorrowedBooks).get(book_id)
    session.add(new_borrow)
    session.commit()
    print(
        f"Book ID {book.id} borrowed by Friend ID {friend.id} at {borrow_record.borrow_date}."
    )
    session.close()


def return_book(borrow_id: int) -> None:
    """
    Mark a borrowed book as returned.

    :param borrow_id: The ID of the borrow record to update.
    """
    session = DBSession()
    borrow_record = session.query(BorrowedBooks).get(borrow_id)
    if borrow_record:
        borrow_record.return_date = datetime.now()
        session.commit()
        print(
            f"Borrowed record ID {borrow_id} marked as returned at {borrow_record.return_date}."
        )
    else:
        print(f"No borrowed record found with ID {borrow_id}")
    session.close()


def books() -> None:
    """
    Print a list of all books in the database.
    """
    session = DBSession()
    books = session.query(Books).all()
    for book in books:
        print(
            f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}"
        )
    session.close()


def friends() -> None:
    """
    Print a list of all friends in the database.
    """
    session = DBSession()
    friends = session.query(Friends).all()
    for friend in friends:
        print(f"ID: {friend.id}, Name: {friend.name}, Email: {friend.email}")
    session.close()


def borrowed() -> None:
    """
    Print a list of all active borrowed book records.
    """
    session = DBSession()
    borrowed_books = (
        session.query(BorrowedBooks).filter(BorrowedBooks.return_date.is_(None)).all()
    )
    for record in borrowed_books:
        book = session.query(Books).get(record.book_id)
        friend = session.query(Friends).get(record.friend_id)
        print(
            f"Borrow ID: {record.id} Book ID: {record.book_id}, Title: {book.title}, Borrowed by: {friend.name}, Borrow Date: {record.borrow_date}"
        )

    session.close()


def clear() -> None:
    """
    Clear all data.
    """

    session = DBSession()
    session.query(BorrowedBooks).delete()
    session.query(Friends).delete()
    session.query(Books).delete()
    session.commit()
    print("All data cleared.")
    session.close()


def api_add_book(title: str, author: str, year: int) -> None:
    """
    Add a new book to the database API.

    :param title: Title of the book
    :param author: Author of the book
    :param year: Publication year of the book
    """
    response = requests.post(
        f"{API_URL}/books", json={"title": title, "author": author, "year": year}
    )
    print(response.json()["message"])


def api_get_book(book_id: int) -> None:
    """
    Get book from the database API.

    :param book_id: Id of the book
    """
    response = requests.get(f"{API_URL}/books/{book_id}")
    if response.ok:
        book = response.json()
        print(
            f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Year: {book['year']}"
        )
    else:
        print("Book not found.")


def api_update_book(book_id: int, title: Optional[str] = None, author: Optional[str] = None, year: Optional[str] = None) -> None:
    """
    Update book to the database API.

    :param book_id: Id of the book
    :param title: Title of the book
    :param author: Author of the book
    :param year: Publication year of the book
    """
    data = {}
    if title:
        data["title"] = title
    if author:
        data["author"] = author
    if year:
        data["year"] = year

    response = requests.put(f"{API_URL}/books/{book_id}", json=data)
    print(response.json()["message"])


def api_delete_book(book_id: int) -> None:
    """
    Delete book from the database API.

    :param book_id: Id of the book
    """
    response = requests.delete(f"{API_URL}/books/{book_id}")
    print(response.json()["message"])


def api_borrow_book(book_id: int, friend_id: int) -> None:
    """
    Create a record for borrowing a book in the database API.

    :param book_id: The ID of the book being borrowed.
    :param friend_id: The ID of the friend borrowing the book.
    """
    response = requests.post(
        f"{API_URL}/borrow", json={"book_id": book_id, "friend_id": friend_id}
    )
    if response.ok:
        print("Book borrowed successfully.")
    else:
        print("Failed to borrow book.", response.json().get("message", ""))


def api_return_book(borrow_id: int) -> None:
    """
    Mark a borrowed book as returned in the database API.

    :param borrow_id: The ID of the borrow record to update.
    """
    response = requests.put(f"{API_URL}/return_book", json={"borrow_id": borrow_id})
    if response.ok:
        print("Book returned successfully.")
    else:
        print("Failed to return book.", response.json().get("message", ""))


def api_books() -> None:
    """
    Print a list of all books in the database API.
    """
    response = requests.get(f"{API_URL}/books")
    if response.ok:
        for book in response.json():
            print(
                f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Year: {book['year']}"
            )
    else:
        print("Failed to retrieve books.")


def api_friends() -> None:
    """
    Print a list of all friends in the database API.
    """
    response = requests.get(f"{API_URL}/friends")
    if response.ok:
        for friend in response.json():
            print(
                f"ID: {friend['id']}, Name: {friend['name']}, Email: {friend['email']}"
            )
    else:
        print("Failed to retrieve friends.")


def api_borrowed() -> None:
    """
    Print a list of all active borrowed books in the database API.
    """
    response = requests.get(f"{API_URL}/borrowed")
    if response.ok:
        for borrow in response.json():
            print(
                f"Borrow ID: {borrow['id']}, Book ID: {borrow['book_id']}, Friend ID: {borrow['friend_id']}, "
                f"Borrow Date: {borrow['borrow_date']}, Return Date: {borrow['return_date']}"
            )
    else:
        print("Failed to retrieve borrowed records.")


def api_clear() -> None:
    """
    Clear all data API.
    """
    response = requests.delete(f"{API_URL}/clear_all")
    if response.ok:
        print("All data cleared.")
    else:
        print("Failed to clear data.", response.json().get("message", ""))
