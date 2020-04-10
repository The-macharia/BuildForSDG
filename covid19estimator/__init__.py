from flask import Flask

def create_app(config='covid19estimator.settings'):
    app = Flask(__name__)
    app.config.from_object(config)

    #Registering views for the app
    from .api import api_bp
    app.register_blueprint(api_bp)

    from .main import main_bp
    app.register_blueprint(main_bp)

    return app