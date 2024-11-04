import flet as ft
#Importar firebase
import firebase_admin
from firebase_admin import credentials, auth
import webbrowser


#Paso 2. Inicializar Firebase con el archivo de las credenciales
cred = credentials.Certificate("service_account.json")
firebase_admin.initialize_app(cred)

#Paso 3. Variables de configuracion de Firebase Autentificacion con Google
firebse_auth_url="https://accounts.google.com/o/oauth2/auth"
client_id= ""
redirect_uri="http://127.0.0.1:49240/"
scope="https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile openid"

#Paso 4. Crear una funcion para realizar la autentificacion con Firebase
def autentificacionFirebase(id_token):
    try:
        decodificador_token=auth.verify_id_token(id_token)
        return decodificador_token
    except Exception as e:
        print("Error al verificar el token de acceso", e)
        return None

#Funcion para seleccionar Google como servicio de autentificacion
def iniciarConGoole():
    #Armar la url de solicitud
    auth_url=f"{firebse_auth_url}?cliente_id={client_id}&redirect_uri={redirect_uri}&scope={scope}&response_type=token"
    webbrowser.open(auth_url)



#Paso 5 Configurar la interfaz
def main(page: ft.Page):
    page.title="Inicio de Sesión"
    

    #Crear la funcion para manejar el evento del click en boton (CONTINUAR CON GOOGLE)
    def loginGoogle(e):
        iniciarConGoole()
        page.update()
    
    #bOTON PARA INICAR SESION
    botonGoogle=ft.CupertinoFilledButton(text="Continuar con Google",on_click=loginGoogle)

    page.add(botonGoogle)


ft.app(main)
