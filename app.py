from flask import Flask, render_template, Response, request
from excel import open_file, add_to_cell

app = Flask(__name__, template_folder='templates')

@app.route('/')
def homepage():
    return render_template('index.html', goods = open_file())

@app.route('/add/', methods=['post'])
def add():
    good = request.form['good']
    add_to_cell(good)
    return """
    <h1> Инвентарь заполнен </h1>
    <a href="/"> Домой </a>
    """
