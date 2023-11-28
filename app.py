from flask import Flask, redirect, url_for, render_template
from lab import lab
from lab2 import laba2
from lab3 import laba3
from lab4 import laba4
from lab5 import laba5



app = Flask(__name__)
app.secret_key = "123"
app.register_blueprint(lab)
app.register_blueprint(laba2)
app.register_blueprint(laba3)
app.register_blueprint(laba4)
app.register_blueprint(laba5)

