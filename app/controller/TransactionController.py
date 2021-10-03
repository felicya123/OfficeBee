from app.model.transaction import Transaction
from app.model.product import Product 

from app import response, app, db
from flask import request

def index():
    try:
        product = Transaction.query.all()
        data = formatarray(product)
        return response.success(data, "success")
    except Exception as e:
        print (e)

def formatarray(datas):
    array = []
    for i in datas:
        array.append(sigleObj(i))
    return array


def sigleObj(data):
    data = {
        'id':data.id,
        "product_id":data.product_id,
        "quantity":data.quantity
    }
    return data

def save():
    try:
        product_id = request.form.get('product_id')
        quantity = request.form.get('quantity')

        input = [{
            'product_id':product_id,
            'quantity':quantity,
        }]
        transaction = Transaction(product_id=product_id, quantity=quantity)
        product = Product.query.filter(Transaction.product_id==Product.id).first()
        product.stocks = decreaseStock(product,quantity)

        db.session.add(transaction)
        db.session.commit()
        
        return response.success(input,"inserted successfully")
    except Exception as e:
        print(e)
        return response.failed(input,"inserted failed")
    
def decreaseStock(product, qty):
    data = product.stocks - int(qty)
    return data