from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'super secret key'
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost:3307/product_service"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    with app.app_context():
        from .product_api import product_api_blueprint
        app.register_blueprint(product_api_blueprint)
        return app