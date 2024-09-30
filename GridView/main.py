import flet as ft

def main(page: ft.Page):
    #Configurarcion de la aplicacion
    page.title="Aplicacion GridView"
    #Tema de la aplicacion
    page.theme_mode=ft.ThemeMode.DARK
    page.padding=10
    #Enviamos la actualizacion - Aplicar los cambios a la aplicacion
    

    page.add(ft.Text(value="Aplicacion Prueba GridView Imagenes",size=20))

    #Paso1. Crear el contenido del gridView (Filas=rows, Columnas=columns)
    imagenes=ft.GridView(
        #Propiedades del gridView
        #Espacio para ocupar el gridview
        expand=1,
        #Maximo de Columnas para vizualizar 
        runs_count=4,
        max_extent=300,
        #horizontal=True
        #Espaciado de contenidos
        spacing=15,
        run_spacing=15,
    )
    #Paso2. Añadir el componente a la aplicacion
    page.add(imagenes)

    #Paso 3. Agregar las imagenes al GridView - 100
    for i in range(50):
        imagenes.controls.append(
            #Añadir las imagenes
            ft.Image(
                src=f"https://picsum.photos/300/300?{i}",
                border_radius=ft.border_radius.all(20),
                     
                     
                ) #Enviar la solicitud a la API y devolver las imagenes con su id
        )

    #aCTUALIZAR LA PAGINA
    page.update()
ft.app(main)
