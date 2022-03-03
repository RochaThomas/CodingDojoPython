
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.restaurant import Restaurant
from flask_app.models.users_favorite import Users_favorite
from flask_app.models.user import User

@app.route('/restaurant/add_favorite')
def disp_add_favorite():
    if 'user_id' not in session:
        return redirect('/login')
    return render_template('add_favorite.html')

@app.route('/restaurant/add_favorite/process', methods=['POST'])
def add_favorite():
    # call a validation method for the entry
    pass