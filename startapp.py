import logging
import time
from flask import g, request
from covid19estimator import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
