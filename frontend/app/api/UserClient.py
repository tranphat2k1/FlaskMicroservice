import requests
from flask import session, request

class UserClient:
    @staticmethod
    def post_login(form):
        api_key = False
        payload = {
            'username': form.username.data,
            'password': form.password.data
        }
        url = 'http://127.0.0.1:5001/api/user/login'
        response = requests.request("POST", url=url, data=payload)
        if response:
            d = response.json()
            print("This is response from user api: " + str(d))
            if d['api_key'] is not None:
                api_key = d['api_key']
        return api_key

    @staticmethod
    def get_user():
        headers = {
            'Authorization': 'Basic ' + session['user_api_key']
        }
        url = 'http://127.0.0.1:5001/api/user/is_login'
        response = requests.request(method="GET", url=url, headers=headers)
        user = response.json()
        return user

    @staticmethod
    def post_user_create(form):
        user = False
        payload = {
            'fullname': form.fullname.data,
            'phone_number': form.phone_number.data,
            'email': form.email.data,
            'username': form.username.data,
            'password': form.password.data,
        }
        url = 'http://127.0.0.1:5001/api/user/create'
        response = requests.request("POST", url=url, data=payload)
        if response:
            user = response.json()
        return user

    @staticmethod
    def does_exist(form):
        payload = {
            'fulname': form.fullname.data,
            'phone_number': form.phone_number.data,
            'email': form.email.data,
            'username': form.username.data,
            'password': form.password.data,
        }
        url = 'http://127.0.0.1:5001/api/user/exists'
        response = requests.request("GET", data=payload, url=url)
        message = response.json()
        return message

    @staticmethod
    def create_OTP(email):
        payload = {
            'email': email
        }
        url = 'http://127.0.0.1:5001/api/user/create_otp'
        response = requests.request("POST", data=payload, url=url)
        otp = response.json()
        return otp

    @staticmethod
    def get_otp(form):
        payload = {
            'otp': form.otp.data
        }
        url = 'http://127.0.0.1:5001/api/user/get_otp'
        response = requests.request("GET", data=payload, url=url)
        otp = response.json()
        return otp

    @staticmethod
    def change_password(new_password, email):
        payload = {
            'password': new_password,
            'email': email
        }
        url = 'http://127.0.0.1:5001/api/user/change_password'
        response = requests.request("POST", data=payload, url=url)
        return response.json()

    @staticmethod
    def get_address():
        headers = {
            'Authorization': 'Basic ' + session['user_api_key']
        }
        url = 'http://127.0.0.1:5001/api/user/address'
        response = requests.request(method="GET", url=url, headers=headers)
        address = response.json()
        return address

    @staticmethod
    def add_address(city, district, ward, road):
        payload = {
            'city': city,
            'district': district,
            'ward': ward,
            'road': road
        }
        headers = {
            'Authorization': 'Basic ' + session['user_api_key']
        }
        url = 'http://127.0.0.1:5001/api/user/add_address'
        response = requests.request(method="POST", data=payload, url=url, headers=headers)
        address = response.json()
        return address

    @staticmethod
    def does_exist_address(city, district, ward, road):
        payload = {
            'city': city,
            'district': district,
            'ward': ward,
            'road': road
        }
        headers = {
            'Authorization': 'Basic ' + session['user_api_key']
        }
        url = 'http://127.0.0.1:5001/api/user/address/exists'
        response = requests.request(method="POST", data=payload, url=url, headers=headers)
        address = response.json()
        return address