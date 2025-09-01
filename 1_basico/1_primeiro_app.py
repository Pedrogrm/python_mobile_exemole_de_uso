import flet as ft

def main(page: ft.Page):
    """
    Função principal que será executada quando o app iniciar. O parâmero 'page' representa a tela/página do nosso app.
    """

    # Configurações basicas da pagina
    page.title = "Meu primeiro App Flet" # Título que aparece na aba do navegador
    page.padding = 20 # Espaçamento interno da página

    # Criando nosso primeiro elemento: um textocls
    meu_textob= ft.Text(
        value="🎉 Hello world! (Primeiro app com Flet!)", # O texto que será exibido
        size=24, # Tamanho da fonte
        color=ft.Colors.BLUE, # Cor do texto
        weighy=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER # Centralizar o texto
    )

    # Adicionando o texto à nossa página
    page.add(
        ft.Text("Bem-Vindoao mundo do desenvolvimento mobile!", size=16),
        ft.Text("Com Flet, você pode criar apps incriveis!📱", size=16, color=ft.Colors.GREEN)
    )

    ft.app(target=main) 