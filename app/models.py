from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Create both a Fiction AND a NonFiction model with the following attributes:
# id (Integer),
# title (String),
# author(String),
# year(Integer)

# Have both models inherit from db.Model as well as the Book class below. This Book class will be used to serialize
# our results back to the user who is requesting them


class Book:
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.brand,
            'author': self.name,
            'year': self.year
        }


# class Fiction here:
class Fiction(db.Model, Book):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(68), nullable=False)
    author = db.Column(db.String(96), nullable=False)
    year = db.Column(db.Integer)


# class NonFiction here:
class NonFiction(db.Model, Book):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(68), nullable=False)
    author = db.Column(db.String(96), nullable=False)
    year = db.Column(db.Integer)
