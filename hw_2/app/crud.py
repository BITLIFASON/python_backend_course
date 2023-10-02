import sqlite3
from typing import Union

from fastapi import HTTPException

from .schemas import Book

DB_PATH = "../data/database.sqlite"


def create_db():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(
        """CREATE TABLE book(id INTEGER PRIMARY KEY,
                                        title VARCHAR(50),
                                        author VARCHAR(20),
                                        description VARCHAR(500))"""
    )

    connection.commit()
    connection.close()


def add_book_into_db(book: Book):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("SELECT MAX(id) FROM book LIMIT 1")
    id_ = cursor.fetchall()[0][0]
    if id_:
        id_ += 1
    else:
        id_ = 0

    if book.id is None:
        book.id = id_
    else:
        if book.id > id_:
            raise HTTPException(
                status_code=404, detail="book id is too big, make it smaller"
            )

    cursor.execute(
        "INSERT INTO book (id, title, author, description) VALUES (?, ?, ?, ?)",
        (book.id, book.title, book.author, book.description),
    )

    connection.commit()
    connection.close()


def get_book_by_id(id: int) -> Union[Book, None]:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM book WHERE id = ?", (id,))
    result = cursor.fetchall()
    if result:
        book = Book(
            id=result[0][0],
            title=result[0][1],
            author=result[0][2],
            description=result[0][3],
        )
    else:
        book = None

    connection.close()

    return book


def update_book_by_id(book: Book):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE book SET title=?, author=?, description=? WHERE id=?",
        (book.title, book.author, book.description, book.id),
    )

    connection.commit()
    connection.close()


def delete_book_by_id(id: int):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM book WHERE id=?", (id,))

    connection.commit()
    connection.close()
