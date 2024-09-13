#PROJECT 00 - COUNTER

import flet as ft


def main(page: ft.Page):
    page.title = 'Counter'
    #page.bgcolor = ft.colors.BLUE_300
    #page.window.height = 750
    #page.window.width = 400
    #page.window.maximizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = 'light'
    

    text_number = ft.TextField(value='0', text_align=ft.TextAlign.CENTER, width=100)

    def minus_click(e):
        text_number.value = str(int(text_number.value) - 1)#1º TRANSFORMA A VARIAVEL EM INT E DEPOIS TRANFORMA EM STR DE NOVO
        text_number.update()#ATUALIZA A VARIÁVEL TEXT_NUMBER, FUNCIONA COMO page.update()

    def plus_click(e):
        text_number.value = str(int(text_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.REMOVE, on_click=minus_click),
                text_number,
                ft.IconButton(icon=ft.icons.ADD, on_click=plus_click)
            ],
            alignment=ft.MainAxisAlignment.CENTER #ALINHA OS ITENS DA ROW
        )
    )
    page.update()

    


ft.app(target=main)