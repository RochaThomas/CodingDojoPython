
from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/ninjas')
def disp_ninja():
    dojos = Dojo.get_all_dojos()
    return render_template('ninja.html', all_dojos = dojos)

@app.route('/ninjas/create/new', methods=['POST'])
def create_ninja():
    Ninja.create_new_ninja(request.form)
    return redirect(f"/dojos/{request.form['dojo_id']}")