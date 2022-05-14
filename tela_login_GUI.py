from PySimpleGUI import PySimpleGUI as sg

# layout
sg.theme("Reddit")
layout = [
    [sg.Text("Usuário: "), sg.Input(key = "usuario", size=(25,1), )],
    [sg.Text("Senha: "), sg.Input(key = "senha", password_char="*", size=(25,1))],
    [sg.Checkbox("Salvar o Login? ")],
    [sg.Button("Entrar")]
]
# janela
window = sg.Window("Tela de Login", layout)

# ler eventos
while True:
    events, values = window.read()
    if events == sg.WINDOW_CLOSED:
        break
    if events == "Entrar":
        if values["usuario"] == "Enzo" and values["senha"] == "123456":
            print("Bem Vindo Enzo")
