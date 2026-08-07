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

    page.add(
        ft.Text(
            "🍧 Açaí Flow",
            size=28,
            weight=ft.FontWeight.BOLD,
        )
    )

    for produto in produtos:
        page.add(
            ft.Text(produto),
            ft.ElevatedButton(
                "Adicionar",
                on_click=lambda e: carrinho.append(produto)
            )
        )