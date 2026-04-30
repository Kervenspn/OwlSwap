from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.String(36), primary_key=True)

    username = db.Column(db.String(80), unique=True, nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password_hash = db.Column(db.String(255), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"



#FUTURE FEATURE? LISTINGS
#add marketplace listings

# class Listing(db.Model):
#     __tablename__ = "listings"
#
#     id = db.Column(db.Integer, primary_key=True)
#
#     title = db.Column(db.String(150), nullable=False)
#
#     price = db.Column(db.Float, nullable=False)
#
#     description = db.Column(db.Text)
#
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#
#     user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
#
#     seller = db.relationship("User", backref="listings")