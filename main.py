import flet as ft


def main(page: ft.Page):
    page.title = 'Мое первое приложение!'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    greeting_history = []
    favorite_names = []

    count = 0
    
    greeting_text = ft.Text("История приветствий")
    favorite_names_text = ft.Text("Любимые имена: \n")
    click_count_text = ft.Text(f"количество нажатий кнопки SEND: {count}")
    access_age_text = ft.Text(value="",size=25)

    def text_name(e):   # e - event
        name = text_input.value.strip()

        if name:
            
            text_hello.value = f"Добро пожаловать! {text_input.value}"
            text_hello.color = ft.Colors.GREEN_900
            text_input.value = ""
            greeting_history.append(name)
            if len(greeting_history) > 5:
                greeting_history.pop(0) 
                
            print(greeting_history)
            greeting_text.value = f"История приветствий: \n" + "\n".join(greeting_history)

        else:
            text_hello.value = f"Поле ввода имени не заполнено!"
            text_hello.color = ft.Colors.RED_900
        click_count() 
        page.update()

    
    text_hello = ft.Text('Hello', size=25)
    text_input = ft.TextField(label="Введите свое имя", on_submit=text_name, expand=False)
    btn = ft.ElevatedButton('SEND', on_click=text_name)
    


    def clear_history():
        greeting_history.clear()
        greeting_text.value = f"История приветствий: "
        page.update()

    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)
    
    def add_favorites_name(e):
        if greeting_history: 
            last_name = greeting_history[-1]
            if last_name not in favorite_names: 
                favorite_names.append(last_name)  
                favorite_names_text.value = f"Любимые имена: \n" + "\n".join(favorite_names)
                page.update()

    favorite_name_button = ft.ElevatedButton('Добавить в избранное', on_click=add_favorites_name)
    
    def click_count():
        nonlocal count
        count += 1
        click_count_text.value = f"количество нажатий кнопки SEND: {count}"
        page.update()

    def thememode(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
    def check_age(e):
        age = text_age_input.value.strip()

        if age.isdigit():
            age_number = int(age)
            if age_number >= 18:
                access_age_text.value = "Доступ разрешен"
                access_age_text.color = ft.Colors.GREEN
            else:
                access_age_text.value = "Доступ запрещен"
                access_age_text.color = ft.Colors.RED
        else:
            access_age_text.value = "Введите корректный возраст"
            access_age_text.color = ft.Colors.YELLOW
        text_age_input.value = ""
        page.update()
    age_send_button = ft.IconButton(icon=ft.Icons.SEND, on_click=check_age)
    text_age_input = ft.TextField(label="Введите свой возраст", on_submit=check_age)
    

    theme_btn = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=thememode)

    main_object = ft.Row(
        controls=[text_input,btn,clear_button,favorite_name_button], 
        alignment=ft.MainAxisAlignment.CENTER)
    text_row = ft.Row(
        controls=[text_hello,],
        alignment=ft.MainAxisAlignment.CENTER
    )
    age_acces_row = ft.Row(
        controls=[access_age_text],
        alignment=ft.MainAxisAlignment.CENTER
    )
    age_row = ft.Row(
        controls= [text_age_input,age_send_button],
        alignment=ft.MainAxisAlignment.CENTER
    )
    page.add(text_row, age_acces_row, main_object, age_row, theme_btn, greeting_text,favorite_names_text, click_count_text )

ft.app(target=main, view=ft.AppView.WEB_BROWSER)