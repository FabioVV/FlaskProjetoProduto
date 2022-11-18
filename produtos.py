proximo_codigo = 5

prods = {
    1: {"nome": "Monitor ASUS Pro AXT", "preco": 1200, "ano": 2017, "desc": "Monitor 144hz"},
    2: {"nome": "RTX 3060 TI", "preco": 2302, "ano": 2020, "desc": "Placa de vídeo"},
    3: {"nome": "Apple iPhone XR (Red, 128 GB)", "preco": 6200, "ano": 2017, "desc": '128 GB ROM | 15.49 cm (6.1 inch) Display 12MP Rear Camera | 7MP Front Camera A12 Bionic Chip Processor'},
    4: {"nome": "OnePlus 7 Pro (Almond, 256 GB)", "preco": 5200, "ano": 2019, "desc": "Rear Camera|48MP (Primary)+ 8MP (Tele-photo)+16MP (ultrawide)| Front Camera|16 MP POP-UP Camera|8GB RAM|Android pie"}
}


def adicionar_produto(id: int, produto):
    prods[id] = produto


def remover_produto(id: int):
    if id in prods:
        del prods[id]


def editar_produto(id: int, edit):
    if id in prods:
        prods[id] = edit
