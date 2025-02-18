import unittest
from unittest.mock import patch
from program.api import app
from program.modules import Books


class TestApiEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch("api.session")
    def test_add_book(self, mock_session):
        response = self.app.post(
            "/books", json={"title": "Test Book", "author": "Test Author", "year": 2020}
        )
        self.assertEqual(response.status_code, 201)

    @patch("api.session")
    def test_get_book_not_found(self, mock_session):
        mock_session.query(Books).filter.return_value.first.return_value = None
        response = self.app.get("/books/1")
        self.assertEqual(response.status_code, 404)

    @patch("api.session")
    def test_delete_book(self, mock_session):
        mock_session.query(Books).filter.return_value.first.return_value = Books()
        response = self.app.delete("/books/1")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
