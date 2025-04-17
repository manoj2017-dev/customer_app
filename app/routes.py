from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

from app import mongo, db
from .models import User, Book

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

        user_id = mongo.db.users.insert_one({
            'name': name,
            'email': email,
            'password': password,
            'phone': phone,
            'product': product
        }).inserted_id

        user_doc = mongo.db.users.find_one({'_id': user_id})
        login_user(User(user_doc))
        flash('Signup successful!')
        return redirect(url_for('main.dashboard'))

    return render_template('signup.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user_doc = mongo.db.users.find_one({'email': email})
        if user_doc and check_password_hash(user_doc['password'], password):
            login_user(User(user_doc))
            return redirect(url_for('main.dashboard'))

        flash('Invalid email or password')
    return render_template('login.html')

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))

# ---------- Book Management (SQLAlchemy) ----------

@main.route('/books')
@login_required
def books():
    book_list = Book.query.limit(10).all()
    return render_template('books.html', books=book_list)

@main.route('/add-book', methods=['GET', 'POST'])
@login_required
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        description = request.form.get('description')

        new_book = Book(title=title, author=author, description=description)
        db.session.add(new_book)
        db.session.commit()

        flash('Book added successfully!')
        return redirect(url_for('main.books'))

    return render_template('add_book.html')
