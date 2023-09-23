# app/models.py
from app import db
from datetime import datetime
from flask_login import UserMixin

# User Model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # Define other user-related fields here

    def __repr__(self):
        return f'<User {self.username}>'

# Dish Model
class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    description = db.Column(db.String(256))
    price = db.Column(db.Float)
    # Define other dish-related fields here

    def __repr__(self):
        return f'<Dish {self.name}>'

# Order Model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    dish_id = db.Column(db.Integer, db.ForeignKey('dish.id'))
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    # Define other order-related fields here

    def __repr__(self):
        return f'<Order {self.id}>'
