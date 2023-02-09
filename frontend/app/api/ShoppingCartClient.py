import requests
from flask import session, request

class ShoppingCartClient:
    @staticmethod
    def get_spc():
        headers = {
            'Authorization': 'Basic ' + session['user_api_key']
        }
        url = 'http://127.0.0.1:5003/api/shoppingcart'
        response = requests.request("GET", url=url, headers=headers)
        return response.json()

    @staticmethod
    def add_to_cart(product_id):
        payload = {
            'product_id': product_id
        }
        headers = {
            'Authorization': 'Basic ' + session['user_api_key']
        }
        url = 'http://127.0.0.1:5003/api/shoppingcart/add_to_cart'
        response = requests.request("POST", url=url, data=payload, headers=headers)
        return response.json()

    @staticmethod
    def get_cart_items():
        headers = {
            'Authorization': 'Basic ' + session['user_api_key']
        }
        url = 'http://127.0.0.1:5003/api/shoppingcart/get_cart_items'
        response = requests.request("GET", url=url, headers=headers)
        return response.json()

    @staticmethod
    def get_cart_item(item_id):
        payload = {
            'item_id': item_id
        }
        headers = {
            'Authorization': 'Basic ' + session['user_api_key']
        }
        url = 'http://127.0.0.1:5003/api/shoppingcart/get_cart_item'
        response = requests.request("GET", url=url, data=payload, headers=headers)
        return response.json()

    @staticmethod
    def delete_cart_item(item_id):
        payload = {
            'item_id': item_id
        }
        headers = {
            'Authorization': 'Basic ' + session['user_api_key']
        }
        url = 'http://127.0.0.1:5003/api/shoppingcart/delete_cart_item'
        response = requests.request("POST", url=url, data=payload, headers=headers)
        return response.json()

    # @staticmethod
    # def update_spc():
    #     payload = {
    #         'item_id': item_id
    #     }
    #     headers = {
    #         'Authorization': 'Basic ' + session['user_api_key']
    #     }
    #     url = 'http://127.0.0.1:5003/api/shoppingcart/delete_cart_item'
    #     response = requests.request("POST", url=url, data=payload, headers=headers)
    #     return response.json()
