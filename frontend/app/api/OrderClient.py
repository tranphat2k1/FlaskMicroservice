import requests
from flask import session, request

class OrderClient:
    @staticmethod
    def add_order(address_id, total):
        payload = {
            'address_id': address_id,
            'total': total
        }
        headers = {
            'Authorization': 'Basic ' + session['user_api_key']
        }
        url = 'http://127.0.0.1:5004/api/order/add'
        response = requests.request("POST", data=payload, url=url, headers=headers)
        order = response.json()
        return order

    @staticmethod
    def add_order_item(order_id, product_id, quantity):
        payload = {
            'order_id': order_id,
            'product_id': product_id,
            'quantity': quantity
        }
        headers = {
            'Authorization': 'Basic ' + session['user_api_key']
        }
        url = 'http://127.0.0.1:5004/api/order/add_order_item'
        response = requests.request("POST", data=payload, url=url, headers=headers)
        orderItem = response.json()
        return orderItem

    @staticmethod
    def get_orders():
        headers = {
            'Authorization': 'Basic ' + session['user_api_key']
        }
        url = 'http://127.0.0.1:5004/api/user/orders'
        response = requests.request("GET", url=url, headers=headers)
        order = response.json()
        return order

    @staticmethod
    def get_order_items(order_id):
        headers = {
            'Authorization': 'Basic ' + session['user_api_key']
        }
        url = 'http://127.0.0.1:5004/api/order/' + str(order_id) + '/get_order_items'
        response = requests.request("GET", url=url, headers=headers)
        order_items = response.json()
        return order_items

    @staticmethod
    def get_order_by_status(status):
        payload = {
            'status': status
        }
        headers = {
            'Authorization': 'Basic ' + session['user_api_key']
        }
        url = 'http://127.0.0.1:5004/api/orders/get_orders_by_status'
        response = requests.request("GET", url=url, data=payload, headers=headers)
        orders = response.json()
        return orders

    @staticmethod
    def update_order_status(order_id, status):
        payload = {
            'order_id': order_id,
            'status': status
        }
        headers = {
            'Authorization': 'Basic ' + session['user_api_key']
        }
        url = 'http://127.0.0.1:5004/api/order/update_status'
        response = requests.request("POST", url=url, data=payload, headers=headers)
        order = response.json()
        return order