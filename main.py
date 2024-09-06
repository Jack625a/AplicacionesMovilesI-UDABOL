#importar flet
import flet as ft

def main(page):
   page.add(
      ft.ElevatedButton(
         text="Boton de Prueba",
         on_click= lambda e:print ("Se hizo click en el boton"),
         bgcolor='green',
         color='white',
        

         )
   )

   
ft.app(target=main)