import flet as ft

def main(page: ft.Page):
    page.title = "Gestión de Eventos para la Comunidad Educativa"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = "auto"
    page.theme_mode = ft.ThemeMode.LIGHT

    # Lista para almacenar los eventos
    events = []

    # Función para agregar un evento
    def add_event(e):
        if not event_title.value or not event_description.value or not event_image_url.value:
            page.dialog = ft.AlertDialog(
                title=ft.Text("Error"),
                content=ft.Text("El título, la descripción y la URL de la imagen son obligatorios."),
                actions=[ft.TextButton("OK", on_click=lambda e: page.dialog.close())],
            )
            page.dialog.open = True
            page.update()
            return

        # Crear un nuevo Card para el evento
        new_event = ft.Card(
            content=ft.Column(
                [
                    ft.Image(src=event_image_url.value, height=150, fit="cover"),
                    ft.ListTile(
                        title=ft.Text(event_title.value, weight="bold"),
                        subtitle=ft.Text(event_description.value),
                    ),
                    ft.Row(
                        [ft.ElevatedButton("Eliminar", on_click=lambda e: remove_event(new_event))],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ],
                spacing=10,
                tight=True
            ),
            elevation=5,
        )

        # Agregar el evento a la lista y actualizar la página
        events_list.controls.append(new_event)
        events.append(new_event)
        event_title.value = ""
        event_description.value = ""
        event_image_url.value = ""
        page.update()

    # Función para eliminar un evento
    def remove_event(event):
        events_list.controls.remove(event)
        events.remove(event)
        page.update()

    # Campos de entrada para el título, la descripción y la URL de la imagen del evento
    event_title = ft.TextField(label="Título del Evento", width=300)
    event_description = ft.TextField(label="Descripción del Evento", width=300)
    event_image_url = ft.TextField(label="URL de la Imagen del Evento", width=300)

    # Botón para agregar evento
    add_event_button = ft.ElevatedButton("Agregar Evento", on_click=add_event)

    # Lista para mostrar los eventos como tarjetas
    events_list = ft.Column(spacing=10, expand=True)

    # Barra de navegación (AppBar)
    page.appbar = ft.AppBar(
        title=ft.Text("Gestión de Eventos"),
        center_title=True,
        bgcolor=ft.colors.BLUE,
        actions=[
            ft.IconButton(ft.icons.HOME, on_click=lambda e: page.go('/')),
            ft.IconButton(ft.icons.EVENT, on_click=lambda e: page.go('/eventos')),
        ],
    )

    # Contenido principal
    main_content = ft.Column(
        [
            ft.Text("Agregar Nuevo Evento", style="headlineSmall"),
            event_title,
            event_description,
            event_image_url,
            add_event_button,
            ft.Divider(),
            ft.Text("Lista de Eventos", style="headlineSmall"),
            events_list,
        ],
        tight=True
    )

    # Agregar el contenido principal a la página
    page.add(main_content)

# Ejecutar la aplicación
ft.app(target=main)
