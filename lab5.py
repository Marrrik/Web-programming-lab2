from flask import Blueprint, redirect, url_for, render_template, request
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
     return render_template('glav.html')




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
    
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute(f"SELECT username FROM users WHERE username = '{user_name}';")

    if cur.fetchone() is not None:
        errors.append("Пользователь с данным именем уже существует")

        dbClose(cur, conn)
        return render_template('registr.html', errors=errors)
    
    cur.execute(f"INSERT INTO users (username, password) VALUES ('{user_name}', '{password}');")
    
    conn.commit()
    dbClose(cur, conn)
    return redirect("/lab5/users")


def lab5_registr():
     return render_template('registr.html')