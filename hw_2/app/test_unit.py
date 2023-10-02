import sqlite3
import pytest

from .schemas import Book
from .crud import add_book_into_db, get_book_by_id, update_book_by_id, delete_book_by_id

DB_PATH = "../data/database.sqlite"


@pytest.mark.parametrize(
    "id, title, author, description",
    [
        (4, None, None, None),
        (4, None, "B", "C"),
        (4, "A", None, "C"),
        (4, "A", "B", None),
        (4, "A", "B", "C"),
    ],
)
def test_add_book(create_test_db, id, title, author, description):
    init_book = Book(id=id, title=title, author=author, description=description)

    add_book_into_db(init_book)

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM book WHERE id = ?", (id,))
    result = cursor.fetchall()
    if result:
        result_book = Book(
            id=result[0][0],
            title=result[0][1],
            author=result[0][2],
            description=result[0][3],
        )
    else:
        result_book = None

    connection.close()

    assert result_book == init_book


@pytest.mark.parametrize(
    "id, title, author, description",
    [
        (0, "Pride and Prejudice", "Jane Austen", "first published in 1813"),
        (1, "Crime and Punishment", "Fyodor Dostoevsky", "first published in 1866"),
        (
            2,
            "Around the World in Eighty Days",
            "Juiles Verne",
            "first published in 1873",
        ),
        (3, "Metro 2033", "Dmitry Glukhovsky", "first published in 2005"),
        (100, None, None, None),
    ],
)
def test_get_book(create_test_db, id, title, author, description):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM book WHERE id = ?", (id,))
    result = cursor.fetchall()
    if result:
        init_book = Book(
            id=result[0][0],
            title=result[0][1],
            author=result[0][2],
            description=result[0][3],
        )
    else:
        init_book = None

    connection.close()

    result_book = get_book_by_id(id)

    assert init_book == result_book


@pytest.mark.parametrize(
    "id, title, author, description",
    [
        (0, None, None, None),
        (1, None, "B", "C"),
        (2, "A", None, "C"),
        (3, "A", "B", None),
    ],
)
def test_update_book(create_test_db, id, title, author, description):
    init_book = Book(id=id, title=title, author=author, description=description)

    update_book_by_id(book=init_book)

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM book WHERE id = ?", (id,))
    result = cursor.fetchall()
    if result:
        result_book = Book(
            id=result[0][0],
            title=result[0][1],
            author=result[0][2],
            description=result[0][3],
        )
    else:
        result_book = None

    connection.close()

    assert init_book == result_book


@pytest.mark.parametrize(
    "id, exception_value",
    [
        (0, None),
        (2, None),
        (100, None),
    ],
)
def test_delete_book(create_test_db, id, exception_value):
    delete_book_by_id(id)

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM book WHERE id = ?", (id,))
    result = cursor.fetchall()
    if result:
        result_book = Book(
            id=result[0][0],
            title=result[0][1],
            author=result[0][2],
            description=result[0][3],
        )
    else:
        result_book = None

    connection.close()

    assert result_book == exception_value
