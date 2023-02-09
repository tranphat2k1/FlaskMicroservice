import json
from . import spc_api_blueprint
from .. import db, login_manager
from ..models import ShoppingCart, CartItem
from .api.UserClient import UserClient
from .api.ProductClient import ProductClient
from flask import make_response, request, jsonify
import datetime

@spc_api_blueprint.route('/api/shoppingcart', methods=['GET'])
def get_spc():
    api_key = request.headers.get('Authorization')
    response = UserClient.get_user(api_key)

    if not response:
        return make_response(jsonify({'message': 'Not logged in'}), 401)

    user = response['result']
    u_id = user['id']

    spc = ShoppingCart.query.filter_by(user_id=u_id).first()
    if spc is not None:
        response = jsonify({'message': True, 'result': spc.to_json()})
        return response
    else:
        return make_response(jsonify({'message': False}))

@spc_api_blueprint.route('/api/shoppingcart/add_to_cart', methods=['POST'])
def add_to_cart():
    api_key = request.headers.get('Authorization')
    response = UserClient.get_user(api_key)

    if not response:
        return make_response(jsonify({'message': 'Not logged in'}), 401)

    user = response['result']
    u_id = user['id']
    p_id = int(request.form['product_id'])
    now = datetime.datetime.now()
    spc = ShoppingCart.query.filter_by(user_id=u_id).first()
    if spc is None:
        spc = ShoppingCart()
        spc.quantity = 1
        spc.user_id = u_id

        cart_item = CartItem(product_id=p_id, quantity=1)
        spc.items.append(cart_item)
    else:
        found = False

        for item in spc.items:
            if item.product_id == p_id:
                found = True
                item.quantity += 1
                item.modified_at = now
                spc.quantity +=1

        if found is False:
            cart_item = CartItem(product_id=p_id, quantity=1)
            spc.items.append(cart_item)
            spc.quantity +=1

    db.session.add(spc)
    db.session.commit()
    response = jsonify({'result': spc.to_json()})
    return response

@spc_api_blueprint.route('/api/shoppingcart/get_cart_items', methods=['GET'])
def get_cartItems():
    api_key = request.headers.get('Authorization')
    response = UserClient.get_user(api_key)

    if not response:
        return make_response(jsonify({'message': 'Not logged in'}), 404)

    user = response['result']
    u_id = user['id']

    spc = ShoppingCart.query.filter_by(user_id=u_id).first()
    if spc is not None:
        data = []
        cart_item = CartItem.query.filter_by(shoppingcart_id=spc.id).all()
        for item in cart_item:
            p = ProductClient.get_product(item.product_id)
            d = {
                'item_id': item.id,
                'name': p['name'],
                'price': p['price'],
                'discount': p['discount'],
                'quantity': item.quantity
            }
            data.append(d)
        response = jsonify({'message': True, 'result': data})
        return response
    else:
        return make_response(jsonify({'message': False}))

@spc_api_blueprint.route('/api/shoppingcart/get_cart_item', methods=['GET'])
def get_cartItem():
    api_key = request.headers.get('Authorization')
    response = UserClient.get_user(api_key)

    if not response:
        return make_response(jsonify({'message': 'Not logged in'}), 401)

    item_id = int(request.form['item_id'])

    cart_item = CartItem.query.filter_by(id=item_id).first()
    p = ProductClient.get_product(cart_item.product_id)
    cart_item = {
        'item_id': cart_item.id,
        'name': p['name'],
        'price': p['price'],
        'discount': p['discount'],
        'final_price': (int(p['price']) - int(p['price']*int(p['discount'])/100)) * int(cart_item.quantity),
        'product_id': p['id'],
        'quantity': cart_item.quantity
    }
    response = jsonify(cart_item)
    return response

@spc_api_blueprint.route('/api/shoppingcart/delete_cart_item', methods=['POST'])
def delete_from_cart():
    api_key = request.headers.get('Authorization')
    response = UserClient.get_user(api_key)

    if not response:
        return make_response(jsonify({'message': 'Not logged in'}), 401)

    user = response['result']
    u_id = user['id']
    item_id = int(request.form['item_id'])
    now = datetime.datetime.now()

    spc = ShoppingCart.query.filter_by(user_id=u_id).first()
    item = CartItem.query.filter_by(id=item_id).first()
    spc.quantity -= item.quantity
    spc.modified_at = now
    db.session.delete(item)
    db.session.commit()

    response = jsonify({'message': 'item deleted'})
    return response