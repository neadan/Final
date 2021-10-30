from flask import Blueprint, request,jsonify
from app.models import db,Book,Fiction,NonFiction
book_bp = Blueprint('books', __name__, url_prefix='/api/v1/books')

###### Implement the following functions: ######


@book_bp.route("/fiction", methods=['GET', 'POST'])
def books_fiction():
    ###### Return all books that are Fiction ######
    ###### Accept the "author" query parameter, which returns all books that are written by that specific author ######
    if request.method == 'GET':
        author = request.args.get('author')

        print(author)
        fictionData = []
        if(author):
            bookDetail = db.session.query(Book).filter(Book.author == author)
        else:
            bookDetail=Book.query.all()

        for x in bookDetail:
            fictionData.append({"id": x.id, "title": x.title, "author": x.author, "year": x.year})
        return jsonify(fictionData)



    ###### Create a new book in the database ######
    ###### Don't forget to return the full path of the resource in the location header ######
    if request.method == 'POST':
        if  not request.form['author'] or not request.form['title'] or not request.form[
            'year'] :

            return jsonify({"error": "Please enter all the fields"})
        else:
            bookData = Book(request.form['title'],request.form['author'],
                       request.form['year'])

            db.session.add(bookData)

            db.session.commit()
            response = jsonify()
            response.status_code = 200
            response.headers['location'] = '/fiction'
            response.autocorrect_location_header = False
            return response




@book_bp.route("/fiction/<int:book_id>", methods=['GET', 'DELETE'])
def book_id_fiction(book_id):
    ###### Return the book with book_id ######
    ###### If no such book exists, return the appropriate response as we have seen in class ######
    if request.method == 'GET':
        bookDetail = db.session.query(Book).filter(Book.id == book_id)
        res = []
        for x in bookDetail:
            res.append({"id": x.id, "title": x.title, "author": x.author, "year": x.year})
        if (len(res) > 0):
            return jsonify(res)
        else:
            return jsonify({"message": "Book Not Found!"}), 404


    ###### Delete the book with no ######
    ###### If no such book exists, return the appropriate response as we have seen in class ######
    if request.method == 'DELETE':
        deleteBook = db.session.query(Book).filter(Book.id == book_id).delete()
        print(deleteBook)
        db.session.commit()
        if (deleteBook):
            return jsonify({"message": "Book Record was successfully Deleted!"})
        else:
            return jsonify({"message": "Book Not Found!"}), 404


@book_bp.route("/all", methods=['GET'])
def books():
    ###### Return all books (whether they are fiction or non-fiction ######
    if request.method == 'GET':
        bookData = []
        for x in Book.query.all():
            bookData.append({"id": x.id, "title": x.title, "author": x.author, "year": x.year})
        return jsonify(bookData)
