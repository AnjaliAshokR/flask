from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prof/<username>')
def prof(username):
    return render_template('new.html', username=username)

@app.route('/books')
def books():
    books=[{'book':'Harry Potter Series', 'author':'J.K Rowling', 'cover':'https://m.media-amazon.com/images/I/71-++hbbERL._SY679_.jpg'},
           {'book':'Twilight', 'author':'Stephanie Meyer', 'cover':'https://images-na.ssl-images-amazon.com/images/I/41L5QuedEaL._SX323_BO1,204,203,200_.jpg'},
           {'book':'Notebook', 'author':'Nicholas Sparks', 'cover': 'https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1483183484l/33648131._SY475_.jpg'}]
    return render_template('books.html', books=books)

app.run(debug=True)