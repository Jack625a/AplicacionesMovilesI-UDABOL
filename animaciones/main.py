import flet as ft


def main(page: ft.Page):
    page.add(
        #Paso 1. Obtener el componente LOTTIES

        ft.Column(
            [
                ft.Text(value='Mi Aplicacion', size=50, weight=ft.FontWeight.BOLD),
                ft.Lottie(src='https://lottie.host/f4135d49-3125-41c6-bde9-59f67ca78727/stla81bKKV.json',
                  repeat=True,
                  reverse=True,
                  width=550,
                  height=550
                  ),
                  ft.Lottie(src='https://lottie.host/977675af-fa83-48eb-a453-d63ba5b3d886/joIyN7jYMe.json')
            ], alignment=ft.MainAxisAlignment.CENTER,
            
        )
        

    )


ft.app(main)
