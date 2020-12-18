private_key_id = "62ea5fbc2a1ea76a558d51eaa9bb12990c932150"
#api_key = "YOUR_KEY"
#api_secret = "YOUR_SECRET"
#access_token = "YOUR_ACCESS_TOKEN"
#token_secret = "YOUR_TOKEN_SECRET"]

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'change'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
