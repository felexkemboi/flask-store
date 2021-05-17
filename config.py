# class Config(object):
#     """
#     Common configurations
#     """
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     DEBUG = True
#     # Put any configurations here that are common across all environments
#
# class DevelopmentConfig(Config):
#     """
#     Development configurations
#     """
#
#     SQLALCHEMY_ECHO = True
#
# class ProductionConfig(Config):
#     """
#     Production configurations
#     """
#
#     DEBUG = False
#
# class TestingConfig(Config):
#     """
#     Testing configurations
#     """
#
#     TESTING = True
#
# app_config = {
#     'development': DevelopmentConfig,
#     'production': ProductionConfig,
#     'testing': TestingConfig
# }
#
#
# # config.py
# ENV = "development"
PORT = 5000
DEBUG = True

SECRET_KEY = 'secretkeyforsessions'

SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost/flask"
SQLALCHEMY_TRACK_MODIFICATIONS = False
