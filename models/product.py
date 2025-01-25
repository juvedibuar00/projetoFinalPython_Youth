# src/models/product.py


from database import db

class Product(db.Model):
    __tablename__ = 'product'

    idproduct = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    weight = db.Column(db.Float)
    brand = db.Column(db.String(100))
    expiration = db.Column(db.Date)

    comments = db.relationship('Comment', backref='product', lazy=True)
