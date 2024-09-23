import flet as ft
from pantallaopcion1 import mostrarPantalla1
from pantallaopcion2 import mostrarPantalla2
from pantallaopcion3 import mostrarPantalla3
from pantallaopcion4 import mostrarPantalla4


def main(page: ft.Page):
   secciones=ft.Tabs(
      #Configuracion de propiedades
      selected_index=0,
      animation_duration=1000,
      tabs=[
         ft.Tab(
            text='Opcion 1',
            icon=ft.icons.HOME,
            content=ft.Container(
               alignment=ft.alignment.top_center,
               content=mostrarPantalla1()
               )

         ),
         ft.Tab(
            text='Opcion 2',
            icon=ft.icons.FACE,
            content=ft.Container(
               alignment=ft.alignment.center,
               content=mostrarPantalla2()
               
            )
         ),
         ft.Tab(
            text='Opcion 3',
            icon=ft.icons.LOCAL_GROCERY_STORE,
            content=ft.Container(
               alignment=ft.alignment.center,
               content=mostrarPantalla3()
            )
         ),
         ft.Tab(
            text='Opcion 4',
            icon=ft.icons.TIKTOK,
            content=ft.Container(
               alignment=ft.alignment.center,
               content=mostrarPantalla4()
               
            )
         )
      ],
      expand=1,

   )
   #Barra de navegacion inferior

   #Paso 1 crear la barra de navegacion inferior
   navegacionInferior=ft.NavigationBar(
      destinations=[
         ft.NavigationDestination(label='Inicio',icon=ft.icons.HOME_FILLED),
         ft.NavigationDestination(label="Productos",icon=ft.icons.STORE),
         ft.NavigationDestination(label='Servicios',icon=ft.icons.ELECTRICAL_SERVICES),
         ft.NavigationDestination(label='Perfil',icon=ft.icons.FACE,)
      ],
      bgcolor=ft.colors.YELLOW,
      indicator_color='red',
      animation_duration=3000,
      

   )
   #Agregar los contenidos

   page.add(secciones, navegacionInferior)

ft.app(main)

