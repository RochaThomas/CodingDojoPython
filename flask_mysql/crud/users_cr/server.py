
from operator import methodcaller
from flask import Flask, request, redirect, render_template
from user import User;
app = Flask(__name__)

@app.route('/')
@app.route('/users')
def disp_users():
    users = User.get_all()
    print(users)
    return render_template("read.html", all_users = users)

@app.route('/user/new')
def disp_create_user():
    return render_template('create.html')

@app.route('/process_create_new_user', methods = ["POST"])
def create_user():
    User.create_new_user(request.form)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)