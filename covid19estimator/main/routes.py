import json
from flask import render_template
from covid19estimator.main import main_bp

@main_bp.route('/', methods=('GET',))
def main():
    return render_template('main/index.html')
