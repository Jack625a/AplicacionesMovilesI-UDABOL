import flet as ft


def main(page: ft.Page):

    #Configurar el WebView
    webView=ft.WebView(
        url='https://flet.dev/',
        javascript_enabled=True,

        )
    page.add(webView)


ft.app(main)
