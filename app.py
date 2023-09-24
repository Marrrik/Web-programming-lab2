from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code = 302)

@app.route("/menu")
def menu():
    return """
<!doctype html>
<head>
<link rel="stylesheet" type="text/css" href="/static/lab1.css">
</head>
<html>
    <head>
        <title>Старченко Марк, Лабораторная 1</title>
    </head>
    <body>
        <header>
            <h1>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</h1>
        </header>

        <main>
            <ol>
                <li><a href = "http://127.0.0.1:5000/lab1" target="blank">Лабораторная работа 1</a></li>
            </ol>
        </main>
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
<head>
<link rel="stylesheet" type="text/css" href="/static/lab1.css">
</head>
<html>
    <head>
        <title>Старченко Марк, Лабораторная 1</title>
    </head>
    <body>
        <header>
            <h1>ФБ, НГТУ, Лабораторная 1</h1>
        </header>
        <main>
            <div>
                Flask — фреймворк для создания веб-приложений на языке
                программирования Python, использующий набор инструментов
                Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
                называемых микрофреймворков — минималистичных каркасов
                веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
            </div>

            <a href="http://127.0.0.1:5000/menu" target="blank">Меню</a>

            <h2>Реализованные роуты</h2>

            <ul>
                <li><a href="http://127.0.0.1:5000/lab1/dub">/lab1/dub-дуб</a></li>
                <li><a href="http://127.0.0.1:5000/lab1/student">/lab1/student-я</a></li>
                <li><a href="http://127.0.0.1:5000/lab1/python">/lab1/python-python</a></li>
                <li><a href="http://127.0.0.1:5000/lab1/bk">/lab1/bk-back</a></li>
            </ul>
        </main>
        <footer>
            ©<i>Марк Старченко, ФБИ-14, 2 курс, 2023</i>
        </footer>
    </body>
</html>
"""

@app.route("/lab1/dub")
def dub(): 
    return'''
<!doctype html>
<head>
<link rel="stylesheet" type="text/css" href="/static/lab1.css">
</head>
<html>
    <body class="lab1bodydub">
    <h1>Дуб</h1>
    <img src = "''' + url_for('static', filename='dub.jpg') + '''">
    </body>
</html>
'''
@app.route("/lab1/student")
def student(): 
    return'''
<!doctype html>
<head>
<link rel="stylesheet" type="text/css" href="/static/lab1.css">
</head>
<html>
    <body class = "bodynstu">
    <h1>Старченко Марк Альбертович </h1>
    <img class = "nstu" src = "''' + url_for('static', filename='nstu.jpg') + '''">
    </body> 
</html>
'''

@app.route("/lab1/python")
def python(): 
    return'''
<!doctype html>
<head>
<link rel="stylesheet" type="text/css" href="/static/lab1.css">
</head>
<html>
    <body class="lab1bodypy">

    <h1 style = "text-aligin:center">О python</h1>

    <div class = "ramka">
        <div class = "textabautpy">
            <div style = "margin-top:25px">
                Создатель языка Python — нидерландский программист Гвидо ван Россум. Он был участником проекта по написанию ABC, языка для обучения программированию. В конце 1989 года Гвидо приступил к разработке нового языка и задумал его как потомка ABC, способного к обработке исключений и взаимодействию с операционной системой Amoeba. Так и получился Python.
            </div>

            <div style = "margin-top:25px">
                Откуда такое название? Многие разработчики считают, что язык назван в честь семейства змей, но это не так. Когда Гвидо работал над проектом, он любил смотреть комедийное шоу «Летающий цирк Монти Пайтона», поэтому и нарёк своё творение в честь британской комик-группы. Так что правильно произносить название языка как «Пайтон».
            </div>

            <div style = "margin-top:25px">
                В чём секрет такой популярности в использовании языка? Python подходит для решения широкого круга задач и применяется на всех популярных платформах. Росту популярности Python способствовала и его эффективность в стремительно развивающихся сферах Machine Learning и Data Science.
            </div>
        </div>
        
        <img class="imgpy" src = "''' + url_for('static', filename='py.png') + '''">
    </div>
    </body> 
</html>
'''

