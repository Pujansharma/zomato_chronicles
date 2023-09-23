
from flask import render_template

# from app.models import  Dish
# from app.forms import LoginForm, RegistrationForm, ReviewForm, OrderForm
# from app.payments import process_payment
# from app.inventory import check_inventory
# from app.socketio import socketio
from app import create_app   
app = create_app()

# Define your routes and views below

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    # Display the menu of dishes
    # dishes = Dish.query.all()
    return render_template('menu.html')


