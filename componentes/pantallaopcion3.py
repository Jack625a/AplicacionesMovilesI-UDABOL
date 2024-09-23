import flet as ft

#funcion para crear el contenido de la pantalla 3
def mostrarPantalla3():
    return ft.Container(
        alignment=ft.alignment.bottom_center,
        content=(ft.CupertinoButton(text="boton pantalla 3", icon=ft.icons.FACE, )
                 )
    )
