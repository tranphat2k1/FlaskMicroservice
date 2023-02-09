import json
from . import db
import datetime

class ShoppingCart(db.Model):
    __tablename__ = 'shoppingcart'
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    modified_at = db.Column(db.DateTime, nullable=True)

    user_id = db.Column(db.Integer, nullable=False)
    items = db.relationship('CartItem', backref='cartItem')

    def __repr__(self):
        return '<ShoppingCart %r>' % self.id

    def to_json(self):
        spc_dict = {
            'id': self.id,
            'quantity': self.quantity,
            'user_id': self.user_id
        }
        return spc_dict

class CartItem(db.Model):
    __tablename__ = 'cartitem'
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    modified_at = db.Column(db.DateTime, nullable=True)

    product_id = db.Column(db.Integer, nullable=False)
    shoppingcart_id = db.Column(db.Integer, db.ForeignKey('shoppingcart.id'), nullable=False)
    shoppingcart = db.relationship('ShoppingCart', backref=db.backref('shoppingcarts', lazy=True))

    def __repr__(self):
        return '<CartItem %r>' % self.id

    def to_json(self):
        ci_dict = {
            'id': self.id,
            'quantity': self.quantity,
            'product_id': self.product_id,
            'shoppingcart_id': self.shoppingcart_id
        }
        return ci_dict