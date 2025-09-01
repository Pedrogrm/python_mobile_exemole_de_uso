
import flet as ft

def main(page: ft.Page):
    page.title = "Meu primeiro Botão"
    page.padding = 20

    # Criando um texto que será modificado pelo botão
    mensagem = ft.Text(
        value="Clique no Botão abaixo! 👇",
        size=20,
        text_align=ft.TextAlign.CENTER
    )

    def botao_clicado(evento):
        """
        Esta função será executada sempre que o botão for clicado.
        O parâmetro 'evento contém informações sobre o clique.
        """
        # Mudando o texto da mensagem
        mensagem.value = "🎉 Parabéns! Você clicou no botão!"
        mensagem.color = ft.Colors.GREEN

        # IMPORTANTE: Sempre que modificamos elementos da interface,
        # precisamos chamar page.update() para que as mudaças apareçam na tela
        page.update()

    # Criando nosso botão
    meu_botao = ft.ElevatedButton(
        text="Clique em mim!",
        on_click=botao_clicado,
        width=200,
        height=50,
        # bgcolor=ft.Colors.BLUE, # cor de fundo do botão
        color="#4caf50", # cor das letras do botao
        bgcolor=ft.Colors.BLACK # cor com hexadecimal fundo do botão
    )

    # Adicionando os elementos à página
    page.add(mensagem)
    page.add(meu_botao)

ft.app(target=main)