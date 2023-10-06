from flask import Blueprint, redirect, url_for, render_template, request
laba3 = Blueprint('laba3', __name__)

@laba3.route('/lab3/')
def lab3():
    return render_template("lab3.html")


@laba3.route('/lab3/form1')
def lab3_form1():
    user = request.args.get('user')
    age = request.args.get('age')
    sex = request.args.get('sex')
    return render_template("form1.html", user=user, age=age, sex=sex)