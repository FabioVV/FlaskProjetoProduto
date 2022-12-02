from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, SubmitField, PasswordField, BooleanField, EmailField, ValidationError, TextAreaField, FloatField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, equal_to, length



class UserForm(FlaskForm):
    name = StringField("Nome", validators=[DataRequired()])
    username = StringField("Usuário", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    foto_perfil = FileField("Imagem de perfil")
    password_hash = PasswordField("Senha", validators=[DataRequired(), equal_to('password_hash2', message="As duas senhas devem ser iguais!")])
    password_hash2 = PasswordField("Senha novamente", validators=[DataRequired()])
    submit = SubmitField("Criar conta")

class ProductsForm(FlaskForm):
    name = StringField("Nome do produto", validators=[DataRequired()])
    desc = StringField("Descrição do produto", validators=[DataRequired()])
    category = StringField("Categoria do produto", validators=[DataRequired()])
    price = FloatField("Preço do produto", validators=[DataRequired()])
    submit = SubmitField("Registrar produto")

class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("Entrar")


class SearchForm(FlaskForm):
    searched = StringField("Campo de pesquisa", validators=[DataRequired()])
    submit = SubmitField('Pesquisar')
