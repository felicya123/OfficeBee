from datetime import timedelta
from app.model.user import User

from app import response, app, db
from flask import request
from flask_jwt_extended import *




def createUser():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        level = 1


        input = [{
            'name':name,
            'email':email,
            'password':password,
            'level':level,
        }]

        users = User(name=name, email=email,level=level)
        users.setPassword(password)
        db.session.add(users)
        db.session.commit()
        
        return response.success(input,"inserted successfully")
    except Exception as e:
        print(e)
        return response.failed('',"inserted failed")

def singleObj(data):
    data={
        'id':data.id,
        'name':data.name,
        'email':data.email,
        'level':data.level
    }
    return data

def login():
    try:
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if not user:
            return response.failed('', 'email not found')
        elif not user.checkPassword(password):
            return response.failed('', 'wrong password')

        
        data = singleObj(user)

        expires = timedelta(days=7)
        expires_refresh = timedelta(days=7)

        access_token = create_access_token(data, fresh=True, expires_delta= expires)
        refresh_token = create_refresh_token(data, expires_delta=expires_refresh)
        

        return response.success({
            "data":data,
            "access_token":access_token,
            "refresh_token":refresh_token
            }, "login success")
    except Exception as e:
        print(e)
        return response.failed('','login failed')