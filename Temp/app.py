from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection
def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",     # replace with your MySQL username
        password="@Ishangupta1234", # replace with your MySQL password
        database="LibraryDB"
    )

# Route to view all books
@app.route("/books", methods=["GET"])
def get_books():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM books")
    result = cursor.fetchall()
    db.close()
    
    books = [{"id": row[0], "title": row[1], "author": row[2], "genre": row[3], "year_published": row[4]} for row in result]
    return jsonify(books)

# Route to add a new book
@app.route("/books", methods=["POST"])
def add_book():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    year_published = request.form["year"]
    
    db = connect()
    cursor = db.cursor()
    cursor.execute("INSERT INTO books (title, author, genre, year_published) VALUES (%s, %s, %s, %s)", 
                   (title, author, genre, year_published))
    db.commit()
    db.close()
    
    return jsonify({"message": "Book added successfully!"})

# Route to delete a book
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    db = connect()
    cursor = db.cursor()
    cursor.execute("DELETE FROM books WHERE book_id = %s", (book_id,))
    db.commit()
    db.close()
    
    return jsonify({"message": "Book deleted successfully!"})

# Route to update a book
@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    title = request.form.get("title")
    author = request.form.get("author")
    genre = request.form.get("genre")
    year_published = request.form.get("year")
    
    db = connect()
    cursor = db.cursor()
    cursor.execute("""
        UPDATE books
        SET title = %s, author = %s, genre = %s, year_published = %s
        WHERE book_id = %s
    """, (title, author, genre, year_published, book_id))
    db.commit()
    db.close()

    return jsonify({"message": "Book updated successfully!"})

# Route to search books
@app.route("/books/search", methods=["GET"])
def search_books():
    query = request.args.get("query")
    db = connect()
    cursor = db.cursor()
    cursor.execute("""
        SELECT * FROM books 
        WHERE title LIKE %s OR author LIKE %s
    """, (f"%{query}%", f"%{query}%"))
    result = cursor.fetchall()
    db.close()

    books = [{"id": row[0], "title": row[1], "author": row[2], "genre": row[3], "year_published": row[4]} for row in result]
    return jsonify(books)

if __name__ == "__main__":
    app.run(debug=True)
