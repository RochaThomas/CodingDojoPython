
from distutils.log import debug
from flask_app import app
from flask_app.controllers.users import User
from flask_app.controllers.messages import Message

if __name__=='__main__':
    app.run(debug=True)