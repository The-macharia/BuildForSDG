from flask import Flask

def create_app(config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY = "dev"
    )

    from .api import api_bp
    app.register_blueprint(api_bp)

    return app