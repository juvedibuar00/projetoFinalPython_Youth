# src/models/person.py

from database import db

class Person(db.Model):
    __tablename__ = 'person'

    idperson = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(255))
    birthday = db.Column(db.Date)
    typeuser = db.Column(db.String(50), nullable=False)
    rg = db.Column(db.String(20))
    cpf = db.Column(db.String(11), unique=True)

    comments = db.relationship('Comment', backref='person', lazy=True)