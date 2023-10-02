"""pytest fixtures."""

import os
import shutil
import sqlite3
import pytest
import shutil


DB_PATH = "../data/database.sqlite"


@pytest.fixture(scope="session")
def connect_db(DB_PATH=DB_PATH):
    connection = sqlite3.connect(DB_PATH)
    return connection


@pytest.fixture(scope="function")
def create_test_db():
    if os.path.exists(DB_PATH):
        shutil.copyfile(DB_PATH, DB_PATH[:-7] + "_copy" + DB_PATH[-7:])
        os.remove(DB_PATH)

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(
        """CREATE TABLE book(id INTEGER PRIMARY KEY,
                                        title VARCHAR(50),
                                        author VARCHAR(20),
                                        description VARCHAR(500))"""
    )
    connection.commit()

    ids = [0, 1, 2, 3]
    titles = [
        "Pride and Prejudice",
        "Crime and Punishment",
        "Around the World in Eighty Days",
        "Metro 2033",
    ]
    authors = ["Jane Austen", "Fyodor Dostoevsky", "Juiles Verne", "Dmitry Glukhovsky"]
    descriptions = [
        "first published in 1813",
        "first published in 1866",
        "first published in 1873",
        "first published in 2005",
    ]
    for id, title, author, description in zip(ids, titles, authors, descriptions):
        cursor.execute(
            "INSERT INTO book (id, title, author, description) VALUES (?, ?, ?, ?)",
            (id, title, author, description),
        )
        connection.commit()

    connection.close()

    yield

    os.remove(DB_PATH)
    if os.path.exists(DB_PATH[:-7] + "_copy" + DB_PATH[-7:]):
        os.rename(DB_PATH[:-7] + "_copy" + DB_PATH[-7:], DB_PATH)
