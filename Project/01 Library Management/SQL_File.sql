CREATE DATABASE LibraryDB;

USE LibraryDB;

 
CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    genre VARCHAR(100),
    year_published INT
);


def update_book(book_id, title=None, author=None, genre=None, year_published=None):
    # Allows changing specific book details
    # Updates only the information you want to change