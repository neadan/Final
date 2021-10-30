from flask import Blueprint, request, jsonify, Response

from app.models import Book, db, Fiction, NonFiction

book_bp = Blueprint('books', __name__, url_prefix='/api/v1/books')


###### Implement the following functions: ######


@book_bp.route("fiction", methods=['GET', 'POST'])
def books_fiction():
    ###### Return all books that are Fiction ######
    ###### Accept the "author" query parameter, which returns all books that are written by that specific author ######
    if request.method == 'GET':
        query_params = request.args
        if not query_params:
            b_fictions = Fiction.query.all()
        else:
            b_fictions = Fiction.query.filter((Fiction.author == query_params['author']) and (Fiction.genre == "Fiction"))
        results = [b_fiction.to_dict() for b_fiction in b_fictions]
        if len(results)==0:
            return "No Books in DB"
        return jsonify(results)

    ###### Create a new book in the database ######
    ###### Don't forget to return the full path of the resource in the location header ######
    if request.method == 'POST':
        data = request.form
        b_add = Fiction(title=data['title'], author=data['author'], year=data['year'], genre="Fiction")
        db.session.add(b_add)
        db.session.commit()
        response = Response(status=200)
        response.headers['location'] = f"books/{b_add.id}"
        return response


@book_bp.route("/nonfiction", methods=['GET', 'POST'])
def books_non_fiction():
    ###### Return all books that are Fiction ######
    ###### Accept the "author" query parameter, which returns all books that are written by that specific author ######
    if request.method == 'GET':
        query_params = request.args
        if not query_params:
            b_non_fictions = NonFiction.query.all()
        else:
            b_non_fictions = NonFiction.query.filter((NonFiction.author == query_params['author']) and (NonFiction.genre == "NonFiction"))
        results = [b_nonfiction.to_dict() for b_nonfiction in b_non_fictions]
        if len(results) == 0:
            return "No Books in DB"
        return jsonify(results)

    ###### Create a new book in the database ######
    ###### Don't forget to return the full path of the resource in the location header ######
    if request.method == 'POST':
        data = request.form
        b_add = NonFiction(title=data['title'], author=data['author'], year=data['year'], genre="NonFiction")
        db.session.add(b_add)
        db.session.commit()
        response = Response(status=200)
        response.headers['location'] = f"books/{b_add.id}"
        return response

@book_bp.route("/fiction/<int:book_id>", methods=['GET', 'DELETE'])

def book_id_fiction(book_id):
    ###### Return the book with book_id ######
    ###### If no such book exists, return the appropriate response as we have seen in class ######
    if request.method == 'GET':
        book = Fiction.query.get(book_id)
        if book is None:
            return Response(status=404)
        return jsonify(book.to_dict())
    ###### Delete the book with no ######
    ###### If no such book exists, return the appropriate response as we have seen in class ######
    if request.method == 'DELETE':
        book = Fiction.query.get(book_id)
        if book is None:
            return Response(status=404)
        db.session.delete(book)
        db.session.commit()
        return Response(status=200)

@book_bp.route("/nonfiction/<int:book_id>", methods=['GET', 'DELETE'])
def book_id_nonfiction(book_id):
    ###### Return the book with book_id ######
    ###### If no such book exists, return the appropriate response as we have seen in class ######
    if request.method == 'GET':
        book = NonFiction.query.get(book_id)
        if book is None:
            return Response(status=404)
        return jsonify(book.to_dict())
    ###### Delete the book with no ######
    ###### If no such book exists, return the appropriate response as we have seen in class ######
    if request.method == 'DELETE':
        book = NonFiction.query.get(book_id)
        if book is None:
            return Response(status=404)
        db.session.delete(book)
        db.session.commit()
        return Response(status=200)

@book_bp.route("/all", methods=['GET'])
def books():
    ###### Return all books (whether they are fiction or non-fiction ######
    if request.method == 'GET':
        fiction = Fiction.query.all()
        b_non_fictions = NonFiction.query.all()

        if books is None:
            return Response(status=404)

        results_f = [book.to_dict() for book in fiction]
        results_nf = [book.to_dict() for book in b_non_fictions]
        results = results_f+results_nf
        if len(results) == 0:
            return "No Books in DB"
        return jsonify(results)
