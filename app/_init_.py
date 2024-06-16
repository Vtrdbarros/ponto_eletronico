print("Initializing app module")

from flask import Flask
from .models import init_db

def create_app():
    print("Creating Flask app")
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ponto_eletronico.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from .views import bp as main_bp
    app.register_blueprint(main_bp)

    init_db()

    return app
