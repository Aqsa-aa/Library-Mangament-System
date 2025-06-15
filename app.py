from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
books = [
    {"id": 1, "title": "Python Basics", "author": "John"},
    {"id": 2, "title": "Flask in Action", "author": "Jane"}
]

# 1. Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# 2. Get a single book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    return jsonify(book) if book else ('Not Found', 404)

# 3. Add a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = {"id": len(books) + 1, "title": data['title'], "author": data['author']}
    books.append(new_book)
    return jsonify(new_book), 201

# 4. Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b["id"] != book_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
