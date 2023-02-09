import json
from sqlalchemy import desc
from . import order_api_blueprint
from .. import db
from ..models import Order, OrderItem
from .api.UserClient import UserClient
from .api.ProductClient import ProductClient
from flask import make_response, request, jsonify
import datetime

@order_api_blueprint.route('/api/user/orders', methods=['GET'])
def get_orders():
    api_key = request.headers.get('Authorization')
    response = UserClient.get_user(api_key)

    if not response:
        return make_response(jsonify({'message': 'Not logged in'}), 401)

    user = response['result']
    u_id = user['id']

    data = []
    orders = Order.query.filter_by(user_id=u_id).order_by(desc(Order.created_at)).all()
    for order in orders:
        address = UserClient.get_address_byID(order.address_id)
        d = {
            'id': order.id,
            'total': order.total,
            'status': order.status,
            'created_at': order.created_at,
            'user_id': order.user_id,
            'address': {
                'city': address['city'],
                'district': address['district'],
                'ward': address['ward'],
                'road': address['road']
            }
        }
        data.append(d)
    response = jsonify(data)
    return response

@order_api_blueprint.route('/api/order/add', methods=['POST'])
def add_order():
    api_key = request.headers.get('Authorization')
    response = UserClient.get_user(api_key)

    if not response:
        return make_response(jsonify({'message': 'Not logged in'}), 401)

    user = response['result']
    u_id = user['id']
    address_id = int(request.form['address_id'])
    total = request.form['total']

    order = Order()
    order.user_id = u_id
    order.total = total
    order.status = 'Đang chờ xác nhận'
    order.address_id = address_id

    db.session.add(order)
    db.session.commit()

    response = jsonify(order.to_json())
    return response

@order_api_blueprint.route('/api/order/add_order_item', methods=['POST'])
def add_order_item():
    api_key = request.headers.get('Authorization')
    response = UserClient.get_user(api_key)

    if not response:
        return make_response(jsonify({'message': 'Not logged in'}), 401)

    order_id = int(request.form['order_id'])
    product_id = int(request.form['product_id'])
    quantity = int(request.form['quantity'])

    order_item = OrderItem()
    order_item.order_id = order_id
    order_item.product_id = product_id
    order_item.quantity = quantity

    db.session.add(order_item)
    db.session.commit()

    ProductClient.update_product_quantity(product_id, quantity)

    response = jsonify(order_item.to_json())
    return response

@order_api_blueprint.route('/api/order/<int:order_id>/get_order_items', methods=['GET'])
def get_order_items(order_id):
    api_key = request.headers.get('Authorization')
    response = UserClient.get_user(api_key)

    if not response:
        return make_response(jsonify({'message': 'Not logged in'}), 401)

    data = []
    order_items = OrderItem.query.filter_by(order_id=order_id).all()
    for item in order_items:
        p = ProductClient.get_product(item.product_id)
        d = {
            'item_id': item.id,
            'name': p['name'],
            'price': p['price'],
            'discount': p['discount'],
            'final_price': int((p['price'] - p['price'] * p['discount']/100) * item.quantity),
            'quantity': item.quantity
        }
        data.append(d)
    response = jsonify(data)
    return response

@order_api_blueprint.route('/api/orders/get_orders_by_status', methods=['GET'])
def get_order_by_status():
    api_key = request.headers.get('Authorization')
    response = UserClient.get_user(api_key)

    if not response:
        return make_response(jsonify({'message': 'Not logged in'}), 401)

    status = request.form['status']
    data = []

    orders = Order.query.filter_by(status=status).order_by(desc(Order.created_at)).all()
    for order in orders:
        address = UserClient.get_address_byID(order.address_id)
        user = UserClient.get_user_by_id(order.user_id)
        d = {
            'id': order.id,
            'total': order.total,
            'status': order.status,
            'created_at': order.created_at,
            'user_id': order.user_id,
            'fullname': user['fullname'],
            'address': {
                'city': address['city'],
                'district': address['district'],
                'ward': address['ward'],
                'road': address['road']
            }
        }
        data.append(d)
    response = jsonify(data)
    return response

@order_api_blueprint.route('/api/order/update_status', methods=['POST'])
def update_order_status():
    api_key = request.headers.get('Authorization')
    response = UserClient.get_user(api_key)

    if not response:
        return make_response(jsonify({'message': 'Not logged in'}), 401)

    order_id = request.form['order_id']
    status = request.form['status']

    order = Order.query.filter_by(id=order_id).first()
    order.status = status
    db.session.commit()

    response = jsonify(order.to_json())
    return response