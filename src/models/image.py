from .. import db


class Image(db.Model):
    id = db.Column(db.String, primary_key=True, unique=True)
    title = db.Column(db.String(160))
    filename = db.Column(db.String(160), unique=True)
    description = db.Column(db.String(512))
    visible = db.Column(db.Integer(1))
    updated_by = db.Column(db.Integer, db.ForeignKey(
        'user.id', ondelete='CASCADE'), nullable=False)
    created_at = db.Column(db.String(19))
    updated_at = db.Column(db.String(19))
    __table_args__ = {'extend_existing': True}
