import os

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = False

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {
        'default':{
            'format': '[%(asctime)s] - %(name)s - %(levelname)s %(funcName)s:%(lineno)d - %(message)s\n',
        },
    },
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'estimator.logs'),
        }
    },
    'root': {
        'handlers': ['wsgi']
    },
    'loggers': {
        'werkzeug':{
            'propagate': False
        },
        'covid19estimator': {
            'level': 'INFO',
            'handlers': ['file']
        }
    }
})
LOG_ROUTES = [
    "/api/v1/on-covid19",
    "/api/v1/on-covid19/json",
    "/api/v1/on-covid19/xml"
]