@app.route("/lab1/bk")
def backend(): 
    return'''
<!doctype html>
<head>
<link rel="stylesheet" type="text/css" href="/static/lab1.css">
</head>
<html>
    <body class="back">

    <h1 style = "text-aligin:center">О backend programming language</h1>

    <div class = "ramka_1">
        <div class = "textabautbk">
            <div style = "margin-top:25px">
               В бэкенде выделяются несколько востребованных языков: PHP, Java, Python, Ruby, JavaScript, C# и Go. Например, JavaScript активно используется для создания динамичных веб-приложений, в то время как Python славится своей простотой и расширенной библиотекой. Ruby с фреймворком Ruby on Rails подходит для быстрой разработки, в то время как Java обеспечивает надежность и масштабируемость. C# ориентирован на Windows-платформу, а Go – на высокую производительность. PHP остается одним из основных выборов для создания динамических веб-страниц на серверном языке.
            </div>

            <div style = "margin-top:25px">
                Для небольших проектов выбор языка программирования для серверной части может показаться незначительным. Времена сложных конфигураций и XML ушли в прошлое, а с современными MVC-фреймворками разработчики могут легко создать простое приложение на практически любом из указанных языков. Однако, при более серьезных задачах стоит учитывать особенности каждого языка и его способность эффективно решать поставленные задачи.
            </div>

            <div style = "margin-top:25px">
                Backend переводится с английского как «задний, дальний край» и означает внутреннюю, серверную часть сайта или приложения, которая не видна пользователю. Она соединяет клиента и базу данных и отвечает за взаимодействие между сервером и интерфейсом.
                Во frontend главное требование к языку — способность работать в браузере, в backend важны удобство, скорость и производительность. А еще — то, насколько язык подходит для конкретной задачи.
                Универсальной технологии не существует: под каждую выбирается своя, со своими преимуществами и недостатками. Для больших проектов обычно выбирают Java, средних — PHP, а быстро развивающихся стартапов — Ruby или Go. Почему так — читайте дальше.
            </div>
        </div>
        
        <img class="imgbk" src = "''' + url_for('static', filename='bk.png') + '''">
    </div>
    </body> 
</html>
'''

@app.route('/lab2/example')
def example():
    name = 'Мрак Старченко'
    lab = 'Лабораторная работа 2'
    num_group = 'ФБИ-14'
    rang = '2 курс'
    fruits = [
        {'name': 'яблоки', 'price':100},
        {'name': 'грущи', 'price':120},
        {'name': 'апельсины', 'price':80},
        {'name': 'мандарины', 'price':95},
        {'name': 'манго', 'price':321}
    ]

    books = [
        {"Author": "George Orwell", "Title": "1984", "Genre": "Science Fiction", "Number_of_Pages": 328},
        {"Author": "Fyodor Dostoevsky", "Title": "Crime and Punishment", "Genre": "Classic Literature", "Number_of_Pages": 672},
        {"Author": "J.K. Rowling", "Title": "Harry Potter and the Philosopher's Stone", "Genre": "Fantasy", "Number_of_Pages": 256},
        {"Author": "J.R.R. Tolkien", "Title": "The Lord of the Rings", "Genre": "Fantasy", "Number_of_Pages": 1216},
        {"Author": "Agatha Christie", "Title": "And Then There Were None", "Genre": "Detective", "Number_of_Pages": 256},
        {"Author": "Leo Tolstoy", "Title": "War and Peace", "Genre": "Classic Literature", "Number_of_Pages": 1225},
        {"Author": "George R.R. Martin", "Title": "A Game of Thrones", "Genre": "Fantasy", "Number_of_Pages": 694},
        {"Author": "Jane Austen", "Title": "Pride and Prejudice", "Genre": "Novel", "Number_of_Pages": 432},
        {"Author": "Ray Bradbury", "Title": "Fahrenheit 451", "Genre": "Science Fiction", "Number_of_Pages": 249},
        {"Author": "George Orwell", "Title": "Animal Farm", "Genre": "Satire", "Number_of_Pages": 144}
    ]

    return render_template('example.html', name=name, lab=lab, num_group=num_group, rang=rang, fruits = fruits, books=books)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/mem/')
def mem():
    return render_template('mem.html')