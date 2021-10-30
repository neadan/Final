from flask import Flask 

from app.books.routes import book_bp
from app.models import db


def create_app():
    app = Flask("BookStoreAPI")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookstore.db'
    app.register_blueprint(book_bp)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app