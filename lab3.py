from flask import Blueprint, redirect, url_for, render_template, request
laba3 = Blueprint('laba3', __name__)

@laba3.route('/lab3/')
def lab3():
    return render_template("lab3.html")


@laba3.route('/lab3/form1')
def lab3_form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    return render_template("form1.html", user=user, age=age, errors=errors)


@laba3.route('/lab3/orders')
def lab3_order():
    return render_template("orders.html")


@laba3.route('/lab3/pay')
def lab3_pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    elif drink == 'green-tea':
        price = 70
    else:
        price = ''
    if request.args.get('milk') == 'on':
        price +=30
    if request.args.get('sugar') == 'on':
        price +=10

    return render_template("pay.html", price=price)


@laba3.route('/lab3/itog')
def lab3_itog():
    return render_template("itog.html")


@laba3.route('/lab3/tiket')
def tiket():
    full_name = request.args.get('full_name')
    age = request.args.get('age')
    ticket_type = request.args.get('ticket_type')
    bunk = request.args.get('bunk')
    luggage = request.args.get('luggage')
    departure_point = request.args.get('departure_point')
    destination = request.args.get('destination')
    travel_date = request.args.get('travel_date')
    return render_template("tiket.html", full_name=full_name, age=age, ticket_type=ticket_type, bunk=bunk,luggage=luggage,departure_point=departure_point,
                           destination=destination,travel_date=travel_date)

@laba3.route('/lab3/tiket_pay')
def tiket_pay():
        full_price = 0
        ticket_type = request.args.get('ticket_type')
        if ticket_type == 'Взрослый':
            full_price = 2000
        elif ticket_type == 'Детский':
            full_price = 1000
        else:
            full_price = ''
        if request.args.get('luggage') == 'yes':
            full_price +=300
        bunk = request.args.get('bunk')
        if bunk == 'Нижняя':
            full_price += 500
        elif bunk == 'Верхняя':
            full_price += 300
        elif bunk == 'Верхняя боковая':
            full_price += 250
        elif bunk == 'Нижняя боковая':
            full_price += 400
        else:
            full_price = ''
        return render_template("tiket_pay.html", full_price=full_price)

@laba3.route('/lab3/itog_pay')
def itog_pay():
    return render_template("itog_pay.html")