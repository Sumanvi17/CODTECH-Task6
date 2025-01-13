from flask import Blueprint, request, jsonify
from ..models import Review
from .. import db

review_bp = Blueprint('review', __name__)

@review_bp.route('/reviews/<int:product_id>', methods=['GET'])
def get_reviews(product_id):
    reviews = Review.query.filter_by(product_id=product_id).all()
    return jsonify([{
        "id": r.id, "user_id": r.user_id, "rating": r.rating, "comment": r.comment
    } for r in reviews])

@review_bp.route('/reviews', methods=['POST'])
def add_review():
    data = request.get_json()
    review = Review(
        product_id=data['product_id'],
        user_id=data['user_id'],
        rating=data['rating'],
        comment=data['comment']
    )
    db.session.add(review)
    db.session.commit()
    return jsonify({"message": "Review added successfully"}), 201
