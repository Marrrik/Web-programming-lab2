from flask import Blueprint, redirect, url_for, render_template
laba3 = Blueprint('laba3', __name__)

@laba3.route('/lab3/')
def lab3():
    return render_template("lab3.html")