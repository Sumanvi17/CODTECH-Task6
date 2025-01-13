from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    
    # Register routes
    from .routes.auth_routes import auth_bp
    from .routes.product_routes import product_bp
    from .routes.review_routes import review_bp
    from .routes.search_routes import search_bp
    from .routes.seller_routes import seller_bp
    from .routes.cart_routes import cart_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(search_bp)
    app.register_blueprint(seller_bp)
    app.register_blueprint(cart_bp)
    
    return app
