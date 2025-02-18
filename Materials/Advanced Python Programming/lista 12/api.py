from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modules import Base, Books, Friends, BorrowedBooks
from datetime import datetime

app = Flask(__name__)

engine = create_engine('sqlite:///zadanie1.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Book operations

@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    new_book = Books(title=data['title'], author=data['author'], year=data['year'])
    session.add(new_book)
    session.commit()
    return jsonify({'message': 'Book added successfully'}), 201

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = session.query(Books).filter(Books.id == book_id).first()
    if book:
        return jsonify({'id': book.id, 'title': book.title, 'author': book.author, 'year': book.year})
    return jsonify({'message': 'Book not found'}), 404

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    book = session.query(Books).filter(Books.id == book_id).first()
    if book:
        book.title = data.get('title', book.title)
        book.author = data.get('author', book.author)
        book.year = data.get('year', book.year)
        session.commit()
        return jsonify({'message': 'Book updated successfully'})
    return jsonify({'message': 'Book not found'}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = session.query(Books).filter(Books.id == book_id).first()
    if book:
        session.delete(book)
        session.commit()
        return jsonify({'message': 'Book deleted successfully'})
    return jsonify({'message': 'Book not found'}), 404

# Borrowing book

@app.route('/borrow', methods=['POST'])
def api_borrow_book():
    data = request.json
    book_id = data.get('book_id')
    friend_id = data.get('friend_id')

    book = session.query(Books).filter(Books.id == book_id).one_or_none()
    friend = session.query(Friends).filter(Friends.id == friend_id).one_or_none()

    if not book or not friend:
        return jsonify({'message': 'Book or Friend not found'}), 404

    already_borrowed = session.query(BorrowedBooks).filter(
        BorrowedBooks.book_id == book_id, BorrowedBooks.return_date.is_(None)).one_or_none()
    
    if already_borrowed:
        return jsonify({'message': 'Book is already borrowed'}), 400

    new_borrow = BorrowedBooks(book_id=book_id, friend_id=friend_id)
    session.add(new_borrow)
    session.commit()

    return jsonify({'message': 'Book borrowed successfully'}), 201

# Returning Book

@app.route('/return_book', methods=['PUT'])
def api_return_book():
    data = request.json
    borrow_id = data.get('borrow_id')

    borrow_record = session.query(BorrowedBooks).get(borrow_id)
    if not borrow_record:
        return jsonify({'message': 'Borrow record not found'}), 404

    borrow_record.return_date = datetime.now()
    session.commit()

    return jsonify({'message': 'Book returned successfully'}), 200

# Listing operations 

@app.route('/books', methods=['GET'])
def get_books():
    books = session.query(Books).all()
    return jsonify([{'id': book.id, 'title': book.title, 'author': book.author, 'year': book.year} for book in books])

@app.route('/friends', methods=['GET'])
def get_friends():
    friends = session.query(Friends).all()
    return jsonify([{'id': friends.id, 'name': friends.name, 'email': friends.email} for friends in friends])

@app.route('/borrowed', methods=['GET'])
def get_borrowed():
    borrowed = session.query(BorrowedBooks).all()
    return jsonify([{'id': borrowed.id, 'book_id': borrowed.book_id, 'friend_id': borrowed.friend_id, 
                     'borrow_date': borrowed.borrow_date, 'return_date': borrowed.return_date} for borrowed in borrowed])

# Clearing 

@app.route('/clear_all', methods=['DELETE'])
def api_clear_data():
    session.query(BorrowedBooks).delete()
    session.query(Friends).delete()
    session.query(Books).delete()
    session.commit()
    session.close()
    return jsonify({'message': 'All data cleared'}), 200

if __name__ == '__main__':
    app.run()