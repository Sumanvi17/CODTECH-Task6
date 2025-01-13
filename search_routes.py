from flask import Blueprint, request, jsonify
from ..models import Product

search_bp = Blueprint('search', __name__)

@search_bp.route('/search', methods=['GET'])
def search_products():
    query = request.args.get('query', '')
    category = request.args.get('category', None)
    min_price = request.args.get('min_price', 0, type=float)
    max_price = request.args.get('max_price', float('inf'), type=float)
    
    products = Product.query.filter(
        Product.title.ilike(f"%{query}%"),
        Product.price >= min_price,
        Product.price <= max_price
    )
    if category:
        products = products.filter_by(category=category)
    products = products.all()
    return jsonify([{
        "id": p.id, "title": p.title, "price": p.price, "category": p.category
    } for p in products])
