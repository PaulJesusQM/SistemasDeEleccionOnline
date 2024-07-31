from flask import Flask
from controllers.usuario_controller import usuario_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.register_blueprint(usuario_bp, url_prefix='/api')
    return app
