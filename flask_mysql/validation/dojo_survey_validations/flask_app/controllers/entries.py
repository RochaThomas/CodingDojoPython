
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.entry import Entry

@app.route('/')
def disp_default():
    return render_template('index.html')

@app.route('/results/<entry_name>')
def disp_result(entry_name):
    data = {
        'name': entry_name
    }
    return render_template('results.html', entry = Entry.get_one_survey_info(data))

@app.route('/results/processing', methods=['POST'])
def save_entry():
    print(request.form)
    if not Entry.validate_entry(request.form):
        return redirect('/')
    Entry.save(request.form)
    return redirect (f"/results/{request.form['name']}")