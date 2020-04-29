from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Configuration
from flask_whooshee import Whooshee

db = SQLAlchemy()
whooshee = Whooshee()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Configuration)
    db.init_app(app)
    whooshee.init_app(app)

    from whocalledme.main.routes import main
    app.register_blueprint(main)
    return app