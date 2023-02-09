import requests

class ProductClient:
    @staticmethod
    def get_product(product_id):
        response = requests.request(method="GET", url='http://127.0.0.1:5002/api/product/' + str(product_id))
        product = response.json()
        return product

    @staticmethod
    def update_product_quantity(product_id, quantity):
        payload = {
            'product_id': product_id,
            'quantity': quantity
        }
        response = requests.request(method="POST", data=payload, url='http://127.0.0.1:5002/api/product/update_quantity')
        product = response.json()
        return product