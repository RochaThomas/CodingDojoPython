from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.user import User

@app.route('/')
@app.route('/users')
def disp_users():
    users = User.get_all()
    print(users)
    return render_template("read.html", all_users = users)

@app.route('/user/new')
def disp_create_user():
    return render_template('create.html')

@app.route('/user/<int:user_id>')
def disp_one_user(user_id):
    data = {
        'id': user_id
    }
    return render_template('read_one.html', user = User.get_one(data))

@app.route('/user/<int:user_id>/edit')
def disp_edit_user(user_id):
    data = {
        'id': user_id
    }
    return render_template('edit.html', user = User.get_one(data))

@app.route('/process_create_new_user', methods = ["POST"])
def create_user():
    User.create_new_user(request.form)
    return redirect('/')

@app.route('/process_update_user', methods=["POST"])
def update_user():
    print(request.form)
    User.update(request.form)
    return redirect('/')

@app.route('/process_delete_user/<int:user_id>')
def delete_user(user_id):
    data = {
        'id': user_id
    }
    User.delete(data)
    return redirect('/')