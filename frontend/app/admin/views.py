from functools import wraps
import json
from . import admin
from ..api.UserClient import UserClient
from ..api.ProductClient import ProductClient
from ..api.OrderClient import OrderClient
from flask import current_app, jsonify, render_template, session, redirect, url_for, flash, request
from werkzeug.utils import secure_filename
import os

def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if session.get("role") != 'Admin':
                return redirect(url_for('main.home'))
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

@admin.route("/brand/getBrand", methods=['GET'])
@admin_required()
def getBrand():
    if request.method == 'GET':
        id = request.args.get('id')
        brand = ProductClient.get_brand(id)
        name = brand['name']
        if brand:
            return jsonify({'name': name})
        else:
            return jsonify({'msg': ''})

@admin.route("/product/getProduct", methods=['GET'])
@admin_required()
def getProduct():
    if request.method == 'GET':
        id = request.args.get('id')
        product = ProductClient.get_product(id)
        if product:
            return jsonify({'name': product['name'],
                            'price': product['price'],
                            'discount': product['discount'],
                            'stock': product['stock'],
                            'desc': product['desc'],
                            'brand' : product['brand_id'],
                            'img': product['image']})
        else:
            return jsonify({'msg': ''})

@admin.route('/')
@admin_required()
def home():
    return render_template('admin/layout.html')

@admin.route('/brand')
@admin_required()
def brand():
    brands = ProductClient.get_brands()
    brandList = []
    for b in brands:
        brandList.append(b)
    return render_template('admin/brand.html', brandList=brandList)

@admin.route('/brand/add', methods=['POST'])
@admin_required()
def add_brand():
    name = request.form.get('name')
    check = ProductClient.add_brand(name)
    if check['result'] != False:
        flash(check['message'], 'success')
        return redirect(url_for('admin.brand'))
    else:
        flash(check['message'], 'danger')
        return redirect(url_for('admin.brand'))

@admin.route('/brand/edit', methods=['POST'])
@admin_required()
def edit_brand():
    check = ProductClient.edit_brand(request.form)
    if check['result'] != False:
        flash(check['message'], 'success')
        return redirect(url_for('admin.brand'))
    else:
        flash(check['message'], 'danger')
        return redirect(url_for('admin.brand'))

@admin.route('/product')
@admin_required()
def product():
    products = ProductClient.get_products()
    productList = []
    for p in products:
        productList.append(p)
    brands = ProductClient.get_brands()
    brandList = []
    for b in brands:
        brandList.append(b)
    return render_template('admin/product.html', productList=productList, brandList=brandList)

@admin.route('/product/add', methods=['POST'])
@admin_required()
def add_product():
    img = request.files['img']
    filename = secure_filename(img.filename)
    check = ProductClient.add_product(request.form, filename)
    if check['result'] != False:
        img.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        flash(check['message'], 'success')
        return redirect(url_for('admin.product'))
    else:
        flash(check['message'], 'danger')
        return redirect(url_for('admin.product'))

@admin.route('/product/edit', methods=['POST'])
@admin_required()
def edit_product():
    product = ProductClient.get_product(request.form['id'])
    old_img = product['image']
    img = request.files['img']
    filename = secure_filename(img.filename)
    check = ProductClient.edit_product(request.form, filename)
    if check['result'] != False:
        if img.filename != '':
            os.remove(os.path.join(current_app.config['UPLOAD_FOLDER'], old_img))
            img.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            flash(check['message'], 'success')
            return redirect(url_for('admin.product'))
        else:
            flash(check['message'], 'success')
            return redirect(url_for('admin.product'))
    else:
        flash(check['message'], 'danger')
        return redirect(url_for('admin.product'))

@admin.route('/order/pending')
@admin_required()
def order_pending():
    orderList = OrderClient.get_order_by_status('Đang chờ xác nhận')
    return render_template('admin/order.html', orderList=orderList)

@admin.route('/order/packing')
@admin_required()
def order_packing():
    orderList = OrderClient.get_order_by_status('Đang được chuẩn bị')
    return render_template('admin/order.html', orderList=orderList)

@admin.route('/order/transporting')
@admin_required()
def order_transporting():
    orderList = OrderClient.get_order_by_status('Đang vận chuyển')
    return render_template('admin/order.html', orderList=orderList)

@admin.route('/order/complete')
@admin_required()
def order_complete():
    orderList = OrderClient.get_order_by_status('Hoàn tất')
    return render_template('admin/order.html', orderList=orderList)

@admin.route('/order/cancel')
@admin_required()
def order_cancel():
    orderList = OrderClient.get_order_by_status('Hủy')
    return render_template('admin/order.html', orderList=orderList)

@admin.route('/order/update_status', methods=['POST'])
@admin_required()
def edit_order():
    id = request.form.get('id')
    status = request.form.get('status')
    OrderClient.update_order_status(id, status)
    flash('Chỉnh sửa thành công', 'success')
    if status == 'Đang được chuẩn bị':
        return redirect(url_for('admin.order_packing'))
    if status == 'Đang vận chuyển':
        return redirect(url_for('admin.order_transporting'))
    if status == 'Hoàn tất':
        return redirect(url_for('admin.order_complete'))
    else:
        return redirect(url_for('admin.order_cancel'))

@admin.route('/order/<int:order_id>', methods=['GET'])
@admin_required()
def order_detail(order_id):
    order_items = OrderClient.get_order_items(order_id)
    itemList = []
    total = 0
    for item in order_items:
        itemList.append(item)
        total += item['final_price']
    return render_template('admin/order_detail.html', itemList=itemList, total=total)
