from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Configuration

db = SQLAlchemy()

def create_app(config_class=Configuration):
    app = Flask(__name__)
    app.config.from_object(Configuration)
    db.init_app(app)

    from whocalledme.main.routes import main
    app.register_blueprint(main)
    return app