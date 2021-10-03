from app import db
from datetime import datetime
from app.model.product import Product

class Transaction(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement= True, nullable=False)
    product_id = db.Column(db.BigInteger, db.ForeignKey(Product.id), nullable=False)
    quantity = db.Column(db.BigInteger, nullable=False)


    def __repr__(self):
        return '<Transaction {}>'.format(self.name)
