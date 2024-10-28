import flet as ft

def main(page: ft.Page):
    
    #fUNCION PARA MANEJAR EL CAMBIO DE RUTA 
    #RUTA inicio -- productos -- configuracion
    def rutas(route):
        #Limpiamos las vistas del contenedor
        page.views.clear()
        #Configuracion del ruta inicial
        if page.route=="/":
            page.views.append(
                ft.View(
                    "/",
                    controls=[
                        ft.AppBar(title="Pantalla Inicio"),
                        ft.Text(value="Pantalla Inicio"),
                        ft.Image(src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/640px-Python.svg.png"),
                        ft.CupertinoFilledButton(text="IR PANTALLA 2", on_click=lambda _:page.go("/productos"))
                    ],
                )
            )
        elif page.route=="/productos":
            ft.View(
                "/productos",
                controls=[
                    ft.AppBar(title="Pantalla Productos"),
                    ft.Text(value="Pantalla Productos"),
                    ft.CupertinoFilledButton(text="Volver al Inicio", on_click=lambda _:page.go("/")),
                    ft.CupertinoFilledButton(text="ir Pntalla configuracion", on_click=lambda _:page.go("/configuraciones"))
                ],
            )
        
        elif page.route=="/configuracion":
            ft.View(
                "/configuracion",
                controls=[
                    ft.AppBar(title="Pantalla Configuraciones"),
                    ft.Text(value="Pantalla Configuraciones"),
                    ft.CupertinoFilledButton(text="Volver al Inicio", on_click=lambda _:page.go("/"))
                ],
            )

        page.update()

    #funcion para controlar el boton atras
    def botonAtras(view):
        page.views.pop()
        viewPrincipal=page.views[-1]
        page.go(viewPrincipal.route)

    
    #Configuracion de los eventos
    page.on_route_change=rutas #manejio de rutas
    page.on_view_pop=botonAtras #Manejo del boton atras
    page.go(page.route)


ft.app(main)
