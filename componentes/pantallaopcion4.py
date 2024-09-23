#Importar flet
import flet as ft
#funcion para mostrar el contenido de la pantalla 4
def mostrarPantalla4():
    return ft.Container(
        alignment=ft.alignment.top_left,
        content=(ft.TextField(value="Entrada de texto de Prueba"))
    )