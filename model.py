from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User( UserMixin, db.Model):
    id = db.Column (db.Integer, primary_key=True)
    username = db.Column (db.String(15), unique=True)
    email = db.Column (db.String(200), nullable=False, unique=True, index=True)
    password = db.Column (db.String(20), nullable=False)
    role = db.Column (db.String(20), nullable=False, default='user')

class Products(db.Model):
    id = db.Column (db.Integer, primary_key=True)
    name = db.Column (db.String(30), nullable=False)
    price = db.Column (db.Float, nullable=False)
    stock = db.Column (db.Integer, nullable=False)
    image = db.Column (db.LargeBinary, nullable=False)
    create_at = db.Column (db.DateTime, nullable=False)
    
class Orders(db.Model):
    id = db.Column (db.Integer, primary_key=True)
    user_id = db.Column (db.Integer, db.ForeignKey('user.id'), nullable=False)
    total = db.Column (db.Integer, nullable=False)
    status = db.Column (db.Integer, nullable=False)
    create_at = db.Column (db.DateTime, nullable=False)
    
class OrderItem(db.Model):
    id = db.Column (db.Integer, primary_key=True)
    Order_id = db.Column (db.Integer, db.ForeignKey('orders.id'), nullable=False)
    Product_id = db.Column (db.Integer, db.ForeignKey('products.id'), nullable=False)
    qty = db.Column (db.Integer, nullable=False)
    unit_price = db.Column (db.Float, nullable=False)
