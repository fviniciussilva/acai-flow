import flet as ft

carrinho = []

produtos = [
    "Açaí 300ml",
    "Açaí 500ml",
    "Açaí 700ml",
    "Açaí 2 litros"
]


def main(page: ft.Page):

    page.title = "Açaí Flow"

    texto_carrinho = ft.Text("Carrinho vazio")


    def adicionar_ao_carrinho(produto):

        carrinho.append(produto)

        texto_carrinho.value = f"Itens no carrinho: {len(carrinho)}"

        page.update()


    page.add(
        ft.Text(
            "🍧 Açaí Flow",
            size=28,
            weight=ft.FontWeight.BOLD,
        )
    )


    page.add(texto_carrinho)


    for produto in produtos:

        page.add(
            ft.Text(produto),

            ft.ElevatedButton(
                "Adicionar",
                on_click=lambda e, produto=produto: adicionar_ao_carrinho(produto)
            )
        )


ft.run(main)