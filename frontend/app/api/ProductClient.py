import requests
from flask import session, request

class ProductClient:
    @staticmethod
    def get_brand(brand_id):
        url = 'http://127.0.0.1:5002/api/brand/' + str(brand_id)
        response = requests.request("GET", url=url)
        brand = response.json()
        return brand

    @staticmethod
    def get_product(product_id):
        url = 'http://127.0.0.1:5002/api/product/' + str(product_id)
        response = requests.request("GET", url=url)
        product = response.json()
        return product

    @staticmethod
    def get_brands():
        url = 'http://127.0.0.1:5002/api/brands'
        response = requests.request("GET", url=url)
        brands = response.json()
        return brands

    @staticmethod
    def get_products():
        url = 'http://127.0.0.1:5002/api/products'
        response = requests.request("GET", url=url)
        products = response.json()
        return products

    @staticmethod
    def get_products_by_brand(brand_id):
        url = 'http://127.0.0.1:5002/api/products_by_brand/' + str(brand_id)
        response = requests.request("GET", url=url)
        products = response.json()
        return products

    @staticmethod
    def get_products_by_keyword(keyword):
        payload = {
            'keyword': keyword
        }
        url = 'http://127.0.0.1:5002/api/products_by_keyword/'
        response = requests.request("GET", data=payload, url=url)
        products = response.json()
        return products

    @staticmethod
    def add_brand(brand_name):
        payload = {
            'name': brand_name
        }
        url = 'http://127.0.0.1:5002/api/brand/add'
        response = requests.request("POST", data=payload, url=url)
        brand = response.json()
        return brand

    @staticmethod
    def edit_brand(form):
        payload = {
            'brand_id': form['id'],
            'name': form['name']
        }
        url = 'http://127.0.0.1:5002/api/brand/edit'
        response = requests.request("POST", data=payload, url=url)
        brand = response.json()
        return brand

    @staticmethod
    def add_product(form, img):
        payload = {
            'name': form['name'],
            'price': form['price'],
            'discount': form['discount'],
            'stock': form['stock'],
            'desc': form['desc'],
            'img': img,
            'brand_id': form['brand']
        }
        url = 'http://127.0.0.1:5002/api/product/add'
        response = requests.request("POST", data=payload, url=url)
        product = response.json()
        return product

    @staticmethod
    def edit_product(form, img):
        payload = {
            'id': form['id'],
            'name': form['name'],
            'price': form['price'],
            'discount': form['discount'],
            'stock': form['stock'],
            'desc': form['desc'],
            'img': img,
            'brand_id': form['brand']
        }
        url = 'http://127.0.0.1:5002/api/product/edit'
        response = requests.request("POST", data=payload, url=url)
        product = response.json()
        return product