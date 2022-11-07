from flask import render_template, request, redirect
from app import app
from models.book_list import *
from models.book import Book

@app.route('/library')
def index():
    return render_template('index.html', title='Home', library=library)

@app.route('/books/<book>')
def single_book(book):
    selected_book = library[int(book)]
    return render_template('individual_book.html', title='book', book=selected_book)

@app.route('/library', methods=['POST'])
def add_book():
  title = request.form['title']
  author = request.form['author']
  genre = request.form['genre']
  isbn = request.form['isbn']
  location = request.form['location']
  checked_out = False
  new_book = Book(isbn=isbn, title=title, author=author, genre=genre, location=location, checked_out=checked_out)
  add_new_book(new_book)
  return redirect('/library')

@app.route('/library/delete/<book>', methods=['POST'])
def delete(book):
  delete_book(book)
  return redirect('/library')