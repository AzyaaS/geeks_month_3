import flet as ft


def main(page: ft.Page):
    page.title = 'Мое первое приложение!'
    page.theme_mode = ft.ThemeMode.LIGHT

    text_hello = ft.Text("Привет, Группа 66-1!", size=24)

    text_button = ft.TextButton('SEND')
    elavated_button = ft.ElevatedButton('SEND')
    icon_button = ft.IconButton(icon=ft.Icons.SEND)

    name_input = ft.TextField(label="Введите имя")

    page.add(
        text_hello,
        name_input,
        text_button, 
        elavated_button, 
        icon_button, 
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER)