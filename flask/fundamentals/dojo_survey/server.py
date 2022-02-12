
from flask import Flask, render_template, request, redirect, session
app = Flask('__name__')
app.secret_key = 'Secret secrets are no fun, secret secrets hurt someone'

@app.route('/')
def disp_original():
    return render_template('index.html')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/process', methods=["POST"])
def process():
    print(request.form)
    session['name'] = request.form['full_name']
    session['location'] = request.form['location']
    session['fav_lang'] = request.form['fav_lang']
    session['comments'] = request.form['comments']
    return redirect('/results')

@app.route('/del_session', methods=["POST"])
def del_session():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)