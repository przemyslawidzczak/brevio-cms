from .. import db


class Settings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    value = db.Column(db.String(64))
    updated_by = db.Column(db.Integer, db.ForeignKey(
        'user.id', ondelete='CASCADE'), nullable=False)
    updated_at = db.Column(db.String(16))
    __table_args__ = {'extend_existing': True}
