import os

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = False

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {
        'default':{
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s\n',
        },
        'request': {
            'format': '[%(asctime)s]\n',
        }
    },
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'estimator.logs'),
        }
    },
})