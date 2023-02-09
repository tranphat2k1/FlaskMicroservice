import requests

class ProductClient:
    @staticmethod
    def get_product(product_id):
        response = requests.request(method="GET", url='http://127.0.0.1:5002/api/product/' + str(product_id))
        product = response.json()
        return product