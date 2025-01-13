from flask import Blueprint, request, jsonify

cart_bp = Blueprint('cart', __name__)

shopping_cart = {}

@cart_bp.route('/cart/<int:user_id>', methods=['GET'])
def get_cart(user_id):
    cart = shopping_cart.get(user_id, [])
    return jsonify(cart)

@cart_bp.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    user_id = data['user_id']
    product_id = data['product_id']
    quantity = data.get('quantity', 1)
    
    if user_id not in shopping_cart:
        shopping_cart[user_id] = []
    shopping_cart[user_id].append({"product_id": product_id, "quantity": quantity})
    return jsonify({"message": "Product added to cart"}), 201
