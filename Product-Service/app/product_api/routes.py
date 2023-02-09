from . import product_api_blueprint
from .. import db, login_manager
from ..models import Brand, Product
from flask import make_response, request, jsonify
import datetime

@product_api_blueprint.route('/api/brands', methods=['GET'])
def get_brands():
    data = []
    for row in Brand.query.all():
        data.append(row.to_json())

    response = jsonify(data)
    return response

@product_api_blueprint.route('/api/products', methods=['GET'])
def get_products():
    data = []
    for p in Product.query.all():
        b = Brand.query.filter_by(id=p.brand_id).first()
        d = {
            'id': p.id,
            'name': p.name,
            'price': p.price,
            'discount': p.discount,
            'stock': p.stock,
            'desc': p.desc,
            'image': p.image,
            'brand_id': p.brand_id,
            'brand_name': b.name
        }
        data.append(d)

    response = jsonify(data)
    return response

@product_api_blueprint.route('/api/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    p = Product.query.filter_by(id=product_id).first()
    b = Brand.query.filter_by(id=p.brand_id).first()
    data = {
        'id': p.id,
        'name': p.name,
        'price': p.price,
        'discount': p.discount,
        'stock': p.stock,
        'desc': p.desc,
        'image': p.image,
        'brand_id': p.brand_id,
        'brand_name': b.name
    }
    response = jsonify(data)
    return response

@product_api_blueprint.route('/api/brand/<int:brand_id>', methods=['GET'])
def get_brand(brand_id):
    b = Brand.query.filter_by(id=brand_id).first()
    response = jsonify(b.to_json())
    return response

@product_api_blueprint.route('/api/products_by_brand/<int:brand_id>', methods=['GET'])
def get_products_by_brand(brand_id):
    data = []
    for row in Product.query.filter_by(brand_id=brand_id):
        data.append(row.to_json())

    response = jsonify(data)
    return response


@product_api_blueprint.route('/api/products_by_keyword/', methods=['GET'])
def get_products_by_keyword():
    keyword = request.form['keyword']
    data = []
    for row in Product.query.filter(Product.name.like("%"+keyword+"%")):
        data.append(row.to_json())

    response = jsonify(data)
    return response

@product_api_blueprint.route('/api/brand/add', methods=['POST'])
def add_brand():
    name = request.form['name']
    brand = Brand.query.filter_by(name=name).first()
    if brand is not None:
        return make_response(jsonify({'message':'Tên nhãn hiệu này đã tồn tại', 'result': False}))
    else:
        b = Brand()
        b.name = name

        db.session.add(b)
        db.session.commit()

        response = jsonify({'message': 'Thêm nhãn hiệu thành công', 'result': b.to_json()})
        return response

@product_api_blueprint.route('/api/brand/edit', methods=['POST'])
def edit_brand():
    now = datetime.datetime.now()
    b_id = request.form['brand_id']
    name = request.form['name']
    brand = Brand.query.filter_by(name=name).first()
    if brand is not None:
        return make_response(jsonify({'message':'Tên nhãn hiệu này đã tồn tại', 'result': False}))

    b = Brand.query.filter_by(id=b_id).first()
    b.name = name
    b.modified_at = now
    db.session.commit()

    response = jsonify({'message': 'Chỉnh sửa nhãn hiệu thành công', 'result': b.to_json()})
    return response

@product_api_blueprint.route('/api/product/add', methods=['POST'])
def add_product():
    name = request.form['name']
    price = request.form['price']
    discount = request.form['discount']
    stock = request.form['stock']
    desc = request.form['desc']
    b_id = request.form['brand_id']
    img = request.form['img']
    check = Product.query.filter_by(name=name).first()
    if check is not None:
        return make_response(jsonify({'message':'Tên sản phẩm này đã tồn tại', 'result': False}))

    p = Product()
    p.name = name
    p.price = price
    p.discount = discount
    p.stock = stock
    p.desc = desc
    p.image = img
    p.brand_id = b_id

    db.session.add(p)
    db.session.commit()

    response = jsonify({'message': 'Thêm sản phẩm thành công', 'result': p.to_json()})
    return response

@product_api_blueprint.route('/api/product/edit', methods=['POST'])
def edit_product():
    id = request.form['id']
    name = request.form['name']
    price = request.form['price']
    discount = request.form['discount']
    stock = request.form['stock']
    desc = request.form['desc']
    b_id = request.form['brand_id']
    img = request.form['img']
    now = datetime.datetime.now()

    p = Product.query.filter_by(id=id).first()
    p.name = name
    p.price = price
    p.discount = discount
    p.stock = stock
    p.desc = desc
    if img != '':
        p.image = img
    p.brand_id = b_id
    p.modified_at = now

    db.session.commit()

    response = jsonify({'message': 'Chỉnh sửa sản phẩm thành công', 'result': p.to_json()})
    return response

@product_api_blueprint.route('/api/product/update_quantity', methods=['POST'])
def update_product_quantity():
    id = request.form['product_id']
    quantity = request.form['quantity']
    now = datetime.datetime.now()

    p = Product.query.filter_by(id=id).first()
    p.stock = p.stock - int(quantity)
    p.modified_at = now

    db.session.commit()

    response = jsonify({'message': 'Chỉnh sửa sản phẩm thành công', 'result': p.to_json()})
    return response