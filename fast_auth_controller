from fastapi import FastAPI, HTTPException

app = FastAPI()

# Sample data - Replace this with your actual data or database interaction
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
    {"id": 3, "title": "Book 3", "author": "Author 3"},
]

# Route to list books
@app.get("/books")
def list_books():
    return books

# Route to get a specific book by ID
@app.get("/books/{book_id}")
def get_book(book_id: int):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return book
    else:
        raise HTTPException(status_code=404, detail="Book not found")

# Route to add a new book
@app.post("/books")
def add_book(book: dict):
    new_book = {
        "id": len(books) + 1,
        "title": book.get("title"),
        "author": book.get("author")
    }
    books.append(new_book)
    return new_book

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
