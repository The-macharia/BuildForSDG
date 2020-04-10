from flask import Blueprint

main_bp = Blueprint('main', __name__)

from covid19estimator.main import routes