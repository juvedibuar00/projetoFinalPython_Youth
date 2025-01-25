# src/repositories/product_repository.py

from models.product import Product
from database import db

class ProductRepository:
    @staticmethod
    def create(data):
        product = Product(**data)
        db.session.add(product)
        db.session.commit()
        return product

    @staticmethod
    def get_all():
        return Product.query.all()

    @staticmethod
    def get_by_id(product_id):
        return Product.query.get(product_id)

    @staticmethod
    def update(product_id, data):
        product = Product.query.get(product_id)
        if product:
            for key, value in data.items():
                setattr(product, key, value)
            db.session.commit()
        return product

    @staticmethod
    def delete(product_id):
        product = Product.query.get(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()
        return product
