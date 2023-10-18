from flask import Blueprint, redirect, url_for, render_template, request
laba4 = Blueprint('laba4', __name__)

@laba4.route('/lab4/')
def lab4():
    return render_template("lab4.html")