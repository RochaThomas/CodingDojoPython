
from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def disp_default():
    if 'user_id' in session:
        return redirect('/dashboard')
    return render_template('index.html')

@app.route('/dashboard')
def disp_dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    user = User.get_user_by_id(data)
    recipes = Recipe.get_all_recipes()
    return render_template('dashboard.html', user=user, recipes=recipes)

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
    return redirect('/dashboard')

@app.route('/login/user', methods=['POST'])
def login_user():
    if not User.login_is_valid(request.form):
        return redirect('/')
    user_in_db = User.get_user_by_email(request.form)
    session['user_id'] = user_in_db.id
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')