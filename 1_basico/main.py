import flet as ft 
from bd.connectiondb import DataBase

class AppToDo:
    def __init__(self, page: ft.Page):
        # inicializa o aplicativo com a página flet e configura as configurções iniciais
        self.page = page
        self.configurar_pagina()
        self.banco_dados = DataBase()
        self.usuario = None
        self.verificar_usuario()

    def configurar_pagina(self):
        # Configura as propriedades iniciais de página
        self.page.title = 'Aplicativo ToDo'
        self.page.window_width = 400
        self.page.window_height = 750
        self.page.vertical_alignment = ft.MainAxisAlignment.START
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.padding = 20
        self.definir_cores()

    def definir_cores(self):
        # Define o esquema de cores para o modo escuro
        self.cor = {
            'primaria': '#3498db' ,
            'secundaria': '#2ecc71' ,
            'fundo': '#121212',
            'texto': '#ffffff',
            'texto_secundario': '#b3b3b3',
            'destaque': '#e74c3c',
            'item_fundo': '#1e1e1e',
            'borda': '#333333',
            'checkbox': '#3498db',
            'botao': '#3498db',
        }

    def verificar_usuario(self):
        # Verifica se o usuario já foi definido, caso contrario, pede o nome
        if self.usuario is None:
            self.pedir_nome_usuario()
        else
            self.main()

    def pedir_nome_usuari
    # Cria e exibe o formulario para inserir seu nome