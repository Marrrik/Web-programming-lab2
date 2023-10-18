from flask import Blueprint, redirect, url_for, render_template, request
laba4 = Blueprint('laba4', __name__)

@laba4.route('/lab4/')
def lab4():
    return render_template("lab4.html")


@laba4.route('/lab4/login', methods=['GET', 'POST'])
def lab4_login():
    if request.method == 'GET':
        return render_template("login.html")

    username = request.form.get('username')
    password = request.form.get('password')
    error = None 
    if not username and not password:
        error = 'Нет логина и пароля'
    elif not username:
        error = 'Нет логина'
    elif not password:
        error = 'Нет пароля'
    elif username == 'Mark_St' and password == '2003':
        return render_template("success.html", username=username)
    else:
        error = 'Неверный логин или пароль!'

    return render_template("login.html", error=error, username=username, password=password)


@laba4.route('/lab4/freeze', methods=['GET', 'POST'])
def lab4_freeze():
    if request.method == 'GET':
        return render_template("freeze.html")
    
    temperature = request.form.get('temperature')
    if  not temperature:
        result = 'ошибка: не задана температура!'
    elif int(temperature) < -12:
        result = 'не удалось установить температуру — слишком низкое значение'
    elif int(temperature) > -1:
        result = 'не удалось установить температуру — слишком высокое значение'
    elif int(temperature) > -12 and int(temperature) < -9:
        result = f"Установлена температура: {temperature}°C ***"
    elif int(temperature) >= -8 and int(temperature) <= -5:
        result = f"Установлена температура: {temperature}°C **"
    elif int(temperature) >= -4 and int(temperature) <= -1:
        result = f"Установлена температура: {temperature}°C *"

    return render_template("freeze.html", result=result)