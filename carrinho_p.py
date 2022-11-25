from usuarios import *

carrinho_produtos = {}
codig_produto_carrinho = 0


def adicionar_carrinho(produto):
    carrinho_produtos.update(produto)


def remover_carrinho(produto):
    if produto in carrinho_produtos:
        del carrinho_produtos[produto]


def retorna_preco():
    soma = 0
    for prod in carrinho_produtos:
        if carrinho_produtos[prod]["nome"] == "Exterminator i9" or carrinho_produtos[prod]["nome"] == "Workstation R1":
            aux = float(carrinho_produtos[prod]["preco"]) * 0.40
            aux2 = aux - float(carrinho_produtos[prod]["preco"])
            soma += aux2
        soma += float(carrinho_produtos[prod]["preco"])
    return f'{soma:9.2f}'
