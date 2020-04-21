import os

driver = 'sqlite:///'
basedir = os.path.abspath(os.path.dirname(__file__))
database = os.path.join(basedir, 'site.db')

class Configuration:

    SECRET_KEY = '8JNFRER23F38ERF23JERPOPERJER843B7352W'
    SQLALCHEMY_DATABASE_URI = driver + database
    SQLALCHEMY_TRACK_MODIFICATIONS = False