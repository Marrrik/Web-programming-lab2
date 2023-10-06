from flask import Flask, redirect, url_for, render_template
from lab import lab
from lab2 import laba2
from lab3 import laba3


app = Flask(__name__)
app.register_blueprint(lab)
app.register_blueprint(laba2)
app.register_blueprint(laba3)
