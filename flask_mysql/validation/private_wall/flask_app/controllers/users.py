
from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
from flask_app.models.message import Message
bcrypt = Bcrypt(app)

@app.route('/')
def disp_default():
    return render_template('index.html')

@app.route('/dashboard')
def disp_dashboard():
    if not session['logged_in']:
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    user = User.get_user_by_id(data)
    messages = Message.get_received_messages(data)
    users = User.get_all_users()
    return render_template('success.html', user=user, users=users, messages=messages)

@app.route('/register/user', methods=['POST'])
def register_new_user():
    if not User.registration_is_valid(request.form):
        return redirect('/')
    hashed_pw = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': hashed_pw
    }
    user_id = User.save(data)
    session['user_id'] = user_id
    session['logged_in'] = True
    return redirect('/dashboard')

@app.route('/login/user', methods=['POST'])
def login_user():
    data = {
        'email': request.form['email']
    }
    user_in_db = User.get_user_by_email(data)
    if not user_in_db:
        flash('Invalid email and/or password')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid email and/or password')
        return redirect('/')
    session['user_id'] = user_in_db.id
    session['logged_in'] = True
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect('/')