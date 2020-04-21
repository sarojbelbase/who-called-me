from flask import current_app, Flask
from whocalledme import db

class Company(db.Model):
    __tablename__ = 'company'
    company_id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(20), unique=True)
    posts = db.relationship('Extension', backref='carrier', lazy=True)

    def __repr__(self):
        return f"Company{self.company_id}: [{self.company_name}]"


class Extension(db.Model):
    __tablename__ = 'extension'
    id = db.Column(db.Integer, primary_key=True)
    extension_id = db.Column(db.Integer, db.ForeignKey('company.company_id'), nullable=False)
    extension_number = db.Column(db.String(10), unique=True)
    extension_type = db.Column(db.String(10), unique=True)
    extension_name = db.Column(db.String(30))
    
    def __repr__(self):
        return f"Extension{self.id}: [{self.extension_name}, {self.extension_number}, {self.extension_type}, {self.extension_id}]"