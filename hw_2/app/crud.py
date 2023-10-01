import sqlite3
from typing import Union

from fastapi import HTTPException

from schemas import Book


DB_PATH = "../data/database.sqlite"


# Создание базы данных магазина
def create_db():

    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE book(id INTEGER PRIMARY KEY,
                                        title VARCHAR(50),
                                        author VARCHAR(20),
                                        description VARCHAR(500))""")


    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()


# Добавление книги в магазин
def add_book_into_db(book: Book):

    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    # Получаем последний ID
    cursor.execute('SELECT MAX(id) FROM book LIMIT 1')
    id_ = cursor.fetchall()[0][0]+1

    if book.id is None:
        book.id = id_
    else:
        if book.id > id_:
            raise HTTPException(status_code=404, detail="book id is too big, make it smaller")

    # Добавление новой книги
    cursor.execute('INSERT INTO book (id, title, author, description) VALUES (?, ?, ?, ?)',
                   (book.id, book.title, book.author, book.description))


    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()


# Просмотр информации о книге по ее идентификатору
def get_book_by_id(id: int) -> Union[Book, None]:

    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    # Получение данных книги
    cursor.execute('SELECT * FROM book WHERE id = ?',
                   (id,))
    result = cursor.fetchall()
    if result:
        book = Book(id=result[0][0],
                    title=result[0][1],
                    author=result[0][2],
                    description=result[0][3])
    else:
        book = None

    # Закрываем соединение
    connection.close()

    return book


# Обновление информации о книге по ее идентификатору
def update_book_by_id(book: Book):

    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    print('id book', book.id)
    # Обновление данных книги
    cursor.execute('UPDATE book SET title=?, author=?, description=? WHERE id=?',
                   (book.title, book.author, book.description, book.id))

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()


# Удаление книги по ее идентификатору
def delete_book_by_id(id: int):

    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    # Удаление книги
    cursor.execute('DELETE FROM book WHERE id=?',
                   (id,))

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()
