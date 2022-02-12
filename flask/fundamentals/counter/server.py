
from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'Secret secrets are no fun. Secret secrets hurt someone.'

@app.route('/')
def base_display():
    if 'refresh_counter' not in session:
        session['refresh_counter'] = 1
        print("is this running")
    else: 
        session['refresh_counter'] +=1
        print("then you better go catch it")
    return render_template("index.html", counter=session['refresh_counter'])

@app.route('/counter')
def count():
    # refreshing does plus 2 and ? appears in url
    session['refresh_counter'] += 2
    return render_template('index.html', counter=session['refresh_counter'])

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)