from typing import Any, Callable

from flask import (Flask, flash, redirect, render_template, request, session,
                   url_for)
from werkzeug.wrappers.response import Response

from produtos import *
from usuarios import *

# Instacia a classe que guarda os usuarios
usuarios = user()
usuarios.admin_user("admin", "admin", "admin")
usuarios.novo_user("fabio", "fabio", "teste")

app = Flask(__name__)
app.secret_key = "chavesecreta"
app.config["SESSION_TYPE"] = "filesystem"


######
# Fnção que checa qual usuario esta logado
def quem_esta_logado() -> InformacoesUsuarioSemSenha or None:
    if "usuario_logado" not in session:
        return None
    login = str(session["usuario_logado"])
    logado = usuarios.revalidar(login)
    logar(logado)
    return logado

# FUnção que limita as funcionalidades do site, dando acesso apenas para usuarios logados


def apenas_usuarios_logados(wrapped: Callable[..., Any]) -> Callable[..., Any]:
    from functools import wraps

    @wraps(wrapped)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if quem_esta_logado() is None:
            return redirect(url_for("tela_login"))
        return wrapped(*args, **kwargs)
    return wrapper


######


@app.route("/")
def index():
    return render_template("index.html", prods=prods)


@app.route("/carrinho")
def carrinho():
    return render_template("carrinho.html")


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


@app.route("/ver_principal")
def ver_principal():
    return render_template("ver_principal.html", prods=prods)


# Esse é o login, essa função rendereiza a view do login, para se logar e se cadastrar
@app.route("/login")
def tela_login():
    return render_template("login.html")

# Aqui, é o os dados do formulario de login chegao, para se logar ou tratar erros


@app.route("/login", methods=["POST"])
def login():
    logar(None)
    login_usuario = request.form.get("login", "")
    senha_usuario = request.form.get("senha", "")
    try:

        logar(usuarios.validar_login(login_usuario, senha_usuario))
        flash("Logado com sucesso!", "info")
        return redirect("/produto")

    except SenhaIncorreta:

        flash("Senha incorreta!", "error")
        return redirect("/login")

# Essa função renderiza a tela de criação de novo usuario


@app.route("/usuario/novo")
def tela_novo_user():
    return render_template("novo_user.html")

# Aqui é onde os dados do formulario de criação de usuario chegam, para criar o usuario ou tratar erros


@app.route("/usuario/novo", methods=["POST"])
def novo_user():
    logar(None)
    login_usuario = request.form.get("login", "")
    nome_usuario = request.form.get("nome", "")
    senha_usuario = request.form.get("senha", "")
    senha_usuario2 = request.form.get("senha2", "")
    if senha_usuario != senha_usuario2:
        return redirect("/usuario/novo")
    try:
        usuarios.novo_user(login_usuario, nome_usuario, senha_usuario)
        flash("Conta criada com sucesso!", "info")
        return redirect("/login")
    except UsuarioJaExiste:
        flash("Usuário ja existe!", "info")
        return redirect("/usuario/novo")

# FUnção untilizada para deslogar o usuario, excluindo sua sessão


@app.route("/logout", methods=["POST"])
@apenas_usuarios_logados
def logout():
    logar(None)
    flash("Você saiu da sua conta com sucesso!", "info")
    return redirect("/login")

# Login propriamente dito, faz o login do usuario, caso os dados do formulario batam com os dados do banco de dados


def logar(usuario: InformacoesUsuarioSemSenha or None):
    if usuario is not None:
        session["usuario_logado"] = (usuario.login)

    elif "usuario_logado" in session:
        del session["usuario_logado"]

# Renderiza a tela que mostra todos os produtos registrados, apenas para usuarios logados, e a funcionalidade de criar novos produtos


@app.route("/produto")
@apenas_usuarios_logados
def produtos():
    return render_template('todos_produtos.html', prod=prods)

# AQui os dados do formulario de criação do produto chegam, e criam o produto ou trata erros.


@app.route("/produto/novo", methods=["POST"])
@apenas_usuarios_logados
def novo_produto():
    global proximo_codigo
    data = request.form
    cod = proximo_codigo
    proximo_codigo += 1
    p = {"nome": data["nome"],
         "preco": data["preco"], "ano": data["ano"], "desc": data["desc"], "url_foto": data["url_foto"]}
    adicionar_produto(cod, p)
    flash("Produto criado com sucesso.", "info")
    return redirect("/produto")

# Essa função renderiza a tela com o formulario ara criação do produto


@app.route("/produto/novo")
@apenas_usuarios_logados
def novo_produto_form():
    produto_vazio = {"nome": "", "preco": ""}
    return render_template("registrar_produto.html", prod=produto_vazio, id_produto=-1)


# ESsa funçÃp renderiza a tela de edição do produto selecionado


@app.route("/produto/editar/<int:id_produto>")
@apenas_usuarios_logados
def editar_prod(id_produto):
    return render_template("registrar_produto.html", prod=prods[id_produto], id_produto=id_produto)

# Essa função recebe as modificações do formulario de ediçãp e caso esteja sem erros, edita o produtos


@app.route("/produto/editar/<int:id_produto>", methods=["POST"])
@apenas_usuarios_logados
def editar(id_produto):
    data = request.form
    produto = {"nome": data["nome"],
               "preco": data["preco"], "ano": data["ano"], "desc": data["desc"], "url_foto": data["url_foto"]}
    editar_produto(id_produto, produto)
    flash("Produto editado com sucesso.", "info")
    return redirect("/produto")

# FUnção que exclui o produto selecionado


@app.route("/produto/excluir/<int:id_produto>", methods=["POST"])
@apenas_usuarios_logados
def excluir_prod(id_produto):
    remover_produto(id_produto)
    flash("Produto excluido com sucesso.", "info")
    return redirect("/produto")

# FUnção que renderiza a tela do produto selecionado


@app.route("/produto/<int:id>")
def verprod(id):
    for p in prods:
        if p == id:
            return render_template("ver.html", produto=prods[id])
    return render_template("produto404.html"), 404


if __name__ == "__main__":
    app.run("0.0.0.0", port=5002, debug=True)
