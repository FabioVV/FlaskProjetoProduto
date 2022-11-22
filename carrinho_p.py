from usuarios import *

carrinho_produtos = {}


def adicionar_carrinho(produto):
    carrinho_produtos.update(produto)


def remover_carrinho(produto):
    if produto in carrinho_produtos:
        del carrinho_produtos[produto]


def retorna_preco():
    soma = 0
    for prod in carrinho_produtos:
        soma += float(carrinho_produtos[prod]["preco"])
    return f'{soma:9.2f}'
