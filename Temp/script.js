// Handle adding books
document.getElementById('addBookForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    let title = document.getElementById('title').value;
    let author = document.getElementById('author').value;
    let genre = document.getElementById('genre').value;
    let year = document.getElementById('year').value;

    fetch('/books', {
        method: 'POST',
        body: new URLSearchParams({
            'title': title,
            'author': author,
            'genre': genre,
            'year': year
        }),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message); // Show success message
        loadBooks(); // Reload the books list
    });
});

// Load books dynamically
function loadBooks() {
    fetch('/books')
        .then(response => response.json())
        .then(books => {
            let bookList = document.getElementById('bookList');
            bookList.innerHTML = '';
            books.forEach(book => {
                let bookItem = document.createElement('div');
                bookItem.classList.add('book-item');
                bookItem.innerHTML = `
                    <strong>Title:</strong> ${book.title}<br>
                    <strong>Author:</strong> ${book.author}<br>
                    <strong>Genre:</strong> ${book.genre}<br>
                    <strong>Year Published:</strong> ${book.year_published}
                    <button onclick="deleteBook(${book.id})">Delete</button>
                    <button onclick="editBook(${book.id})">Edit</button>
                `;
                bookList.appendChild(bookItem);
            });
        });
}

// Delete book
function deleteBook(bookId) {
    fetch(`/books/${bookId}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        loadBooks();
    });
}

// Edit book (similar to update form)
function editBook(bookId) {
    // Add logic to populate form and call updateBook
}

// Search books
function searchBooks() {
    let searchValue = document.getElementById('search').value;
    fetch(`/books/search?query=${searchValue}`)
        .then(response => response.json())
        .then(books => {
            let bookList = document.getElementById('bookList');
            bookList.innerHTML = '';
            books.forEach(book => {
                let bookItem = document.createElement('div');
                bookItem.classList.add('book-item');
                bookItem.innerHTML = `
                    <strong>Title:</strong> ${book.title}<br>
                    <strong>Author:</strong> ${book.author}<br>
                    <strong>Genre:</strong> ${book.genre}<br>
                    <strong>Year Published:</strong> ${book.year_published}
                `;
                bookList.appendChild(bookItem);
            });
        });
}

// Toggle dark mode
document.getElementById('darkModeToggle').addEventListener('click', function() {
    document.body.classList.toggle('dark-mode');
});

// Load books when the page loads
window.onload = loadBooks;
