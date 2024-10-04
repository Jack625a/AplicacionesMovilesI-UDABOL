import flet as ft


def main(page: ft.Page):
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
        ]
    )
    page.add(

        ft.Row([
            navegacion,ft.VerticalDivider(width=1),
            ft.Column([
                       ft.Text(value="Pantalla 1",size=50),
                       ft.Image(src='https://avatars.githubusercontent.com/u/102273996?s=280&v=4'),
                       ft.CupertinoButton(text='Boton de Prueba')
                       ],
                      alignment=ft.MainAxisAlignment.START,
                      expand=True
                      )
        ],expand=True
        )
    )

ft.app(main)
