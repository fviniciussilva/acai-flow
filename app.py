import flet as ft

carrinho = []

complementos = [
    "Granola",
    "Leite condensado",
    "Sucrilhos",
    "Paçoca",
    "Leite em pó",
    "morango",
]

produtos = [
    "Açaí 300ml",
    "Açaí 500ml",
    "Açaí 700ml",
    "Açaí 2 litros",
]


def main(page: ft.Page):
    page.title = "Açaí Flow"
    page.bgcolor = "#530146"
    page.padding = 24
    
    texto_carrinho = ft.Text("Carrinho vazio")
    lista_carrinho = ft.Column()
    produto_escolhido = None
    complementos_escolhidos = []
    texto_produto_escolhido = ft.Text("Nenhum açaí selecionado")

    def selecionar_produto(produto):
        nonlocal produto_escolhido
        produto_escolhido = produto
        texto_produto_escolhido.value = f"Produto selecionado: {produto}"
        page.update()

    def selecionar_complemento(complemento):
        complementos_escolhidos.append(complemento)
        texto_produto_escolhido.value = (
            f"Produto selecionado: {produto_escolhido}\n"
            f"Complementos: {', '.join(complementos_escolhidos)}"
        )
        page.update()

    def atualizar_carrinho():
        texto_carrinho.value = f"Itens no carrinho: {len(carrinho)}"
        lista_carrinho.controls.clear()

        for item in carrinho:
            lista_carrinho.controls.append(ft.Text(item))

        page.update()

    def adicionar_ao_carrinho(produto):
        carrinho.append(produto)
        atualizar_carrinho()

    page.add(
        ft.Text(
            "🍧 Açaí Flow",
            size=28,
            weight=ft.FontWeight.BOLD,
            color="#F5B3E4",
            text_align=ft.TextAlign.CENTER,
        )
    )

    page.add(texto_carrinho)
    page.add(lista_carrinho)
    page.add(texto_produto_escolhido)

    # Cada produto pode ser escolhido para montar o pedido.
    for produto in produtos:
        page.add(
            ft.Row(
                [
                    ft.Text(produto),
                    ft.ElevatedButton(
                        "Escolher",
                        on_click=lambda _, produto=produto: selecionar_produto(produto),
                    ),
                ]
            )
        )

    # Complementos ficam guardados até o pedido ser enviado ao carrinho.
    for complemento in complementos:
        page.add(
            ft.Row(
                [
                    ft.Text(complemento),
                    ft.ElevatedButton(
                        "Escolher",
                        on_click=lambda _, complemento=complemento: selecionar_complemento(complemento),
                    ),
                ]
            )
        )


ft.run(main)
