import json
from flask import Blueprint

api_bp = Blueprint("api", __name__, url_prefix="/api")

from covid19estimator.api import routes