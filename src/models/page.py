from ... import db
from ..models.user import User


class Page(db.Model):
    id = db.Column(db.String, primary_key=True, unique=True)
    title = db.Column(db.String(160))
    url_title = db.Column(db.String(160), unique=True)
    content = db.Column(db.Text)
    tags = db.Column(db.String(160))
    created_by = db.Column(db.Integer, db.ForeignKey(
        'user.id', ondelete='CASCADE'), nullable=False)
    created_at = db.Column(db.String(19))
    updated_at = db.Column(db.String(19))
    __table_args__ = {'extend_existing': True}
