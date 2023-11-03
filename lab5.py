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

@laba5.route("/lab5")
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
