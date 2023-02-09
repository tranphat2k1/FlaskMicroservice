import json
from . import db
import datetime

class Brand(db.Model):
    __tablename__ = 'brand'
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    modified_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return '<Brand %r>' % self.name

    def to_json(self):
        brand_dict = {
            'id': self.id,
            'name': self.name
        }
        return brand_dict

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Integer, default=0)
    stock = db.Column(db.Integer, nullable=False)
    desc = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    modified_at = db.Column(db.DateTime, nullable=True)

    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable=False)
    brand = db.relationship('Brand', backref=db.backref('brands', lazy=True))

    image = db.Column(db.String(150), nullable=False, default='image.jpg')

    def __repr__(self):
        return '<Product %r>' % self.name

    def to_json(self):
        product_dict = {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'discount': self.discount,
            'stock': self.stock,
            'desc': self.desc,
            'brand_id': self.brand_id,
            'image': self.image
        }
        return product_dict