import json
from . import db
import datetime
from flask_login import UserMixin
from passlib.hash import sha256_crypt

class Role(db.Model, UserMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    role_name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Role %r>' % self.role_name

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    fullname = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique = True, nullable=False)
    username = db.Column(db.String(100), unique = True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    api_key = db.Column(db.String(255), unique=True, nullable=True)
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    modified_at = db.Column(db.DateTime, nullable=True)

    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    role = db.relationship('Role', backref=db.backref('roles', lazy=True))

    def encode_api_key(self):
        self.api_key = sha256_crypt.hash(self.username + str(datetime.datetime.now))

    def __repr__(self):
        return '<User %r>' % (self.username)

    def to_json(self):
        user_dict = {
            'id': self.id,
            'fullname': self.fullname,
            'phone_number': self.phone_number,
            'email': self.email,
            'username': self.username,
            'password': self.password,
            'role_id': self.role_id,
            'api_key': self.api_key
        }
        return user_dict

class OTP(db.Model):
    __tablename__ = 'otp'
    id = db.Column(db.String(6), primary_key = True)
    expire_at = db.Column(db.DateTime, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('user_otp', lazy=True))

    def __repr__(self):
        return '<OTP %r>' % self.id

    def to_json(self):
        otp_dict = {
            'id': self.id,
            'expire_at': self.expire_at,
            'user_id': self.user_id,
        }
        return otp_dict

class Address(db.Model, UserMixin):
    __tablename__ = 'address'
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    city = db.Column(db.String(80), nullable=False)
    district = db.Column(db.String(80), nullable=False)
    ward = db.Column(db.String(80), nullable=False)
    road = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    modified_at = db.Column(db.DateTime, nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('user_address', lazy=True))

    def __repr__(self):
        return '<Address %r>' % self.id

    def to_json(self):
        address_dict = {
            'id': self.id,
            'city': self.city,
            'district': self.district,
            'ward': self.ward,
            'road': self.road,
            'user_id': self.user_id,
        }
        return address_dict