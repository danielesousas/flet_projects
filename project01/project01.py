import flet as ft
#Breakpoint     Dimension
#xs             <576px
#sm             >=576px
#md             >=768px
#lg             >=992px
#xl             >=1200px
#xxl            >=1400px


def main(page: ft.Page):
    page.bgcolor = ft.colors.BROWN_600

    victim = ft.Image(
        data = 0,
        src = 'images/hangman_0.png',
        repeat = ft.ImageRepeat.NO_REPEAT,
        height= 300, 
    )


    word = ft.Container()

    game = ft.Container(
        col={'xs': 12, 'lg': 6},
        padding=ft.padding.all(50),
        content=ft.Column(
            controls=[
                victim,
                word
            ]
        )
    )

    keyboard = ft.Container(
        col={'xs': 12, 'lg': 6}
    )

    scene = ft.Image(col=12, src = 'images/scene.png')

    layout = ft.ResponsiveRow(
        columns=12,#POR PADRAO A RESPONSIVEROW VEM C/ TAMANHO DE COLUNA 12, PODENDO SER ALTERADA
        controls=[
            scene,
            game,
            keyboard,
            scene,
        ]
    )
    
    page.add(layout)

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')