
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def eight_by_eight_default():
    return render_template("index.html", rows=8, columns=8, box1_color="red", box2_color="black")

@app.route("/<int:num_rows>")
def eight_by_num_rows(num_rows):
    return render_template("index.html", rows=num_rows, columns=8, box1_color="red", box2_color="black")

@app.route("/<int:num_rows>/<int:num_columns>")
def num_columns_by_num_rows(num_rows, num_columns):
    return render_template("index.html", rows=num_rows, columns=num_columns, box1_color="red", box2_color="black")

@app.route("/<int:num_rows>/<int:num_columns>/<string:color1>/<string:color2>")
def columns_rows_and_colors(num_rows, num_columns, color1, color2):
    return render_template("index.html", rows=num_rows, columns=num_columns, box1_color=color1, box2_color=color2)

if __name__=="__main__":
    app.run(debug=True)