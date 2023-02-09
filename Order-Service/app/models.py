import json
from . import db
import datetime

class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    total = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    modified_at = db.Column(db.DateTime, nullable=True)

    user_id = db.Column(db.Integer, nullable=False)
    address_id = db.Column(db.Integer, nullable=False)
    items = db.relationship('OrderItem', backref='orderItem')

    def __repr__(self):
        return '<Order %r>' % self.id

    def to_json(self):
        order_dict = {
            'id': self.id,
            'total': self.total,
            'status': self.status,
            'user_id': self.user_id,
            'created_at': self.created_at,
            'address_id': self.address_id,
        }
        return order_dict

class OrderItem(db.Model):
    __tablename__ = 'orderitem'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    modified_at = db.Column(db.DateTime, nullable=True)

    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    order = db.relationship('Order', backref=db.backref('orders', lazy=True))
    product_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<OrderItem %r>' % self.id

    def to_json(self):
        oi_dict = {
            'id': self.id,
            'quantity': self.quantity,
            'order_id': self.order_id,
            'product_id': self.product_id,
        }
        return oi_dict
