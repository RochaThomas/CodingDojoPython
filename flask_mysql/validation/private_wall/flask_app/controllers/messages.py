
from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.message import Message

@app.route('/send_message', methods=['POST'])
def send_message():
    if not session['logged_in']:
        return redirect('/')
    if not Message.is_valid_message(request.form):
        return redirect('/dashboard')
    data = {
        'sender_id': request.form['sender_id'],
        'receiver_id': request.form['receiver_id'],
        'content': request.form['content']
    }
    Message.save(data)
    return redirect('/dashboard')

@app.route('/delete/message/<int:message_id>')
def delete_message(message_id):
    data = {
        'id': message_id
    }
    Message.delete(data)
    return redirect('/dashboard')