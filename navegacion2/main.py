import flet as ft


def main(page: ft.Page):

    #Crea la funcion para mostrar el contenido de cada opcion 
    def contenidoNavegacion(index):
        if index==0:
            contenido.controls=[
                ft.Text(value="Pantalla 1",size=50),
                       ft.Image(src='https://avatars.githubusercontent.com/u/102273996?s=280&v=4'),
                       ft.CupertinoButton(text='Boton de Prueba')
                       ]
        elif index==1:
            contenido.controls=[
                ft.Text(value="Pantalla Productos",size=40),
                ft.Image(src='https://lavozdetarija.com/wp-content/uploads/2022/01/Celulares-Realme-8-5G.jpg',width=250)
            ]
        elif index==2:
            contenido.controls=[
                ft.Text(value="Pantalla Carrito Compras", size=40),
                ft.Image(src='https://cdn-icons-png.flaticon.com/512/8146/8146003.png')
            ]
        elif index==3:
            contenido.controls=[
                ft.Text(value="Pantalla de Perfil", size=35)
            ]
        contenido.update()

    #Actualizar la aplicacion con los nuevo cAMBIOS
    navegacion=ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=250,
        leading=ft.Image(
            src='https://avatars.githubusercontent.com/u/102273996?s=280&v=4',
            width=100),
            
        destinations=[
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.HOME_SHARP),
                selected_icon_content=ft.Icon(ft.icons.STOREFRONT),
                label='Inicio',
                padding=10
          
                ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.HOME_SHARP),
                selected_icon_content=ft.Icon(ft.icons.STOREFRONT),
                label='Productos',
                padding=10
          
                ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.HOME_SHARP),
                selected_icon_content=ft.Icon(ft.icons.STOREFRONT),
                label='Carrito de Compras',
                padding=10
          
                ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.HOME_SHARP),
                selected_icon_content=ft.Icon(ft.icons.STOREFRONT),
                label='Perfil',
                padding=10
          
                )
            
        
        ],
        # Metodo para el cambio de opcion
        on_change=lambda evento:contenidoNavegacion(evento.control.selected_index)
    )

    #Crear contenedor para cada contenido de las opciones de la navegacion
    contenido=ft.Column(
        [
        ft.Text(value="Pantalla 1",size=50),
                       ft.Image(src='https://avatars.githubusercontent.com/u/102273996?s=280&v=4'),
                       ft.CupertinoButton(text='Boton de Prueba')
                       ],
                      alignment=ft.MainAxisAlignment.START,
                      expand=True
    )

    #aÑADIR LOS COMPONENTES A LA APLICACION
    
    page.add(
        ft.Row([
            navegacion, ft.VerticalDivider(width=1),contenido
        ],expand=True)

    )

ft.app(main)
