from app.model.product import Product
from app.model.transaction import Transaction

from app import response, app, db
from flask import request, jsonify, abort

def index():
    try:
        product = Product.query.all()
        data = formatarray(product)
        return response.success(data, "success")
    except Exception as e:
        return response.failed(e, "Not Found")


def formatarray(datas):
    array = []
    for i in datas:
        array.append(sigleObj(i))
    return array

def sigleObj(data):
    data = {
        'id':data.id,
        'product_name':data.product_name,
        'description':data.description,
        'rating':data.rating,
        'review':data.review,
        'stocks':data.stocks,
        'price':data.price,
    }

    return data


def detail(id):
    try:
        product = Product.query.filter_by(id=id).first()
        transaction = Transaction.query.filter(Transaction.product_id==id)

        if not product:
            return response.failed([],"Not found")
        
        detailTrx = formatTrx(transaction)
        data = formatProductTrx(product, detailTrx)
        return response.success(data, "success")
    except Exception as e:
        return response.failed(e, "failed")


def formatProductTrx(product, transaction):
    data = {
        "id": product.id,
        "product_name":product.product_name,
        "description":product.description,
        "rating":product.rating,
        "review":product.review,
        "stocks":product.stocks,
        "price":product.price,
        "transaction":transaction
    }
    return data
    

def formatTrx(data):
    array =  []
    for i in data:
        array.append(singleTrx(i))
    return array


def singleTrx(dataTrx):
    data = {
        "id":dataTrx.id,
        "product_id":dataTrx.product_id,
        "quantity":dataTrx.quantity
    }
    return data


def save():
    try:
        product_name = request.form.get('product_name')
        description = request.form.get('description')
        rating = request.form.get('rating')
        review = request.form.get('review')
        stocks = request.form.get('stocks')
        price = request.form.get('price')

        input = [{
            'product_name':product_name,
            'description':description,
            'rating':rating,
            'review':review,
            'stocks':stocks,
            'price':price
        }]
        products = Product(product_name=product_name, description=description,rating=rating,review=review,stocks=stocks, price=price)
        db.session.add(products)
        db.session.commit()
        
        return response.success(input,"Product inserted successfully")
    except Exception as e:
        return response.failed(e,"Product failed to inserted")

# updated
def update(id):
    try:
        product_name = request.form.get('product_name')
        description = request.form.get('description')
        rating = request.form.get('rating')
        review = request.form.get('review')
        stocks = request.form.get('stocks')
        price = request.form.get('price')

        input = [
            {
                'product_name':product_name,
                'description':description,
                'rating':rating,
                'review':review,
                'stocks':stocks,
                'price':price
            }
        ]

        product = Product.query.filter_by(id=id).first()
        product.product_name = product_name
        product.description = description
        product.rating = rating
        product.review = review
        product.stocks = stocks
        product.price = price

        db.session.commit()
        return response.success(input, 'Product updated successfully')

    except Exception as e:
        return response.failed(e, "failed")

def delete(id):
    try:
        product = Product.query.filter_by(id=id).first()
        if not product:
            return response.failed([], 'Product is not found')
        
        db.session.delete(product)
        db.session.commit()

        return response.success('', 'Product deleted successfully')
    except Exception as e:
        return response.failed(e, "failed")


    
    