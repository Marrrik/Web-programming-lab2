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


@laba4.route('/lab4/zerno', methods=['GET', 'POST'])
def lab4_zerno():
    if request.method == 'GET':
        return render_template("zerno.html")
    grain = request.form.get('grain')
    weight = float(request.form.get('weight'))
    price = 0
    skidka = None

    if grain == 'Ячмень':
        price = 12000
    elif grain == 'Овёс':
        price = 8500
    elif grain == 'Пшеница':
        price = 8700
    elif grain == 'Рожь':
        price = 14000
    else:
        price = 0
    
    summ = price * weight
    if weight >= 50 and weight <= 500:
        summ = (price * weight) * 0.9
        skidka_itog = (price * weight) * 0.1
        skidka = f'Скидка 10% за объём более 50 тон: = {skidka_itog}'
    elif weight < 50:   
        skidka = 'Скидка 10% за объём не присвена'
    else:
        skidka = None

 
    if weight > 500:
        errors = 'У нас нет столько зерна'
        return render_template("zerno.html", errors=errors)
    elif weight < 0:
        errors = 'Не верно указан объём закупки'
        return render_template("zerno.html", errors=errors)
    
    return render_template("zerno.html", grain=grain, weight=weight, summ=summ, skidka=skidka)


@laba4.route('/lab4/cookies', methods=['GET', 'POST'])
def lab4_cookies():
    if request.method == 'GET':
        return render_template("cookies.html")

    textColor = request.form.get('textColor')
    backgroundСolor = request.form.get('backgroundСolor')
    # print()
    fontSize = int(request.form.get('fontSize'))
    errorss = None

    if not fontSize:
        errorss = 'введите размер!!!'
        return redirect(url_for('lab4_cookies', errorss=errorss))
    if textColor == backgroundСolor:
        errorss = 'Цвет текста не должен совпадать с цветом фона.'
        return redirect(url_for('lab4_cookies', errorss=errorss))

    
    if fontSize>30 or fontSize<5:
        errorss = 'Размер текста должен быть от 5px до 30px.'
        return redirect(url_for('lab4_cookies', errorss=errorss))

    headers = {
        'Set-Cookie': [
            'textColor=' + textColor + 'path=/',
            'backgroundСolor=' + backgroundСolor + 'path=/',
            'fontSize=' + str(fontSize) + 'path=/'
        ],
        'Location': '/lab4/cookies'
    }

    return '', 303, headers
