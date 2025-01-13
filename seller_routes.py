from flask import Blueprint, jsonify
from ..models import Product, User

seller_bp = Blueprint('seller', __name__)

@seller_bp.route('/store/<int:seller_id>', methods=['GET'])
def get_seller_storefront(seller_id):
    seller = User.query.get(seller_id)
    if not seller or not seller.is_seller:
        return jsonify({"message": "Seller not found"}), 404
    
    products = Product.query.filter_by(seller_id=seller_id).all()
    return jsonify({
        "seller": {"id": seller.id, "username": seller.username},
        "products": [{"id": p.id, "title": p.title, "price": p.price} for p in products]
    })
