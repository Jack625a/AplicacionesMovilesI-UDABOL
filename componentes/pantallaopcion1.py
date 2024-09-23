import flet as ft

def mostrarPantalla1():
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.Text(
            size=30,
            value="Pantalla1",
        )
    )