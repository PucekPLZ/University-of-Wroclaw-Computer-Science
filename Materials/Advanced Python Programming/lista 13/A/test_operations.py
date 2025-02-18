import unittest
from unittest.mock import patch
import program.operations as operations


class TestOperationsFunctions(unittest.TestCase):
    @patch("operations.DBSession")
    def test_add_book(self, mock_session):
        operations.add_book("Test Book", "Test Author", 2020)
        mock_session.return_value.add.assert_called()
        mock_session.return_value.commit.assert_called()

    @patch("operations.requests.post")
    def test_api_add_book(self, mock_post):
        mock_post.return_value.json.return_value = {
            "message": "Book added successfully"
        }
        operations.api_add_book("Test Book", "Test Author", 2020)
        mock_post.assert_called_with(
            "http://127.0.0.1:5000/books",
            json={"title": "Test Book", "author": "Test Author", "year": 2020},
        )

    @patch("operations.DBSession")
    def test_borrow_book_not_found(self, mock_session):
        mock_session.return_value.query.return_value.filter.return_value.one_or_none.return_value = (
            None
        )
        operations.borrow_book(1, 1)
        mock_session.return_value.add.assert_not_called()


if __name__ == "__main__":
    unittest.main()
