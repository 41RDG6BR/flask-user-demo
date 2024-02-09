# models/__init__.py
from .user_model import db

def init_app(app):
    with app.app_context():
        db.create_all()
