from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SQL_KEY') #'1488aa6bf6cbe3616527ee3508db8e52'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQL_URI') #'sqlite:///site.db'
db = SQLAlchemy(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

csrf = CSRFProtect(app)

from app import views