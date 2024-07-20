from flask import Flask, render_template, request, redirect, url_for, flash, session, current_app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    """
    User model to represent users in the database.
    """
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

def validate_password(password):
    """
    Validate the password against the given criteria.
    Criteria:
    - Must contain a lowercase letter
    - Must contain an uppercase letter
    - Must end in a number
    - Must be at least 8 characters long
    """
    if (len(password) >= 8 and
        re.search(r'[a-z]', password) and
        re.search(r'[A-Z]', password) and
        re.search(r'\d$', password)):
        return True
    return False

@app.route('/')
def index():
    """
    Route for the home page (login page).
    """
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Route for the registration page.
    Handles both GET and POST requests.
    """
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('register'))

        if not validate_password(password):
            flash('Password does not meet the criteria!', 'danger')
            return redirect(url_for('register'))

        if User.query.filter_by(email=email).first():
            flash('Email already registered!', 'danger')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(first_name=first_name, last_name=last_name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('thank_you'))

    return render_template('register.html')

@app.route('/thank_you')
def thank_you():
    """
    Route for the thank you page.
    Displayed after successful registration.
    """
    return render_template('thankyou.html')

@app.route('/check_password', methods=['POST'])
def check_password():
    """
    Route to check the user's password.
    """
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(email=username).first()

    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id
        flash('Login successful!', 'success')
        return redirect(url_for('secret_page'))
    else:
        flash('Invalid credentials!', 'danger')
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    """
    Route for logging out the user.
    Clears the session and redirects to the home page.
    """
    session.clear()  # Clear the session
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))

@app.route('/secret_page')
def secret_page():
    """
    Route for the secret page.
    Only accessible after successful login.
    """
    user_id = session.get('user_id')
    if user_id:
        user = db.session.query(User).get(user_id)

        return render_template('secret_page.html', user=user)
    else:
        flash('Please log in to access this page.', 'danger')
        return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, use_reloader=False)
