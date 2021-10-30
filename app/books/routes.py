from flask import Blueprint, request, jsonify, Response

from app.models import Fiction, db, NonFiction, Book

book_bp = Blueprint('books', __name__, url_prefix='/api/v1/books')

###### Implement the following functions: ######


@book_bp.route("/fiction", methods=['GET', 'POST'])
def books_fiction():
    ###### Return all books that are Fiction ######
    if request.method == 'GET':
        fiction = Fiction.query.all()
        result = [fictions.to_dict() for fictions in fiction]
        return jsonify(result)

    ###### Accept the "author" query parameter, which returns all books that are written by that specific author ######
    elif request.method == 'GET':
        query_params = request.args
        fiction = Fiction.query.filter(Fiction.year == query_params['year'])
        result = [fictions.to_dict() for fictions in fiction]
        return jsonify(result)

    ###### Create a new book in the database ######
    ###### Don't forget to return the full path of the resource in the location header ######
    if request.method == 'POST':
        data = request.form
        book_to_add = Fiction(title=data['title'], author=data['author'], year=data['year'])
        db.session.add(book_to_add)
        db.session.commit()
        response = Response(status=200)
        response.headers['location'] = f"/fiction/{book_to_add.id}"
        return response


@book_bp.route("/fiction/<int:book_id>", methods=['GET', 'DELETE'])
def book_id_fiction(book_id):
    ###### Return the book with book_id ######
    ###### If no such book exists, return the appropriate response as we have seen in class ######
    if request.method == 'GET':
        book = Fiction.query.get(book_id)
        return jsonify(book.to_dict())
    ###### Delete the book with no ######
    ###### If no such book exists, return the appropriate response as we have seen in class ######
    if request.method == 'DELETE':
        fiction = Fiction.query.get(book_id)
        db.session.delete(fiction)
        db.session.commit()
        response = Response(status=200)
        return response


@book_bp.route("/all", methods=['GET'])
def books():
    ###### Return all books (whether they are fiction or non-fiction ######
    if request.method == 'GET':
        fiction = Fiction.query.all()
        nonfiction = NonFiction.query.all()
        allbooks = fiction + nonfiction
        result = [book.to_dict() for book in allbooks]
        return jsonify(result)