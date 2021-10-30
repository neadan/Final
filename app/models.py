from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Create both a Fiction AND a NonFiction model with the following attributes:
# id (Integer),
# title (String),
# author(String),
# year(Integer)

# Have both models inherit from db.Model as well as the Book class below. This Book class will be used to serialize
# our results back to the user who is requesting them


class Book(db.Model):
    id = db.Column('author_id', db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(50))
    year = db.Column(db.String(10))
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.name,
            'year': self.year
        }

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

# class Fiction here:
class Fiction(db.Model):
    id = db.Column('author_id', db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(50))
    year = db.Column(db.String(10))
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
# class NonFiction here:
class NonFiction(db.Model):
    id = db.Column('author_id', db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(50))
    year = db.Column(db.String(10))
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year





