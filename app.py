from flask import Flask
app = Flask(__name__)

@app.route("/")
def start():
    return """
<!doctype html>
<html>
    <head>
        <title>Старченко Марк, Лабораторная 1</title>
    </head>
    <body>
        <header>
            <h1>ФБ, НГТУ, Лабораторная 1</h1>
        </header>

        <h1>web-сервер на flask</h1>

        <footer>
            ©<i>Марк Старченко, ФБИ-14, 2 курс, 2023</i>
        </footer>
    </body>
</html>
"""