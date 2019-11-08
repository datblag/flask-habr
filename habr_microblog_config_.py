import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql://login:password@host/db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False