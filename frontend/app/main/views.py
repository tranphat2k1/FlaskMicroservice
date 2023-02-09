import json
from . import main
from ..api.ProductClient import ProductClient
from ..api.UserClient import UserClient
from ..api.OrderClient import OrderClient
from ..api.ShoppingCartClient import ShoppingCartClient
from flask import jsonify, render_template, session, redirect, url_for, flash, request
from flask_login import current_user, login_required

def isLogin():
    if 'user' not in session:
        return False
    return True

def getBrand():
    brands = ProductClient.get_brands()
    brandList = []
    for b in brands:
        brandList.append(b)
    return brandList

def getSPC():
    spc = ShoppingCartClient.get_spc()
    if spc['message'] != False:
        spc = spc['result']
        return spc
    else:
        return spc

@main.route('/')
def home():
    products = ProductClient.get_products()
    productList = []
    for p in products:
        productList.append(p)
    if isLogin() == False:
        return render_template('main/home.html', productList=productList, brandList=getBrand())
    return render_template('main/home.html', productList=productList, brandList=getBrand(), shoppingcart=getSPC())

@main.route('/profile')
def profile():
    if isLogin() == False:
        flash('Bạn chưa đăng nhập', 'danger')
        return redirect(url_for('auth.login'))
    info = session['user']
    return render_template('main/profile.html', info=info, shoppingcart=getSPC())

@main.route('/getproudctsbybrand/<int:brand_id>')
def get_products_by_brand(brand_id):
    products = ProductClient.get_products_by_brand(brand_id)
    productList = []
    for p in products:
        productList.append(p)
    if isLogin() == False:
        return render_template('main/home.html', productList=productList, brandList=getBrand())
    else:
        return render_template('main/home.html', productList=productList, brandList=getBrand(), shoppingcart=getSPC())

@main.route('/getproudctsbykeyword', methods=['GET', 'POST'])
def get_products_by_keyword():
    keyword = request.form['search']
    products = ProductClient.get_products_by_keyword(keyword)
    productList = []
    for p in products:
        productList.append(p)
    if isLogin() == False:
        return render_template('main/home.html', productList=productList, brandList=getBrand())
    else:
        return render_template('main/home.html', productList=productList, brandList=getBrand(), shoppingcart=getSPC())

@main.route('/product/detail/<int:product_id>')
def get_product_detail(product_id):
    product = ProductClient.get_product(product_id)
    products = ProductClient.get_products_by_brand(product['brand_id'])
    productList = []
    for p in products:
        productList.append(p)
    if isLogin() == False:
        return render_template('main/product_detail.html', product=product, productList=productList, brandList=getBrand())
    else:
        return render_template('main/product_detail.html', product=product, productList=productList, brandList=getBrand(), shoppingcart=getSPC())

@main.route('/addtocart')
def add_to_cart():
    if isLogin():
        product_id = request.args.get('id')
        result = ShoppingCartClient.add_to_cart(product_id)
        quantity = result['result']['quantity']
        return jsonify({'msg': True, 'count': quantity})
    else:
        flash('Bạn chưa đăng nhập', 'danger')
        return redirect(url_for('auth.login'))

@main.route('/shoppingcart')
def shoppingcart():
    if isLogin():
        spc = ShoppingCartClient.get_cart_items()
        if spc['message'] != False:
            itemList = []
            for item in spc['result']:
                itemList.append(item)
            return render_template('main/shoppingcart.html', itemList=itemList, brandList=getBrand(), shoppingcart=getSPC())
        else:
            return render_template('main/shoppingcart.html', brandList=getBrand(), shoppingcart=getSPC())
    else:
        flash('Bạn chưa đăng nhập', 'danger')
        return redirect(url_for('auth.login'))

@main.route('/shoppingcart/delete/<int:item_id>', methods=['GET'])
def deleteItem(item_id):
    ShoppingCartClient.delete_cart_item(item_id)
    return redirect(url_for('main.shoppingcart'))

@main.route('/orderinfo', methods=['GET', 'POST'])
def orderInfo():
    if isLogin():
        item_selected = []
        total = 0
        for id in request.form.getlist('item'):
            item = ShoppingCartClient.get_cart_item(id)
            item_selected.append(item)
            total += item['final_price']
        session['total'] = total
        address = UserClient.get_address()
        info = session['user']
        return render_template('main/order.html', brandList=getBrand(), shoppingcart=getSPC(), itemList=item_selected, total=total, address=address, info=info)
    else:
        flash('Bạn chưa đăng nhập', 'danger')
        return redirect(url_for('auth.login'))

@main.route('/order', methods=['POST'])
def order():
    city = request.form.get('city')
    district = request.form.get('district')
    ward = request.form.get('ward')
    road = request.form.get('road')
    total = session.get('total')
    exist = UserClient.does_exist_address(city, district, ward, road)
    if exist['result'] == False:
        address = UserClient.add_address(city, district, ward, road)
        address_id = address['id']
    else:
        address_id = exist['address']['id']
    order = OrderClient.add_order(address_id, total)
    order_id = order['id']
    for (product_id, quantity) in zip(request.form.getlist('product_id'), request.form.getlist('quantity')):
        OrderClient.add_order_item(order_id, product_id, quantity)
    for item_id in request.form.getlist('item_id'):
        ShoppingCartClient.delete_cart_item(item_id)
    return redirect(url_for('main.history'))

@main.route('/history')
def history():
    if isLogin():
        orderList = []
        orders = OrderClient.get_orders()
        for order in orders:
            orderList.append(order)
        return render_template('main/history.html', brandList=getBrand(), shoppingcart=getSPC(), orderList=orderList)
    else:
        flash('Bạn chưa đăng nhập', 'danger')
        return redirect(url_for('auth.login'))

@main.route('/history/orderdetail/<int:order_id>')
def orderDetail(order_id):
    if isLogin():
        order_items = OrderClient.get_order_items(order_id)
        itemList = []
        total = 0
        for item in order_items:
            itemList.append(item)
            total += item['final_price']
        return render_template('main/order_detail.html', brandList=getBrand(), shoppingcart=getSPC(), itemList=itemList, total=total)
    else:
        flash('Bạn chưa đăng nhập', 'danger')
        return redirect(url_for('auth.login'))
