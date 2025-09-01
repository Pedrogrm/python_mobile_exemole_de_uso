import flet as ft

def main(page: ft.Page):
    page.title = "Campo de Texto"
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)
    
    # Criando um campo onde o usuario pode digitar
    campo_nome = ft.TextField(
        label="Digite seu nome aqui",
        width=300,
        border_color=ft.Colors.BLUE
    )

    # Texto que mostrará a resposta
    resposta = ft.Text(
        Value="", # Inicialmente vazio
        size=18,
        text_align=ft.TextAlign.CENTER,
    )

    def processar_nome(evento):
        """
        Função que pega o texto digitado pelo usuario e faz algo com ele
        """
        #pegando o valor digitado no campo
        nome_digitado = campo_nome.value

        # Verificando se o usuario realmente digitou algo
        if nome_digitado == "" or nome_digitado is None:
            resposta.value = "⚠️ Por favor, digite seu nome!"
            resposta.color = ft.Colors.RED
        elif len(nome_digitado) < 2:
            resposta.value = "⚠️ Nome muito curto!"
            resposta.color = ft.Colors.ORANGE
        else:
            resposta.value = f"✅ Olá, {nome_digitado}! Prazer em conhecê-lo(a)!"
            resposta.color = ft.Colors.GREEN

        # Atualizando a interface
        page.update()

    # Botao para processar o nome
    botao_ok = ft.ElevatedButtom(

    )

ft.app(target=main)
    