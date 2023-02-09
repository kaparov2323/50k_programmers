from flask import Flask, render_template, Response
from excel import open_file

app = Flask(__name__, template_folder='templates')

@app.route('/')
def homepage():
    return render_template('index.html', goods = open_file())
