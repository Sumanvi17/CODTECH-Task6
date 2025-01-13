from flask import Blueprint, request, jsonify
from ..models import Product
from .. import db

product_bp = Blueprint('product', __name__)

@product_bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{
        "id": p.id, "title": p.title, "price": p.price, "image_url": p.image_url
    } for p in products])

@product_bp.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    product = Product(
        title=data['title'],
        description=data['description'],
        price=data['price'],
        category=data['category'],
        image_url=data['image_url'],
        seller_id=data['seller_id']
    )
    db.session.add(product)
    db.session.commit()
    return jsonify({"message": "Product added successfully"}), 201
