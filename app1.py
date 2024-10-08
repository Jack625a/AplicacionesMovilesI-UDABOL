import flet as ft 

#Funcion Principal
def main(page):
    #Funcion para mostrar una alerta
    def mostrarAlerta(e):
        page.dialog=ft.AlertDialog(
            title=ft.Text("Bienvenido"),
            on_dismiss=lambda e:
            print("Pantalla emergente cerrada")
            )
        page.dialog.open=True
        page.update()

    #Agregar Imagen
    imagen=ft.Image(
        src="https://habrastorage.org/webt/4m/3k/qh/4m3kqhpn2-xb59x_v58sxmyioki.png",
        width=300,
        height=200,
        border_radius=20      
        )

    #Crear el boton para mostrar la funcion 
    boton=ft.CupertinoFilledButton(
        text="Mostrar Mensaje",
        on_click=mostrarAlerta
    )

    #Entradad de datos
    nombre=ft.TextField(label="Ingrese su nombre")
    celular=ft.TextField(label="Ingrese su celular")
    

    #Agregar el componente a la aplicacion
    page.add(imagen,nombre,celular,boton)

ft.app(target=main)

