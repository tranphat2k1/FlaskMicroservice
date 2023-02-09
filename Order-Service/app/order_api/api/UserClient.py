import requests

class UserClient:
    @staticmethod
    def get_user(api_key):
        headers = {
            'Authorization': api_key
        }
        response = requests.request(method="GET", url='http://127.0.0.1:5001/api/user/is_login', headers=headers)
        if response.status_code == 401:
            return False
        user = response.json()
        return user

    @staticmethod
    def get_user_by_id(user_id):
        response = requests.request(method="GET", url='http://127.0.0.1:5001/api/user/' + str(user_id))
        user = response.json()
        return user

    @staticmethod
    def get_address_byID(address_id):
        response = requests.request(method="GET", url='http://127.0.0.1:5001/api/user/address/' + str(address_id))
        address = response.json()
        return address