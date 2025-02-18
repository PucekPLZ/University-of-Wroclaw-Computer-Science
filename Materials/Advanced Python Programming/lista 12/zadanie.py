from __future__ import annotations
import argparse
from operations import add_book, add_friend, borrow_book, return_book, books, friends, borrowed, clear
from operations import (api_add_book, api_update_book, api_get_book, api_delete_book, api_borrow_book, api_return_book, 
                        api_books, api_friends, api_borrowed, api_clear)

def parse_args():
    parser = argparse.ArgumentParser(description="Books DB")
    parser.add_argument('--use-api', action='store_true', help="Use API for data access")
    subparsers = parser.add_subparsers(dest='command', required=True)

    add_book_parser = subparsers.add_parser('add_book', help="Add a new book")
    add_book_parser.add_argument('--title', required=True, help="Title of the book")
    add_book_parser.add_argument('--author', required=True, help="Author of the book")
    add_book_parser.add_argument('--year', type=int, required=True, help="Year of publication")

    update_book_parser = subparsers.add_parser('update_book', help="Update a book's details")
    update_book_parser.add_argument('--book_id', type=int, required=True, help="ID of the book to update")
    update_book_parser.add_argument('--title', help="New title of the book")
    update_book_parser.add_argument('--author', help="New author of the book")
    update_book_parser.add_argument('--year', type=int, help="New publication year of the book")

    get_book_parser = subparsers.add_parser('get_book', help="Get details of a book")
    get_book_parser.add_argument('--book_id', type=int, required=True, help="ID of the book to retrieve")

    delete_book_parser = subparsers.add_parser('delete_book', help="Delete a book")
    delete_book_parser.add_argument('--book_id', type=int, required=True, help="ID of the book to delete")

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

def main():
    args = parse_args()

    if args.use_api:
        if args.command == 'add_book':
            api_add_book(args.title, args.author, args.year)
        if args.command == 'update_book':
            api_update_book(args.book_id, args.title, args.author, args.year)
        elif args.command == 'get_book':
            api_get_book(args.book_id)
        elif args.command == 'delete_book':
            api_delete_book(args.book_id)
        elif args.command == 'books':
            api_books()
        elif args.command == 'friends':
            api_friends()
        elif args.command == 'borrowed':
            api_borrowed()
        elif args.command == 'borrow_book':
            api_borrow_book(args.book_id, args.friend_id)
        elif args.command == 'return_book':
            api_return_book(args.borrow_id)
        elif args.command == 'clear':
            api_clear()
    else:
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