# src/models/comment.py

from database import db
from datetime import datetime

class Comment(db.Model):
    __tablename__ = 'comment'

    idcomment = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.idperson'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.idproduct'), nullable=False)
    comment = db.Column(db.Text, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    date_time = db.Column(db.DateTime, default=datetime.utcnow)