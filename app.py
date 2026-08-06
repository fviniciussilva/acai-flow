import flet as ft


def adicionar_ao_carrinho(e):
    print("Produto adicionado ao carrinho!")


def main(page: ft.Page):
    page.title = "Açaí Flow"

    page.add(
        ft.Text(
            "🍧 Açaí Flow",
            size=28,
            weight=ft.FontWeight.BOLD,
        )
    )

    page.add(
    ft.ElevatedButton(
    "Adicionar ao carrinho",
    on_click=adicionar_ao_carrinho,
    )
    )