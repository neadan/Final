from flask import Blueprint, request, Response, jsonify

import app
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
            fictions = Fiction.query.all()
        else:
            fictions = Fiction.query.filter(Fiction.author == query_params['author'])

        result = [fiction.to_dict() for fiction in fictions]
        return jsonify(result)

    ###### Create a new book in the database ######
    ###### Don't forget to return the full path of the resource in the location header ######
    if request.method == 'POST':
        data = request.form
        fiction_to_add = Fiction(id=data['id'], title=data['title'], author=data['author'], year=data['year'])
        db.session.add(fiction_to_add)
        db.session.commit()
        response = Response(status=200)
        response.headers['location'] = f"fiction/{fiction_to_add}"
        return response, "created fiction book successfully"


@book_bp.route("/fiction/<int:book_id>", methods=['GET', 'DELETE'])
def book_id_fiction(book_id):
    ###### Return the book with book_id ######
    ###### If no such book exists, return the appropriate response as we have seen in class ######
    if request.method == 'GET':
        fiction = Fiction.query.get(book_id)
        if fiction is None:
            return Response(status=404)
        return jsonify(fiction.to_dict())


    ###### Delete the book with no ######
    ###### If no such book exists, return the appropriate response as we have seen in class ######
    if request.method == 'DELETE':
        if request.method == 'DELETE':
            fiction = Fiction.query.get(book_id)
            if fiction is None:
                return Response(status=404)
            db.session.remove(fiction)
            db.session.commit()
            return Response(status=200)


@book_bp.route("/all", methods=['GET'])
def books():
    ###### Return all books (whether they are fiction or non-fiction ######
    if request.method == 'GET':
        fictions = Fiction.query.all()
        result = [fiction.to_dict() for fiction in fictions]
        non_fictions = NonFiction.query.all()
        result += [non_fiction.to_dict() for non_fiction in non_fictions]
        return jsonify(result)