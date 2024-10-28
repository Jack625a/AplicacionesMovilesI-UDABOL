import flet as ft

def screen2_view(page: ft.Page):
    def go_back(e):
        page.views.pop()
        page.update()

    page.views.append(ft.View(route="/screen2", controls=[
        ft.Text("Pantalla 2"),
        ft.ElevatedButton("Volver a la pantalla 1", on_click=go_back)
    ]))
    page.update()
