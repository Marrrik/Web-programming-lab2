from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return """
<!doctype html>
<html>
    <head>
        <title>Старченко Марк, Лабораторная 1</title>
    </head>
    <body>
        <header>
            <h1>«НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</h1>
        </header>

        <ol>
            <li><a href = "http://127.0.0.1:5000/lab1" target="_blank">Лабораторная работа 1</a></li>
        </ol>

        <footer>
            ©<i>Марк Старченко, ФБИ-14, 2 курс, 2023</i>
        </footer>
    </body>
</html>
"""

@app.route("/lab1")
def lab1():
    return"""
<!doctype html>
<html>
    <head>
        <title>Старченко Марк, Лабораторная 1</title>
    </head>
    <body>
        <header>
            <h1>ФБ, НГТУ, Лабораторная 1</h1>
        </header>

        <div>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </div>

        <footer>
            ©<i>Марк Старченко, ФБИ-14, 2 курс, 2023</i>
        </footer>
    </body>
</html>
"""