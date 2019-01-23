'''Application configuration file'''
import os
import datetime

POSTGRES_CONFIG = {
    'host':'localhost',
    'port':5432,
    'user':'postgres',
    'password': 'password1234',
    'database':'questioner'
}

class Config(object):
    """Parent configuration class"""
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(hours=1)

class DevelopmentConfig(Config):
    """Development environment configurations"""
    DEBUG = True
    POSTGRES_CONFIG = 'postgresql://%(user)s:%(password)s@%(host)s:\
    %(port)s/%(database)s' % POSTGRES_CONFIG

class TestingConfig(Config):
    """Testing environment configurations"""
    TESTING = True
    DEBUG = True
    POSTGRES_CONFIG = 'postgresql://%(user)s:%(password)s@%(host)s:\
    %(port)s/test_db' % POSTGRES_CONFIG

class StagingConfig(Config):
    """Staging environment configurations"""
    DEBUG = True

class ProductionConfig(Config):
    """Production environment configurations"""
    DEBUG = False
    TESTING = False

APP_CONFIG = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}