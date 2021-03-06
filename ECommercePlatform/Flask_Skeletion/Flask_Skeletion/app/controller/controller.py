from flask import Blueprint, jsonify

from ..services.product_list import *
from ..services.product_by_ID import *
from ..services.add_product import *

uri = Blueprint("endpoint", __name__, url_prefix="/")

@uri.route("/")
def health_check():
    return "Welcome to E-Commerce Platform"

cart=dict()

# Task 1: Retrieve all the business products

@uri.route("/products", methods = ["GET"])
def fetch_product():
    product_list = get_products()
    res = dict()
    if(len(product_list)!=0):
        res['message'] = "All Business Products Retrieved"
        res['product_list'] = product_list
    else:
        res['message'] = "No products to show"
        res['product_list'] = []

    return (jsonify(res),200)

    
# Task 2: Retrieve details of a specific product based on product_id​

@uri.route("/products/<int:id>", methods = ["GET"])
def fetch_product_by_ID(id):
    product = get_product_by_id(id)
    res = dict()
    if(len(product)!=0):
        res['message'] = "Product Found!"
        res['product_list'] = product
    else:
        res['message'] = "No products to show"
        res['product_list'] = []

    return (jsonify(res),200)

# Task 3: Add a product to cart​

@uri.route("/addProduct/<int:product_id>", methods=["GET"])
def addProduct(product_id):  
    product = add_to_cart(product_id)
    res = dict()
    if(len(product)!=0):
        if product_id in cart:
            return (jsonify(cart),200)
        else:
            cart[product_id]=product

        return (jsonify(cart),200)

    return ("Product not found",404)

# Task 4: Delete a product from cart​

@uri.route("/deleteProduct/<int:product_id>", methods=["GET"])
def deleteProduct(product_id):
    if product_id in cart:
        cart.pop(product_id)
        return (jsonify(cart),200)
    else:
        return (jsonify(cart),200)


# Task 5: List products from cart​

@uri.route("/listCart", methods=["GET"])
def listCart():
    return (jsonify(cart),200)

# Task 6: Proceed to Purchase​

@uri.route("/purchase", methods=["GET"])
def purchase():
    total=0
    for product in cart:
        total=total+cart[product]["price"]
    return (f'Cart Total: {total}',200)
    