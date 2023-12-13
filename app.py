
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Db import db
from Db.models import users
from flask_login import LoginManager
from lab import lab
from lab2 import laba2
from lab3 import laba3
from lab4 import laba4
from lab5 import laba5
from lab7 import laba7
from lab8 import laba8

app = Flask(__name__)
from lab6 import laba6
app.secret_key = "123"
user_db = "admin_base_orm"
host_ip = "127.0.0.1"
host_port = "5432"
database_name = "base_orm"
password = "123"
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user_db}:{password}@{host_ip}:{host_port}/{database_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

login_manager = LoginManager()

login_manager.login_view = 'lab6.login'
login_manager.init_app(app)

@login_manager.user_loader

def load_users(user_id):
    return users.query.get(int(user_id))
app.register_blueprint(laba6)

app.register_blueprint(lab)
app.register_blueprint(laba2)
app.register_blueprint(laba3)
app.register_blueprint(laba4)
app.register_blueprint(laba5)
app.register_blueprint(laba7)
app.register_blueprint(laba8)



# blinker==1.6.2
# click==8.1.7
# colorama==0.4.6
# Flask==3.0.0
# Flask-Login==0.6.3
# Flask-SQLAlchemy==3.1.1
# greenlet==3.0.1
# itsdangerous==2.1.2
# Jinja2==3.1.2
# MarkupSafe==2.1.3
# psycopg2==2.9.9
# psycopg2-binary==2.9.9
# SQLAlchemy==2.0.23
# typing_extensions==4.8.0
# Werkzeug==3.0.1

