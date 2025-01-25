# src/repositories/comment_repository.py

from models.comment import Comment
from database import db

class CommentRepository:
    @staticmethod
    def create(data):
        comment = Comment(**data)
        db.session.add(comment)
        db.session.commit()
        return comment

    @staticmethod
    def get_by_product(product_id):
        return Comment.query.filter_by(product_id=product_id).all()

    @staticmethod
    def delete(comment_id):
        comment = Comment.query.get(comment_id)
        if comment:
            db.session.delete(comment)
            db.session.commit()
        return comment













