import os
from flask import Flask
from flask_bootstrap import Bootstrap4
from flask_login import LoginManager

login_manager = LoginManager()
bootstrap = Bootstrap4()
UPLOAD_FOLDER = 'app/static/images'
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__, static_folder='static')
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.secret_key = 'sEcrEtKeY'

    login_manager.init_app(app)
    login_manager.login_message = "Yêu cầu đăng nhập"
    login_manager.login_view = "auth.login"

    bootstrap.init_app(app)

    @app.template_filter('conv_curr')
    def conv_curr(amount):
        output = amount
        return "{:,}".format(int(output)) + 'đ'

    with app.app_context():
        from .admin import admin
        app.register_blueprint(admin, url_prefix='/admin')
        from .auth import auth
        app.register_blueprint(auth, url_prefix='/auth')
        from .main import main
        app.register_blueprint(main)

        return app