
from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def disp_default():
    return render_template('index.html')

@app.route('/success')
def disp_dashboard():
    if not session['logged_in']:
        return redirect('/')
    # some code to get a users info involving session
    # make another classmethod in user.py to get user by id
    # make user = User.get_user_by_id
    #user = user in return statement
    
    return render_template('success.html', user_first_name = session['first_name'])

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
    user_data = {
        'id': user_id
    }
    user = User.get_user_by_id(user_data)
    session['user_id'] = user.id
    session['first_name'] = user.first_name
    session['logged_in'] = True
    return redirect('/success')

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
    session['first_name'] = user_in_db.first_name
    session['logged_in'] = True
    return redirect('/success')

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect('/')