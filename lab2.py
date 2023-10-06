from flask import Blueprint, redirect, url_for, render_template
laba2 = Blueprint('laba2', __name__)

@laba2.route('/lab2/example')
def example():
    name = 'Марк Старченко'
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

@laba2.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@laba2.route('/lab2/mem/')
def mem():
    return render_template('mem.html')