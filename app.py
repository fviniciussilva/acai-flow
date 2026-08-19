import flet as ft

carrinho = []

complementos = [
    "Granola",
    "Leite condensado",
    "Sucrilhos",
    "Paçoca",
    "Leite em pó",
]

produtos = [
    "Açaí 300ml",
    "Açaí 500ml",
    "Açaí 700ml",
    "Açaí 2 litros",
]


def main(page: ft.Page):
    page.title = "Açaí Flow"

    texto_carrinho = ft.Text("Carrinho vazio")
    lista_carrinho = ft.Column()

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
        )
    )

    page.add(texto_carrinho)
    page.add(lista_carrinho)

    # Cria uma linha e um botão para cada produto.
    for produto in produtos:
        page.add(
            ft.Row(
                [
                    ft.Text(produto),
                    ft.ElevatedButton(
                        "Adicionar",
                        on_click=lambda _, produto=produto: adicionar_ao_carrinho(produto)
                    )
                ]
            )
        )

    # Complementos usam a mesma função porque também entram no carrinho.
    for complemento in complementos:
        page.add(
            ft.Row(
                [
                    ft.Text(complemento),
                    ft.ElevatedButton(
                        "Adicionar",
                        on_click=lambda _, complemento=complemento: adicionar_ao_carrinho(complemento)
                    )
                ]
            )
        )

ft.run(main)
