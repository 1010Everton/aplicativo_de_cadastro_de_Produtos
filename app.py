from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
app.secret_key = "algoqueeunaosei"

from views import *

if __name__ == '__main__':

        app.run(debug=True)
