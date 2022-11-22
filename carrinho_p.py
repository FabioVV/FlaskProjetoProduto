from usuarios import *

carrinho_produtos = {}


def adicionar_carrinho(produto):
    carrinho_produtos.update(produto)


def remover_carrinho(produto):
    if produto in carrinho_produtos:
        del carrinho_produtos[produto]
