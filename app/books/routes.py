from flask import Blueprint, request, Response, jsonify

from app.models import db

book_bp = Blueprint('books', __name__, url_prefix='/api/v1/books')

###### Implement the following functions: ######


@book_bp.route("/fiction", methods=['GET', 'POST'])
def books_fiction():

    if request.method == 'GET':
        return "implement this GET (fiction)"
    if request.method == 'POST':
        data = request.form
        books_fiction_to_add =books_fiction(title=data['title'], author=data['author'], year=data['year'])
        db.session.add(books_fiction_to_add)
        db.session.commit()
        response = Response
        response.headers['location'] = f"books/{books_fiction}"
        return response


    if request.method == 'POST':
        return "implement this POST (fiction)"


@book_bp.route("/fiction/<int:book_id>", methods=['GET', 'DELETE'])
def book_id_fiction(book_id, book_id_fiction_dict=None):

    if request.method == 'GET':
        return "implement this GET (book_id)"
    if request.method == 'GET':
        return jsonify(book_id_fiction[book_id_fiction])
    if request.method == 'DELETE':
        del(book_id_fiction_dict[book_id])
        return Response

    if request.method == 'DELETE':
        return "implement this DELETE (book_id)"

    if request.method == 'DELETE':
        del(book_id_fiction_dict[book_id])
        return Response



@book_bp.route("/all", methods=['GET'])
def books():
    ###### Return all books (whether they are fiction or non-fiction ######
    if request.method == 'GET':
        return "implement this GET (all)"
    if request.method == 'GET':
        return jsonify(books)

