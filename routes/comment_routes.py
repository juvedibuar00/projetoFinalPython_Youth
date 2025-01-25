# src/routes/comment_routes


# src/routes/comment_routes.py
from flask import Blueprint, request, jsonify
from models.comment import Comment
from database import db

comment_bp = Blueprint("comment", __name__)

@comment_bp.route("/", methods=["POST"])
def create_comment():
    data = request.get_json()
    new_comment = Comment(**data)
    db.session.add(new_comment)
    db.session.commit()
    return jsonify({"message": "Comment created successfully"}), 201

@comment_bp.route("/<int:idcomment>", methods=["GET"])
def get_comment(idcomment):
    comment = Comment.query.get_or_404(idcomment)
    return jsonify({"idcomment": comment.idcomment, "comment": comment.comment, "score": comment.score}), 200

@comment_bp.route("/<int:idcomment>", methods=["PUT"])
def update_comment(idcomment):
    data = request.get_json()
    comment = Comment.query.get_or_404(idcomment)
    for key, value in data.items():
        setattr(comment, key, value)
    db.session.commit()
    return jsonify({"message": "Comment updated successfully"}), 200

@comment_bp.route("/<int:idcomment>", methods=["DELETE"])
def delete_comment(idcomment):
    comment = Comment.query.get_or_404(idcomment)
    db.session.delete(comment)
    db.session.commit()
    return jsonify({"message": "Comment deleted successfully"}), 200