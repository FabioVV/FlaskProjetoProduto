proximo_codigo = 15

prods = {
    1: {"nome": "Monitor ASUS Pro AXT", "preco": 1200, "ano": 2017, "desc": "Monitor 144hz",
        "url_foto": "https://www.asus.com/media/global/products/fIeqEqPIr9BRQXa1/i3smlrxWdm40xIFT_setting_xxx_0_90_end_2000.png"},
    2: {"nome": "RTX 3060 TI", "preco": 2300, "ano": 2020, "desc": "8GB de memória, GDDR6, LHR, DLSS, Ray Tracing",
        "url_foto": "https://img.terabyteshop.com.br/produto/g/placa-de-video-winfast-rtx-3060-ti-hurricane-8gb-gddr6-256-bits_113128.jpg"},
    3: {"nome": "Alienware X15", "preco": 17500, "ano": 2022, "desc": "i9-11900H RTX 3080 FHD", "url_foto": "https://www.notebookcheck.info/uploads/tx_nbc2/Alienwarex15-R1__1_.jpg"},
    4: {"nome": "Exterminator i9", "preco": 29000, "ano": 2022, "desc": "i9-10900 Rtx 3090ti- Ddr4 128gb - M.2 2tb - Hd 8t", "url_foto": "https://http2.mlstatic.com/D_NQ_NP_768107-MLB50628298466_072022-O.webp"},
    5: {"nome": "Alienware Area-51m", "preco": 7999, "ano": 2020, "desc": "i9-10900K, RTX 2080 Super", "url_foto": "https://www.notebookcheck.info/uploads/tx_nbc2/a3.JPG"},
    6: {"nome": "Workstation R1", "preco": 1299, "ano": 2017, "desc": "I5 2400 8gb Ssd 240 Gb", "url_foto": "https://http2.mlstatic.com/D_NQ_NP_736842-MLB50532055192_062022-O.webp"},
    7: {"nome": "Placa de Vídeo RX 6750 XT ELITE", "preco": 3599, "ano": 2019, "desc": "Tamanho da memória: 12 GB, Tipo de memória: GDDR6", "url_foto": "https://images.kabum.com.br/produtos/fotos/345888/placa-de-video-gigabyte-amd-radeon-rx-6750xt-gv-r675xtaorus-e-12gd_1652209231_gg.jpg"},
    8: {"nome": "Teclado Gamer Steelseries Apex 3", "preco": 5000, "ano": 2018, "desc": "RGB, Anti-ghosting, Switches Whisper-quiet", "url_foto": "https://images.kabum.com.br/produtos/fotos/sync_mirakl/396754/Teclado-Gamer-Steelseries-Apex-3-RGB-Anti-ghosting-Switches-Whisper-quiet-Us-64795_1666644520_gg.jpg"},
    9: {"nome": "Mouse Gamer Sem Fio Logitech G PRO", "preco": 499, "ano": 2017, "desc": "Wireless LIGHTSPEED, RGB LIGHTSYNC, Ambidestro, 6 Botões Programáveis, HERO 25K", "url_foto": "https://images.kabum.com.br/produtos/fotos/107333/mouse-gamer-sem-fio-logitech-g-pro-wireless-lightspeed-rgb-lightsync-ambidestro-6-botoes-programaveis-hero-25k-910-005271_1644501564_gg.jpg"},
    10: {"nome": "Monitor Dell XP-PRI", "preco": 2450, "ano": 2018, "desc": "Monitor 240hz OLED, no-ghosting", "url_foto": "https://images.kabum.com.br/produtos/fotos/115561/teclado-gamer-trust-gxt-835-azor-illuminated-led-us-23651_1596112638_gg.jpg"},
    11: {"nome": "Intel Core i7-11700F", "preco": 1999, "ano": 2018, "desc": "11ª Geração, 2.5 GHz (4.8GHz Turbo), Cache 16MB, Octa Core, 16 Threads, LGA1200", "url_foto": "https://images.kabum.com.br/produtos/fotos/148916/processador-intel-core-i7-11700f-11-geracao-cache-16mb-2-5-ghz-4-8ghz-turbo-lga1200-bx8070811700f_1615573619_gg.jpg"},
    12: {"nome": "AMD Ryzen 7 5800X", "preco": 1699, "ano": 2020, "desc": "3.8GHz (4.7GHz Max Turbo), Cache 36MB, Octa Core, 16 Threads", "url_foto": "https://images.kabum.com.br/produtos/fotos/129459/processador-amd-ryzen-9-5900x-cache-70mb-3-7ghz-4-8ghz-max-turbo-am4-100-100000063wof_1602600708_gg.jpg"},
    13: {"nome": "Intel Core i3-12100F", "preco": 1299, "ano": 2016, "desc": "3.3GHz (4.3GHz Max Turbo), Cache 12MB, LGA 1700", "url_foto": "https://images.kabum.com.br/produtos/fotos/283719/processador-intel-core-i3-12100f-cache-xmb-xghz-xghz-max-turbo-lga-1700-bx8071512100f_1640095096_gg.jpg"},
    14: {"nome": " intel core i7-11700k", "preco": 2399, "ano": 2019, "desc": "Memória cache 16mb 3.6ghz - 5.0ghz lga 1200", "url_foto": "https://images-submarino.b2w.io/produtos/3713501868/imagens/processador-intel-core-i7-11700k-16mb-3-6ghz-5-0ghz-lga-1200-bx8070811700k/3713501868_1_large.jpg"}
}
important_prod = {0: {"nome": "Raider GE76 - 12U", "preco": 59999, "ano": 2022, "desc": "RTX 3080 Ti, Core i9-12900HK e tela de 360Hz",
                      "url_foto": "https://asset.msi.com/resize/image/global/product/product_1639040638b7515d6bb3107aa4916d9302bac76680.png62405b38c58fe0f07fcef2367d8a9ba1/1024.png"}}


def adicionar_produto(id: int, produto):
    prods[id] = produto


def remover_produto(id: int):
    if id in prods:
        del prods[id]


def editar_produto(id: int, edit):
    if id in prods:
        prods[id] = edit
