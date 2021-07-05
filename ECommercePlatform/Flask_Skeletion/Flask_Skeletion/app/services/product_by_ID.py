import json

def get_product_by_id(product_id):
    with open('./products.json','r') as jsonfile:
        file_data = json.loads(jsonfile.read())

    for x in file_data:
        if x["sku"]==product_id:
            return x
    return {}