import tkinter as tk
from tkinter import messagebox

# Sample in-memory book list
books = []

# Add Book Function
def add_book():
    title = entry_title.get()
    author = entry_author.get()
    if title and author:
        books.append({"title": title, "author": author})
        messagebox.showinfo("Success", "Book added!")
        entry_title.delete(0, tk.END)
        entry_author.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill both fields.")

# View All Books
def view_books():
    output_text.delete("1.0", tk.END)
    for idx, book in enumerate(books, 1):
        output_text.insert(tk.END, f"{idx}. {book['title']} by {book['author']}\n")

# Search Book by Title
def search_book():
    title = entry_title.get().lower()
    output_text.delete("1.0", tk.END)
    found = False
    for book in books:
        if title in book['title'].lower():
            output_text.insert(tk.END, f"{book['title']} by {book['author']}\n")
            found = True
    if not found:
        output_text.insert(tk.END, "No book found.\n")

# Delete Book by Title
def delete_book():
    title = entry_title.get().lower()
    global books
    initial_len = len(books)
    books = [book for book in books if title not in book['title'].lower()]
    if len(books) < initial_len:
        messagebox.showinfo("Deleted", "Book deleted (if matched).")
    else:
        messagebox.showinfo("Not Found", "No matching book found.")
    output_text.delete("1.0", tk.END)

# GUI setup
root = tk.Tk()
root.title("Library Management System")

tk.Label(root, text="Book Title:").grid(row=0, column=0, padx=10, pady=5)
entry_title = tk.Entry(root, width=40)
entry_title.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Author:").grid(row=1, column=0, padx=10, pady=5)
entry_author = tk.Entry(root, width=40)
entry_author.grid(row=1, column=1, padx=10, pady=5)

# Buttons
tk.Button(root, text="Add Book", command=add_book).grid(row=2, column=0, pady=5)
tk.Button(root, text="View Books", command=view_books).grid(row=2, column=1, pady=5)
tk.Button(root, text="Search Book", command=search_book).grid(row=3, column=0, pady=5)
tk.Button(root, text="Delete Book", command=delete_book).grid(row=3, column=1, pady=5)

# Output box
output_text = tk.Text(root, height=10, width=60)
output_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
