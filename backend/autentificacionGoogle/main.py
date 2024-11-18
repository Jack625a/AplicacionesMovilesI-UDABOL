import flet as ft
#Importacion del proveedor del servicio (Google)
from flet.auth.providers import GoogleOAuthProvider

clienteID=""
clienteSecret=""

def main(page: ft.Page):

    #Variable para definir el proveedor
    provider=GoogleOAuthProvider(
        client_id=clienteID,
        client_secret=clienteSecret,
        redirect_url="http://localhost:8550/api/oauth/redirect"
    )
    resultadoSolicitud=ft.Column()

    #fUNCION CUANDO SE OBTIENE LOS DATOS
    def loginActivo(e):
        print(page.auth.user)

        resultadoSolicitud.controls.append(
            ft.Column([
                ft.Text(f"Nombre: {page.auth.user['name']}"),
                ft.Text(f"Correo: {page.auth.user['email']}")
            ])
        )
        page.update()
    
    #Mostrar los datos de la sesion
    page.on_login=loginActivo

    #Funcion para manejar el inicio de sesion
    def loginGoogle(e):
        page.login(provider)   
    page.add(
        ft.Column(
            [
               ft.Text(value="Inicio de Sesión", size=30),
               ft.CupertinoFilledButton(text="Iniciar sesión con Google",icon=ft.icons.EMAIL, on_click=loginGoogle),
               resultadoSolicitud
            ]
        )
    )


ft.app(main, port=8550)
