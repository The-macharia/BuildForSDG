import os

from .base import *

ENV = 'production'
DEBUG = False
SECRET_KEY = os.getenv('SECRET_KEY')