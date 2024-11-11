import flet as ft
import sqlite3

#Funcicon para Obtener los datos de la base de datos
def obtenerDatos():
    #Paso 1. Conectar a la base de dato o crear
    conexion=sqlite3.connect('datos.db')
    #Paso 2. Crear el cursor para las consultas sql
    cursor=conexion.cursor()
    #Paso 3. Ejecutar la consulta SQL (SELECT * FROM usuarios)
    cursor.execute("SELECT nombre,edad,celular FROM usuarios")
    #Paso 3.1. Obtener los datos
    usuarios=cursor.fetchall()
    return usuarios

def mostrarPantalla1():
    #LLamar a los datos Obtenidos
    usuarios=obtenerDatos()

    #Lista de datos en las CARDSVIEWS 
    usuariosCards=[
        ft.ResponsiveRow(
            [
                ft.Container(
                    padding=10,
                    content=ft.Card(
                        content=ft.Container(
                            padding=10,
                            content=ft.Column(
                                [
                                    ft.Text(value=usuario[0],size=22),
                                    ft.CupertinoRadio(label=usuario[1]),
                                    ft.CupertinoFilledButton(text=usuario[2])

                                ]
                            ),
                        ),
                    ),
                )
            ],
            #Columnas por tamaño de pantallas xs md lg
            col={"xs":6,"md":3,"lg":3,} #2Columnas para pantallas pequeñas y 4 columnas para pantallas medianas y grades 
        )
        for usuario in usuarios
    ]
    return ft.Container(
        alignment=ft.alignment.top_center,
        content=ft.Column([
            ft.Text(value="Pantalla de obtenecion de datos"),
            ft.ResponsiveRow(usuariosCards,spacing=10)
        ],
        alignment="center"
            
        ),
    )