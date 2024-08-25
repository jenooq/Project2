from . import db
from datetime import datetime
import string
import random


def get_short():
    while True:
        short = ''.join(random.choices(string.ascii_letters + string.ascii_letters, k=6))
        if URLmodel.query.filter(URLmodel.short == short).first():
            continue
        return short


class URLmodel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(255), unique=True, nullable=True)
    short = db.Column(db.String(6), unique=True, nullable=True)
    visits = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
