
from flask import (Flask, flash, redirect, render_template, request, url_for)
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import uuid as uuid
from flask_login import LoginManager, login_required, logout_user, current_user, login_user
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from flask_login import UserMixin
from datetime import date
from forms import UserForm, LoginForm
import os


app = Flask(__name__)
app.secret_key = "chavesecreta"

#DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:guerra998@localhost/cla'
db = SQLAlchemy(app)
migrate = Migrate(app,db)

#IMAGES
UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#LOGIN
loginm = LoginManager()
loginm.init_app(app)
loginm.login_view = 'login'
@loginm.user_loader
def load_user(userid):
    return Users.query.get(int(userid))



#ROUTES
@app.route("/")
def index():
    return render_template("index.html")

##Checkout
@app.route("/checkout")
def time():
    return render_template("checkout.html")

##NAVBAR
@app.route("/reservar")
def reservar():
    return render_template("reservar.html")


@app.route("/computador")
def computador():
    return render_template("computador.html")


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.route("/notebook")
def notebook():
    return render_template("notebook.html")


#APP

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template("login.html")


@app.route("/registrar", methods=['GET','POST'])
def registrar():
    form = UserForm()
    return render_template("login.html")


##

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(25), nullable=False, unique= True)
    name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(25), nullable=False, unique= True)
    password_hash = db.Column(db.String(25), nullable=False)
    profile_pic = db.Column(db.String(300), nullable=True)
    date_added = db.Column(db.DateTime, default = datetime.utcnow)
    admin = db.Column(db.Boolean, default = False, nullable=False)

if __name__ == "__main__":
    app.run("0.0.0.0", port=5002, debug=True)
