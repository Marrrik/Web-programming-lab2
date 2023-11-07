from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, redirect, url_for, render_template, request, session
import psycopg2


laba5 = Blueprint('laba5', __name__)

cur = None
conn = None
def dbConnect():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database = "laba5",
        user = "marik_starchenko",
        password = "2003")
    
    return conn;
    
def dbClose(cursor, connection):
    cursor.close()
    connection.close()

@laba5.route("/lab5/")
def main():
    conn.close()
    cur.close()

    cur.execute("SELECT * FROM users;")

    result = cur.fetchall()

    print(result)

    dbClose(cur, conn)

    return "go to console"


@laba5.route('/lab5/users')
def show_users():
        connection = dbConnect()
        cursor = connection.cursor()

        # Выполните SQL-запрос для выбора имен пользователей
        cursor.execute("SELECT username FROM users")

        # Получите результаты запроса
        results = cursor.fetchall()

        # Закройте соединение
        cursor.close()
        connection.close()

        # Отобразите результаты в HTML
        return render_template('laba5.html', users=results)


@laba5.route('/lab5/glav')
def lab5_glav():
    user_name = session.get('user_name')
    return render_template('glav.html', user_name=user_name)


@laba5.route('/lab5/registr', methods=["GET", "POST"])
def registrPage():
    errors = []

    if request.method == "GET":
        return render_template('registr.html', errors=errors)
     
    user_name = request.form.get("user_name")
    password = request.form.get("password")


    if not (user_name or password):
        errors.append("Пожалуйста заполните все поля")
        print(errors)
        return render_template('registr.html', errors=errors)
    
    hashPassword = generate_password_hash(password)

    conn = dbConnect()
    cur = conn.cursor()

    cur.execute(f"SELECT username FROM users WHERE username = '{user_name}';")

    if cur.fetchone() is not None:
        errors.append("Пользователь с данным именем уже существует")

        conn.close()
        cur.close()
        return render_template('registr.html', errors=errors)
    
    cur.execute(f"INSERT INTO users (username, password) VALUES ('{user_name}', '{hashPassword}');")
    
    conn.commit()
    conn.close()
    cur.close()
    return redirect("/lab5/login5")


@laba5.route('/lab5/login5', methods=["GET", "POST"])
def loginPage():
    errors = []

    if request.method == "GET":
        return render_template("login5.html", errors=errors)
    
    user_name = request.form.get("username")
    password = request.form.get("password")

    if not (user_name or password):
        errors.append("Пожалуйста заполните все поля")
        return render_template("login5.html", errors=errors)
    
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute(f"SELECT id, password FROM users WHERE username = '{user_name}';")

    result = cur.fetchone()

    if result is None:
        errors.append("Неправильный логин или пароль")
        dbClose(cur, conn)
        return render_template("login5.html", errors=errors)
    
    userID, hashPassword = result

    if check_password_hash(hashPassword, password):
        session['id'] = userID
        session['user_name'] = user_name
        dbClose(cur, conn)
        return redirect("/lab5/glav")
    
    else:
        errors.append("Неправильный логин или пароль")
        return render_template("login5.html", errors=errors)