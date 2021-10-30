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
            'title': self.title,         # thats sneaky way of putting a error glad i learned how to interpret errors
            'author': self.author,
            'year': self.year
        }


# class Fiction here:
class Fiction(db.Model, Book):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(10), nullable=False)
    author = db.Column(db.String(15), nullable=False)
    year = db.Column(db.Integer)


# class NonFiction here:
class NonFiction(db.Model, Book):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(10), nullable=False)
    author = db.Column(db.String(15), nullable=False)
    year = db.Column(db.Integer)
