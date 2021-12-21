from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

app.config['SECRET_KEY'] = '1488aa6bf6cbe3616527ee3508db8e52'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins="*")
csrf = CSRFProtect(app)

from app import views