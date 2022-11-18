from typing import Any, Callable

from flask import (Flask, flash, redirect, render_template, request, session,
                   url_for)
from werkzeug.wrappers.response import Response

from produtos import *
from usuarios import *

usuarios = user()

app = Flask(__name__)
app.secret_key = "chavesecreta"
app.config["SESSION_TYPE"] = "filesystem"


######
def quem_esta_logado() -> InformacoesUsuarioSemSenha or None:
    if "usuario_logado" not in session:
        return None
    login = str(session["usuario_logado"])
    logado = usuarios.revalidar(login)
    logar(logado)
    return logado


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
@app.route("/login")
def tela_login():
    mensagem = request.args.get("mensagem", "")
    erro = request.args.get("erro", "")
    return render_template("login.html", mensagem=mensagem, erro=erro)


@app.route("/login", methods=["POST"])
def login():
    logar(None)
    login_usuario = request.form.get("login", "")
    senha_usuario = request.form.get("senha", "")
    try:
        logar(usuarios.validar_login(login_usuario, senha_usuario))
        flash("Logado com sucesso!", "info")
        return redirect("/produto")
    except SenhaIncorreta as erro:
        flash("Senha incorreta!", "error")
        return redirect("/login")


@app.route("/usuario/novo")
def tela_novo_user():
    mensagem = request.args.get("mensagem", "")
    erro = request.args.get("erro", "")
    return render_template("novo_user.html", mensagem=mensagem, erro=erro)


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


@app.route("/logout", methods=["POST"])
@apenas_usuarios_logados
def logout():
    logar(None)
    flash("Você saiu da sua conta com sucesso!", "info")
    return redirect("/login")


def logar(usuario: InformacoesUsuarioSemSenha or None):
    if usuario is not None:
        session["usuario_logado"] = usuario.login
    elif "usuario_logado" in session:
        del session["usuario_logado"]


@app.route("/produto")
@apenas_usuarios_logados
def produtos():
    return render_template('todos_produtos.html', prod=prods)


@app.route("/produto/novo", methods=["POST"])
@apenas_usuarios_logados
def novo_produto():
    global proximo_codigo
    data = request.form
    cod = proximo_codigo
    proximo_codigo += 1
    p = {"nome": data["nome"],
         "preco": data["preco"], "ano": data["ano"], "desc": data["desc"]}
    adicionar_produto(cod, p)
    flash("Produto criado com sucesso.", "info")
    return redirect("/produto")


@app.route("/produto/novo")
@apenas_usuarios_logados
def novo_produto_form():
    vazio = {"nome": "", "preco": ""}
    return render_template("registrar_produto.html", prod=vazio, id_produto=-1)


@app.route("/produto/editar/<int:id_produto>")
@apenas_usuarios_logados
def editar_prod(id_produto):
    return render_template("registrar_produto.html", prod=prods[id_produto], id_produto=id_produto)


@app.route("/produto/editar/<int:id_produto>", methods=["POST"])
@apenas_usuarios_logados
def editar(id_produto):
    data = request.form
    produto = {"nome": data["nome"],
               "preco": data["preco"], "ano": data["ano"], "desc": data["desc"]}
    editar_produto(id_produto, produto)
    flash("Produto editado com sucesso.", "info")
    return redirect("/produto")


@app.route("/produto/excluir/<int:id_produto>", methods=["POST"])
@apenas_usuarios_logados
def excluir_prod(id_produto):
    remover_produto(id_produto)
    flash("Produto excluido com sucesso.", "info")
    return redirect("/produto")


if __name__ == "__main__":
    app.run("0.0.0.0", port=5002, debug=True)
