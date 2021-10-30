from flask import Blueprint, request, jsonify, Response

from app.models import Fiction, db, NonFiction

book_bp = Blueprint('books', __name__, url_prefix='/api/v1/books')


###### Implement the following functions: ######

@book_bp.route("/fiction", methods=['GET', 'POST'])
def books_fiction():
    ###### Return all books that are Fiction ######
    ###### Accept the "author" query parameter, which returns all books that are written by that specific author ######
    if request.method == 'GET':
        query_param = request.args
        if not query_param:
            fiction_books = Fiction.query.all()
        else:
            fiction_books = Fiction.query.filter(Fiction.author == query_param['author'])
        result = [book.to_dict() for book in fiction_books]
        return jsonify(result)

    ###### Create a new book in the database ######
    ###### Don't forget to return the full path of the resource in the location header ######
    if request.method == 'POST':
        data = request.form
        add_book = Fiction(title=data['title'], author=data['author'], year=data['year'])
        db.session.add(add_book)
        db.session.commit()
        response = Response(status=200)
        response.headers['location'] = f"/api/v1/books/fiction/{add_book.id}"
        return response
        # return "implement this POST (fiction)"


@book_bp.route("/fiction/<int:book_id>", methods=['GET', 'DELETE'])
def book_id_fiction(book_id):
    ###### Return the book with book_id ######
    ###### If no such book exists, return the appropriate response as we have seen in class ######
    if request.method == 'GET':
        fiction_book = Fiction.query.get(book_id)
        if not fiction_book:
            return Response(status=404)
        else:
            return jsonify(fiction_book.to_dict())
        # return "implement this GET (book_id)"
    ###### Delete the book with no ######
    ###### If no such book exists, return the appropriate response as we have seen in class ######
    if request.method == 'DELETE':
        # return "implement this DELETE (book_id)"
        book_to_delete = Fiction.query.get(book_id)
        if not book_to_delete:
            return Response(status=404)
        else:
            db.session.delete(book_to_delete)
            db.session.commit()
            return Response(status=200)


@book_bp.route("/nonfiction", methods=['GET', 'POST'])
def books_nonfiction():
    if request.method == 'GET':
        query_param = request.args
        if not query_param:
            nonfiction_books = NonFiction.query.all()
        else:
            nonfiction_books = NonFiction.query.filter(NonFiction.author == query_param['author'])
        result = [book.to_dict() for book in nonfiction_books]
        return jsonify(result)

    if request.method == 'POST':
        data = request.form
        add_book = NonFiction(title=data['title'], author=data['author'], year=data['year'])
        db.session.add(add_book)
        db.session.commit()
        response = Response(status=200)
        response.headers['location'] = f"/api/v1/books/nonfiction/{add_book.id}"
        return response


@book_bp.route("/all", methods=['GET'])
def books():
    ###### Return all books (whether they are fiction or non-fiction ######
    if request.method == 'GET':
        fiction_list = Fiction.query.all()
        nonfiction_list = NonFiction.query.all()
        all_books = fiction_list+ nonfiction_list
        result = [book.to_dict() for book in all_books]
        return jsonify(result)
        #fiction_list.extend(nonfiction_list)         # doing with extend()
        #result = [book.to_dict() for book in fiction_list]
        #return jsonify(result)

        # return "implement this GET (all)"
