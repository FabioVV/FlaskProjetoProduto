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
from forms import UserForm, LoginForm, ProductsForm, UpdateProduct
import os


app = Flask(__name__)
app.secret_key = "chavesecreta"

#DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:guerra998@localhost/cla'
db = SQLAlchemy(app)
migrate = Migrate(app,db)

#IMAGES
UPLOAD_FOLDER = 'static/prod_images'
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
    prods = Products.query.order_by(Products.date_added)
    return render_template("index.html",prods=prods)

##Checkout

@app.route("/checkout")
@login_required
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
    if form.validate_on_submit():
        user = Users.query.filter_by(email = form.email.data).first()
        #userlogin = Users.query.get_or_404(username = form.username.data).first()
        if user:
            if check_password_hash(user.password_hash, form.password.data):
                login_user(user)
                flash("Logado com sucesso!")
                return redirect(url_for("index"))
            else:
                flash("Senha errada.")
        else:
            flash("Email inexistente.")
    return render_template("login.html", form = form)

@app.route("/logout", methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    flash("Você saiu da sua conta.")
    return redirect(url_for('login'))


@app.route("/registrar", methods=['GET','POST'])
def registrar():
    form = UserForm()
    user = Users.query.filter_by(email = form.email.data).first()
    usern = Users.query.filter_by(email = form.username.data).first()
    if form.validate_on_submit():
        if user is None and usern is None:
            name = form.name.data
            username = form.username.data
            email = form.email.data
            passwordha = generate_password_hash(form.password_hash.data, 'sha256')
            new_user = Users(name = name, username = username, email = email, password_hash = passwordha)
            db.session.add(new_user)
            db.session.commit()

        name = ''
        username = ''
        email = ''
        passwordha = ''
        flash("Conta criada com sucesso!")
        return redirect(url_for('login'))
    return render_template("novo_user.html", form = form)

@app.route("/produtos")
def produtos():
    prods = Products.query.order_by(Products.date_added)
    return render_template('todos_produtos.html', prods = prods)

@app.route("/add-product", methods=['GET','POST'])
@login_required
def adicionar_produto():
    form = ProductsForm()

    if form.validate_on_submit():
        
        pic = request.files['produtc_pic']
        picfilename = secure_filename(pic.filename)
        picname = str(uuid.uuid1()) + "_" + picfilename
        pic = picname
        saver = request.files['produtc_pic']
        saver.save(os.path.join(app.config['UPLOAD_FOLDER'],picname))
        prod = Products(name = form.name.data, desc = form.desc.data, category = form.category.data, price = form.price.data, produtc_pic = pic)
        name = ''
        desc = ''
        category = ''
        price = 0

        db.session.add(prod)
        db.session.commit()
        flash("Produto registrado com sucesso.")

    return render_template('registrar_produto.html', form = form)


@app.route('/delete-product/<int:id>',methods=['POST'])
@login_required
def delete_product(id:int):
    product = Products.query.get_or_404(id)
    try:
        if current_user.admin == True:
            db.session.delete(product)
            db.session.commit()
            flash("Produto excluido.")
            return redirect(url_for('produtos'))
        else:
            flash("Permissão negada.")
            return redirect(url_for('produtos'))
    except:
        flash("Erro ao excluir produto.")
        return redirect(url_for('produtos'))

@app.route('/update-product/<int:id>',methods=['GET','POST'])
@login_required
def update_product(id:int):
    form = UpdateProduct()
    product = Products.query.get_or_404(id)
    if form.validate_on_submit():
        if current_user.admin == True:
            product.name = form.name.data
            product.price = form.price.data
            product.category = form.category.data
            product.desc = form.desc.data
            if request.files['produtc_pic']:
                product.produtc_pic = request.files['produtc_pic']
                picfilename = secure_filename(product.produtc_pic.filename)
                picname = str(uuid.uuid1()) + "_" + picfilename
                product.produtc_pic = picname
                saver = request.files['produtc_pic']
                saver.save(os.path.join(app.config['UPLOAD_FOLDER'],picname))

                db.session.commit()
                flash("Produto editado com sucesso!")
                return redirect(url_for('produtos'))
            else:
                db.session.commit()
                flash("Produto editado com sucesso!")
                return redirect(url_for('produtos'))
        else:
            flash("Permissão negada.")
    return render_template('editar_produto.html',form = form, product = product)

##

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(70), nullable=False, unique= True)
    name = db.Column(db.String(70), nullable=False)
    email = db.Column(db.String(75), nullable=False, unique= True)
    password_hash = db.Column(db.String(300), nullable=False)
    profile_pic = db.Column(db.String(300), nullable=True)
    date_added = db.Column(db.DateTime, default = datetime.utcnow)
    admin = db.Column(db.Boolean, default = False) 
    orders = db.relationship('OrderDetails', backref='order_details')
    cart = db.relationship('Cart', backref='cart_products')

class Products(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(70), nullable=False)
    desc = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(75), nullable=False)
    produtc_pic = db.Column(db.String(300), nullable = True)
    price = db.Column(db.Float, nullable=False)
    date_added = db.Column(db.DateTime, default = datetime.utcnow)
    date_modified = db.Column(db.DateTime, default = datetime.utcnow)
    
class Cart(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String(70), nullable=False)
    total = db.Column(db.Float, nullable=False, default= 0.00)
    date_added = db.Column(db.DateTime, default = datetime.utcnow)


class OrderDetails(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    total = db.Column(db.Float, nullable=False)
    date_added = db.Column(db.DateTime, default = datetime.utcnow)
    
    

if __name__ == "__main__":
    app.run("0.0.0.0", port=5002, debug=True)
