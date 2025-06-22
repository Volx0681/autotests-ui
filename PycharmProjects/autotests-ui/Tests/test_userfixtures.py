import pytest

@pytest.fixture
def clear_books_database() -> None:
    print("[fixture] delete_books_database")

@pytest.fixture
def fill_books_database() -> None:
    print("[fixture] fill_books_database")

@pytest.mark.usefixtures("clear_books_database", "fill_books_database")
def test_read_all_books_in_library():
    print("reading all books in library")

@pytest.mark.usefixtures("clear_books_database", "fill_books_database")
class TestLibrary:
    def test_read_book_in_library(self):
        print("reading book in library")

    def test_delete_book_from_library(self):
        print("deleting book from library")
