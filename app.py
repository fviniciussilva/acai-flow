import flet as ft


def main(page: ft.Page):
    page.title = "Açaí Flow"

    produtos = [
        {
            "nome": "Açaí 300ml",
            "preco": 21.90,
        },
        {
            "nome": "Açaí 500ml",
            "preco": 31.90,
        },
    ]

    page.add(
        ft.Text(
            "🍧 Açaí Flow",
            size=28,
            weight=ft.FontWeight.BOLD,
        )
    )

    for produto in produtos:
        page.add(
            ft.Text(
                f"{produto['nome']} - R$ {produto['preco']:.2f}"
            )
        )
        page.update()