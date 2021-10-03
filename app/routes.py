from operator import methodcaller
from threading import current_thread
from werkzeug.wrappers import request
from app import app, response
from app.controller import ProductController
from app.controller import TransactionController
from app.controller import UserController
from flask import request
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

@app.route('/')
def index():
    return ''

@app.route("/protected", methods=["GET"])
@jwt_required
def protected():
    current_user = get_jwt_identity()
    return response.success(current_user, 'Sukses')

@app.route('/product', methods=['GET','POST'])
def products():
    if request.method=='GET':
        return ProductController.index()
    else:
        return ProductController.save()

@app.route('/transaction', methods=['GET','POST'])
@jwt_required
def transaction():
    if request.method=='GET':
        return TransactionController.index()
    else:
        return TransactionController.save()


@app.route('/product/<id>', methods=['GET','PUT','DELETE'])
def productDetail(id):
    if request.method=='GET':
       return ProductController.detail(id)
    elif request.method=='PUT':
        return ProductController.update(id)
    else:
        return ProductController.delete(id)


@app.route('/createUser', methods=['POST'])
def createAdmin():
    return UserController.createUser()

@app.route('/login',methods=['POST'])
def logins():
    return UserController.login()