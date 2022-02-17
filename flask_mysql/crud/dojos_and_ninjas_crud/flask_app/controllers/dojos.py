
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
@app.route('/dojos')
def disp_default():
    dojos = Dojo.get_all_dojos()
    return render_template('index.html', all_dojos = dojos)

@app.route('/dojos/<int:dojo_id>')
def disp_one_dojo(dojo_id):
    data = {
        'id': dojo_id
    }
    return render_template('dojo_show.html', dojo = Dojo.get_one_dojo_with_ninjas(data))

@app.route('/dojos/create/new', methods=['POST'])
def create_dojo():
    Dojo.create_new_dojo(request.form)
    return redirect('/dojos')