from flask import Blueprint, render_template, request, abort
from datetime import datetime

laba8 = Blueprint('laba8', __name__)

@laba8.route('/lab8/')
def main():
    return render_template('lab8/index.html')

courses = [
    {"name": "C++", "videos": 3, "price": 3000},
    {"name": "basic", "videos": 30, "price": 0},
    {"name": "C#", "videos": 8}

]

@laba8.route('/lab8/api/courses/', methods=['GET'])
def get_courses():
    return courses


@laba8.route('/lab8/api/courses/<int:course_num>', methods=['GET'])
def get_course(course_num):
    if course_num < 0 or course_num > len(courses):
        return "Курс не найден", 404
    return courses[course_num]

