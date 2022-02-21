
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.email import Email

@app.route('/')
def disp_default():
    return render_template('index.html')

@app.route('/success')
def disp_all_emails():
    return render_template('success.html', all_emails = Email.get_all_emails())

@app.route('/email/validation_processing', methods=['POST'])
def validate_email():
    if not Email.validate_email(request.form):
        return redirect('/')
    Email.save(request.form)
    return redirect('/success')

@app.route('/email/delete/<int:email_id>')
def delete_email(email_id):
    data = {
        'id': email_id
    }
    Email.delete(data)
    return redirect('/success')