from flask import Blueprint, render_template

laba7 = Blueprint('laba7', __name__)

@laba7.route('/lab7/')
def main():
    return render_template('lab7/index.html')