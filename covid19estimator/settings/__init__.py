import logging
try:
    #from covid19estimator.settings.development import *
    from covid19estimator.settings.production import *
except ImportError as error:
    logging.error(error)
