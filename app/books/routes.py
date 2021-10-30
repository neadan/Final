from flask import Blueprint, request, jsonify, Response

from app.models import Fiction, db, NonFiction

book_bp = Blueprint('books', __name__, url_prefix='/api/v1/books')

###### Implement the following functions: ######


@book_bp.route("/fiction", methods=['GET', 'POST'])
def books_fiction():
    ###### Return all books that are Fiction ######
    ###### Accept the "author" query parameter, which returns all books that are written by that specific author ######
    if request.method == 'GET':
        query_params = request.args
        if not query_params:
            fiction_books = Fiction.query.all()
        else:
            fiction_books = Fiction.query.filter(Fiction.author == query_params['author'])
        result = [book.to_dict() for book in fiction_books]
        return jsonify(fictionBooks = result)

    ###### Create a new book in the database ######
    ###### Don't forget to return the full path of the resource in the location header ######
    if request.method == 'POST':
        data = request.form
        new_book = Fiction(title= data['title'], author= data['author'], year= data['year'])
        db.session.add(new_book)
        db.session.commit()
        response = Response(status=200)
        response.headers['location'] = f"/api/v1/books/fiction/{new_book.id}"
        return response


@book_bp.route("/fiction/<int:book_id>", methods=['GET', 'DELETE'])
def book_id_fiction(book_id):
    ###### Return the book with book_id ######
    ###### If no such book exists, return the appropriate response as we have seen in class ######
    if request.method == 'GET':
        fiction_book = Fiction.query.get(book_id)
        if not fiction_book:
            return Response(status=404)
        else:
            return jsonify(fictionBook = fiction_book.to_dict())
    ###### Delete the book with no ######
    ###### If no such book exists, return the appropriate response as we have seen in class ######
    if request.method == 'DELETE':
        fiction_book = Fiction.query.get(book_id)
        if not fiction_book:
            return Response(status=404)
        else:
            db.session.delete(fiction_book)
            db.session.commit()
            return Response(status=200)


@book_bp.route("/all", methods=['GET'])
def books():
    ###### Return all books (whether they are fiction or non-fiction ######
    if request.method == 'GET':
        fiction_books = Fiction.query.all()
        non_fiction_books = NonFiction.query.all()
        result = []
        for fiction in fiction_books:
            result.append(fiction.to_dict())
        for nonfiction in non_fiction_books:
            result.append(nonfiction.to_dict())

        return jsonify(allbooks=result)