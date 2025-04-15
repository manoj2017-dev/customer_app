from flask import Blueprint, render_template, request, redirect, session, url_for, flash
from app import mongo
from werkzeug.security import generate_password_hash, check_password_hash

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return redirect(url_for('main.login'))

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        phone = request.form['phone']
        product = request.form['product']

        if mongo.db.users.find_one({'email': email}):
            flash("Email already exists")
            return redirect(url_for('main.signup'))

        mongo.db.users.insert_one({
            'name': name,
            'email': email,
            'password': password,
            'phone': phone,
            'product': product
        })

        flash('Signup successful!')
        return redirect(url_for('main.login'))

    return render_template('signup.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = mongo.db.users.find_one({'email': email})
        if user and check_password_hash(user['password'], password):
            session['user'] = user['email']
            return redirect(url_for('main.dashboard'))
        flash('Invalid email or password')
    return render_template('login.html')

@main.route('/dashboard')
def dashboard():
    if 'user' in session:
        user = mongo.db.users.find_one({'email': session['user']})
        return render_template('dashboard.html', user=user)
    return redirect(url_for('main.login'))

@main.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('main.login'))
