import flet as ft


def main(page: ft.Page):
    #Datos locales para la creacion de la lista
    productos=[
        {
            "nombre":"Producto 1",
            "precio":"150 bs",
            "cantidad":10,
            "icono":'https://lavozdetarija.com/wp-content/uploads/2022/01/Celulares-Realme-8-5G.jpg',
            "imagen":ft.icons.SHOPPING_CART
        },
        {
            "nombre":"Producto 2",
            "precio":"250 bs",
            "cantidad":100,
            "icono":'https://lavozdetarija.com/wp-content/uploads/2022/01/Celulares-Realme-8-5G.jpg',
            "imagen":ft.icons.SHOPPING_CART
        },
        {
            "nombre":"Producto 3",
            "precio":"50 bs",
            "cantidad":10,
            "icono":'https://lavozdetarija.com/wp-content/uploads/2022/01/Celulares-Realme-8-5G.jpg',
            "imagen":ft.icons.SHOPPING_CART
        },
        {
            "nombre":"Producto 4",
            "precio":"150 bs",
            "cantidad":10,
            "icono":'https://lavozdetarija.com/wp-content/uploads/2022/01/Celulares-Realme-8-5G.jpg',
            "imagen":ft.icons.SHOPPING_CART
        },
        {
            "nombre":"Producto 5",
            "precio":"850 bs",
            "cantidad":10,
            "icono":'https://lavozdetarija.com/wp-content/uploads/2022/01/Celulares-Realme-8-5G.jpg',
            "imagen":ft.icons.ADD_SHOPPING_CART
        },
        {
            "nombre":"Producto 6",
            "precio":"650 bs",
            "cantidad":10,
            "icono":'https://lavozdetarija.com/wp-content/uploads/2022/01/Celulares-Realme-8-5G.jpg',
            "imagen":ft.icons.SHOPPING_CART
        }
    ]

    #metodo para crear la lista Cupertino
    def mostrarLista(evento):
        #Manejar el evento del click en cada producto
        producto=evento.control.data
        #Logica para el evento del click
        print (f"Producto seleccionado {producto['nombre']}")
    

    #Paso3. Ingresar los datos de la lista Productos al ListView Cupertino
    for producto in productos:
        page.add(
            ft.CupertinoListTile(
                additional_info=ft.Text(producto['cantidad']),
                title=ft.Text(f"{producto['nombre']}"),
                subtitle=ft.Text(f"{producto['precio']}"),
                trailing=ft.Icon(name=producto['imagen']),
                on_click=mostrarLista,
                data=producto,
                leading=ft.Image(src=producto['icono'],width=250,height=500)
            )
        )
    #Configuraciones finales
    page.title="Lista Cupertino"


ft.app(main)
