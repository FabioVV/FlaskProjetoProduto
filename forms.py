from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, SubmitField, PasswordField, BooleanField, EmailField, ValidationError, TextAreaField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, equal_to, length



class UserForm(FlaskForm):
    name = StringField("Nome", validators=[DataRequired()])
    username = StringField("Usuário", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    foto_perfil = FileField("Imagem de perfil")
    password_hash = PasswordField("Senha", validators=[DataRequired(), equal_to('password_hash2', message="As duas senhas devem ser iguais!")])
    password_hash2 = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("Crian conta")


class LoginForm(FlaskForm):
    username = StringField("Usuário", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    password_hash = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("Entrar")


class SearchForm(FlaskForm):
    searched = StringField("Campo de pesquisa", validators=[DataRequired()])
    submit = SubmitField('Pesquisar')
