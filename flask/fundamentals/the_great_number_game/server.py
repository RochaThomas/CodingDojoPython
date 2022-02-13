
from contextlib import nullcontext
from crypt import methods
from flask import Flask, redirect, request, session, render_template
import random
app = Flask(__name__)
app.secret_key = "Secret secrets are no fun, secret secrets hurt someone"

@app.route('/')
def disp_default():
    session['rand_num'] = random.randint(1,100)
    return render_template('index.html', guess_this_num=session['rand_num'])
@app.route('/guess')
def disp_guess_results():
    session['result'] = None
    if session['num_guessed'] == session['rand_num']:
        session['result'] = 0
    elif session['num_guessed'] >= session['rand_num']:
        session['result'] = 1
    elif session['num_guessed'] <= session['rand_num']:
        session['result'] = 2
    return render_template('result.html')

@app.route('/process', methods=['POST'])
def process():
    session['num_guessed'] = int(request.form['num_guessed'])
    print(request.form)
    return redirect('/guess')

@app.route('/successful', methods=['POST'])
def successful():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)