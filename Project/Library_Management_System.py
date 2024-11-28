import mysql.connector

# Connect to the MySQL database
def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="@Ishangupta1234",
        database="LibraryDB"
    )

# Add a new book
def add_book(title, author, genre, year_published):
    db = connect()
    cursor = db.cursor()
    sql = "INSERT INTO books (title, author, genre, year_published) VALUES (%s, %s, %s, %s)"
    val = (title, author, genre, year_published)
    cursor.execute(sql, val)
    db.commit()
    print(f"Book '{title}' added successfully!")
    db.close()

# View all books
def view_books():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM books")
    result = cursor.fetchall()
    for row in result:
        print(row)
    db.close()

# Search for a book by title or author
def search_books(keyword):
    db = connect()
    cursor = db.cursor()
    sql = "SELECT * FROM books WHERE title LIKE %s OR author LIKE %s"
    val = (f"%{keyword}%", f"%{keyword}%")
    cursor.execute(sql, val)
    result = cursor.fetchall()
    for row in result:
        print(row)
    db.close()

# Update book details
def update_book(book_id, title=None, author=None, genre=None, year_published=None):
    db = connect()
    cursor = db.cursor()
    sql = "UPDATE books SET title=%s, author=%s, genre=%s, year_published=%s WHERE book_id=%s"
    cursor.execute(sql, (title, author, genre, year_published, book_id))
    db.commit()
    print(f"Book ID {book_id} updated successfully!")
    db.close()

# Delete a book
def delete_book(book_id):
    db = connect()
    cursor = db.cursor()
    sql = "DELETE FROM books WHERE book_id=%s"
    val = (book_id,)
    cursor.execute(sql, val)
    db.commit()
    print(f"Book ID {book_id} deleted successfully!")
    db.close()

# Main menu
def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Books")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            genre = input("Enter genre: ")
            year_published = int(input("Enter year published: "))
            add_book(title, author, genre, year_published)

        elif choice == "2":
            view_books()

        elif choice == "3":
            keyword = input("Enter title or author to search: ")
            search_books(keyword)

        elif choice == "4":
            book_id = int(input("Enter book ID to update: "))
            title = input("Enter new title (leave blank to skip): ") or None
            author = input("Enter new author (leave blank to skip): ") or None
            genre = input("Enter new genre (leave blank to skip): ") or None
            year_published = input("Enter new year published (leave blank to skip): ")
            year_published = int(year_published) if year_published else None
            update_book(book_id, title, author, genre, year_published)

        elif choice == "5":
            book_id = int(input("Enter book ID to delete: "))
            delete_book(book_id)

        elif choice == "6":
            print("Exiting the Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

main()
