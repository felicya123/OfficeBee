from app import db
from datetime import datetime

class Product(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement= True)
    product_name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(10000), nullable=True)
    rating = db.Column(db.Float, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    stocks = db.Column(db.BigInteger, nullable=True)
    price = db.Column(db.BigInteger, nullable=True)

    def __repr__(self):
        return '<Product {}>'.format(self.name)
