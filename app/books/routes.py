from flask import Blueprint, request, Response, jsonify

from app.models import Fiction, db, NonFiction

book_bp = Blueprint('books', __name__, url_prefix='/api/v1/books')

###### Implement the following functions: ######


@book_bp.route("/fiction", methods=['GET', 'POST'])
def books_fiction():
    ###### Return all books that are Fiction ######
    ###### Accept the "author" query parameter, which returns all books that are written by that specific author ######
    if request.method == 'GET':
        kwargs=request.args
        if not kwargs:
            books = Fiction.query.all()
        else :
            # books=Fiction.query.filter(Fiction.author == kwargs['author'])
            books = Fiction.query.filter_by(**kwargs)
        list_of_books=[book.to_dict() for book in books]
        return jsonify(fiction_books=list_of_books)
        # return "implement this GET (fiction)"

    ###### Create a new book in the database ######
    ###### Don't forget to return the full path of the resource in the location header ######
    if request.method == 'POST':
        book = request.form
        book_to_add=Fiction(title=book['title'],author=book['author'],year=book['year'])
        db.session.add(book_to_add)
        db.session.commit()
        response=Response(status=200)
        response.headers['location']=f'/api/v1/books/fiction/{book_to_add.id}'
        return response


@book_bp.route("/fiction/<int:book_id>", methods=['GET', 'DELETE'])
def book_id_fiction(book_id):
    ###### Return the book with book_id ######
    ###### If no such book exists, return the appropriate response as we have seen in class ######
    if request.method == 'GET':
        book =  Fiction.query.get(book_id)
        if not book :
            return Response(status=404)
        return jsonify(fiction_book=book.to_dict())
    ###### Delete the book with no ######
    ###### If no such book exists, return the appropriate response as we have seen in class ######
    if request.method == 'DELETE':
        to_be_deleted=Fiction.query.get(book_id)
        if not to_be_deleted :
            return Response(status=404)
        db.session.delete(to_be_deleted)
        db.session.commit()
        return Response(status=200)



# testing non fiction
#
# @book_bp.route("/nonfiction", methods=['GET', 'POST'])
# def books_nonfiction():
#
#     if request.method == 'GET':
#         kwargs=request.args
#         if not kwargs:
#             books = NonFiction.query.all()
#         else :
#             books = NonFiction.query.filter_by(**kwargs)
#         list_of_books=[book.to_dict() for book in books]
#         return jsonify(nonfiction_books=list_of_books)
#
#     if request.method == 'POST':
#         book = request.form
#         book_to_add=NonFiction(title=book['title'],author=book['author'],year=book['year'])
#         db.session.add(book_to_add)
#         db.session.commit()
#         response=Response(status=200)
#         response.headers['location']=f'/api/v1/books/nonfiction/{book_to_add.id}'
#         return response



@book_bp.route("/all", methods=['GET'])
def books():
    ###### Return all books (whether they are fiction or non-fiction ######
    if request.method == 'GET':
        ficbooks=Fiction.query.all()
        nonficbooks = NonFiction.query.all()
        list_of_ficbooks = [book.to_dict() for book in ficbooks]
        list_of_nonficbooks = [book.to_dict() for book in nonficbooks]
        all=[]
        all.extend(list_of_ficbooks)
        all.extend(list_of_nonficbooks)
        return jsonify(all_books=all)
        # return "implement this GET (all)"