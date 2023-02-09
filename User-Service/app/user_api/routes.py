from . import user_api_blueprint
from .. import db, login_manager
from ..models import User, Address, OTP
from flask import make_response, request, jsonify
from flask_login import current_user, login_user, logout_user, login_required
import hashlib, datetime, random, math

def OTPGenerator():
    digits = "0123456789"
    otp = ''
    for _ in range(6):
        otp += digits[math.floor(random.random() * 10)]
    return otp

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

@login_manager.request_loader
def load_user_from_request(request):
    api_key = request.headers.get('Authorization')
    if api_key:
        api_key = api_key.replace('Basic ', '', 1)
        user = User.query.filter_by(api_key=api_key).first()
        if user:
            return user
    return None

@user_api_blueprint.route('/api/users', methods=['GET'])
def get_users():
    data = []
    for row in User.query.all():
        data.append(row.to_json())

    response = jsonify(data)
    return response

@user_api_blueprint.route('/api/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    response = jsonify(user.to_json())
    return response

@user_api_blueprint.route('/api/user/create', methods=['POST'])
def post_register():
    fullname = request.form['fullname']
    phone_number = request.form['phone_number']
    email = request.form['email']
    username = request.form['username']

    password = hashlib.md5((request.form['password']).encode()).hexdigest()

    user = User()
    user.fullname = fullname
    user.phone_number = phone_number
    user.email = email
    user.password = password
    user.username = username
    user.role_id = 2

    db.session.add(user)
    db.session.commit()

    response = jsonify({'message': 'User added', 'result': user.to_json()})

    return response

@user_api_blueprint.route('/api/user/login', methods=['POST'])
def post_login():
    print(request.form.__dict__)
    username = request.form['username']
    password = hashlib.md5((request.form['password']).encode()).hexdigest()
    user = User.query.filter_by(username=username).first()
    if user:
        if password == user.password:
            user.encode_api_key()
            db.session.commit()
            login_user(user)

            return make_response(jsonify({'message': 'Logged in', 'api_key': user.api_key}))

    return make_response(jsonify({'message': 'Not logged in'}), 401)

@user_api_blueprint.route('/api/user/logout', methods=['POST'])
def post_logout():
    if current_user.is_authenticated:
        logout_user()
        return make_response(jsonify({'message': 'You are logged out'}))
    return make_response(jsonify({'message': 'You are not logged in'}))

@user_api_blueprint.route('/api/user/create_otp', methods=['POST'])
def create_OTP():
    now = datetime.datetime.now()
    email = request.form['email']

    user = User.query.filter_by(email=email).first()
    if user is not None:
        otp = OTPGenerator()
        check_otp = OTP.query.filter_by(id=otp).first()
        if check_otp is not None:
            otp = OTPGenerator()
        new_otp = OTP()
        new_otp.id = otp
        new_otp.expire_at = now + datetime.timedelta(minutes=5)
        new_otp.user_id = user.id
        user.modified_at = now
        db.session.add(new_otp)
        db.session.commit()

        response = jsonify({'message': 'OTP added', 'result': new_otp.to_json()})
        return response
    else:
        return make_response(jsonify({'message': False}))

@user_api_blueprint.route('/api/user/get_otp', methods=['GET'])
def get_OTP():
    now = datetime.datetime.now()
    id = request.form['otp']
    otp = OTP.query.filter_by(id=id).first()
    if otp is not None:
        if otp.expire_at > now:
            return make_response(jsonify({'message': True}))
        else:
            db.session.delete(otp)
            db.session.commit()
            return make_response(jsonify({'message': 'Mã OTP đã hết hạn'}))
    else:
        return make_response(jsonify({'message': 'Mã OTP không chính xác'}))

@user_api_blueprint.route('/api/user/change_password', methods=['POST'])
def change_password():
    new_password = hashlib.md5((request.form['password']).encode()).hexdigest()
    email = request.form['email']
    user = User.query.filter_by(email=email).first()
    user.password = new_password
    db.session.commit()
    return make_response(jsonify({'message': 'Password changed'}))

@user_api_blueprint.route('/api/user/exists', methods=['GET'])
def check_user():
    phone_number = request.form['phone_number']
    email = request.form['email']
    username = request.form['username']
    users = User.query.all()
    for u in users:
        if u.phone_number == phone_number:
            return make_response(jsonify({'message': 'Số điện thoại này đã được sử dụng'}))
        if u.email == email:
            return make_response(jsonify({'message': 'Email này đã được sử dụng'}))
        if u.username == username:
            return make_response(jsonify({'message': 'Username này đã được sử dụng'}))
    return make_response(jsonify({'message': 'valid'}))

@login_required
@user_api_blueprint.route('/api/user/is_login', methods=['GET'])
def is_login():
    if current_user.is_authenticated:
        return make_response(jsonify({'result': current_user.to_json()}))

    return make_response(jsonify({'message': 'Not logged in'})), 401

@user_api_blueprint.route('/api/user/address', methods=['GET'])
def get_address():
    address = Address.query.filter_by(user_id=current_user.id).first()
    if address is not None:
        response = jsonify(address.to_json())
    else:
        response = jsonify({'message': 'Cannot find address'})
    return response

@user_api_blueprint.route('/api/user/address/<int:address_id>', methods=['GET'])
def get_address_byID(address_id):
    address = Address.query.filter_by(id=address_id).first()
    response = jsonify(address.to_json())
    return response

@user_api_blueprint.route('/api/user/add_address', methods=['POST'])
def add_address():
    city = request.form['city']
    district = request.form['district']
    ward = request.form['ward']
    road = request.form['road']
    address = Address()
    address.city = city
    address.district = district
    address.ward = ward
    address.road = road
    address.user_id = current_user.id

    db.session.add(address)
    db.session.commit()

    response = jsonify(address.to_json())
    return response

@user_api_blueprint.route('/api/user/address/exists', methods=['POST'])
def does_exist_address():
    city = request.form['city']
    district = request.form['district']
    ward = request.form['ward']
    road = request.form['road']
    address = Address.query.filter_by(city=city, district=district, ward=ward, road=road, user_id=current_user.id).first()
    if address is not None:
        response = jsonify({'result': True, 'address': address.to_json()})
    else:
        response = jsonify({'result': False})
    return response
