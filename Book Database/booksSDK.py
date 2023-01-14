import sqlite3
from book import Book

def cursor():
    return sqlite3.connect('books.db').cursor()

c = cursor()
c.execute('CREATE TABLE IF NOT EXISTS books (title TEXT, pages INTEGER)')
c.connection.close()

def add_book(book):
    c = cursor()

    with c.connection:
        c.execute('INSERT INTO books VALUES (?, ?)', (book.title, book.pages))
    c.connection.close()
    return c.lastrowid

def get_books():
    c = cursor()

    books = []
    for row in c.execute('SELECT * FROM books'):
        books.append(Book(row[0],row[1]))
    c.connection.close()
    return books

def search_book_title(title):
    c = cursor()

    with c.connection:
        c.execute('SELECT * FROM books WHERE title=?', (title,))
    data = c.fetchone()
    c.connection.close()
    if not data:
        return None

    return Book(data[0], data[1])

def update_book(book, newTitle, newPages):
    c = cursor()
    with c.connection:
        c.execute('UPDATE books SET title=?, pages=? WHERE title=? AND pages=?',(newTitle, newPages, book.title, book.pages))
    book = search_book_title(book.title)
    c.connection.close()
    return book

def delete_book(book):
    c = cursor()
    with c.connection:
        c.execute('DELETE FROM books WHERE title=? AND pages=?', (book.title, book.pages))
    rows = c.rowcount
    c.connection.close()
    return rows