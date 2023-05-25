from flask_login import UserMixin
from ... import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(160), unique=True)
    password = db.Column(db.String(160))
    token = db.Column(db.String(160))
    refresh_token = db.Column(db.String(160))
    status = db.Column(db.Integer())
    access = db.Column(db.Integer())
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    about = db.Column(db.Text)
    created_at = db.Column(db.String(19))
    updated_at = db.Column(db.String(19))
    pages = db.relationship('Page', backref='created_by', passive_deletes=True)
    posts = db.relationship('Post', backref='created_by', passive_deletes=True)
    __table_args__ = {'extend_existing': True}