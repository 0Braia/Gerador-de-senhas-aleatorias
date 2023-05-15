import PySimpleGUI as sg
import pyperclip as pp

sg.theme('Dark Grey 13')

layout = [
    [sg.Stretch(), sg.Text("GERADOR DE SENHAS AUTOMÁTICO"), sg.Stretch()],
    [sg.Stretch(), sg.Text("################", key="nova"), sg.Stretch()],
    [sg.Button("Gerar nova senha", size=(15, 2)), sg.Button("Copiar senha", size=(15, 2)), sg.Button("Finalizar", size=(15, 2))],
    [sg.Text("By Dev FullStack 0.Braia", size=(45, 1))],
]

janela = sg.Window("GERADOR DE SENHAS AUTOMÁTICO", layout)

# Gerador de senhas com 16 caracteres diferentes aleatórios.
def gera_senha():
    from random import choice

    letras_maiusculas = 'QWERTYUIOPASDFGHJKLZXCVBNMÇ'
    letras_minusculas = 'qwertyuiopasdfghjklzxcvbnmç'
    numeros = '0123456789'
    caracter_especial = '!@#$%&?'

    senha = ''
    senha_final = []

    while len(senha_final)<18:
        senha = choice(choice(letras_maiusculas) + choice(letras_minusculas) + choice(numeros) + choice(caracter_especial))
        senha_final.append(senha)
        if len(senha_final) == 17:
            break
    
    return (senha_final[0]+senha_final[1]+senha_final[2]+senha_final[3]+senha_final[4]+senha_final[5]+senha_final[6]+senha_final[7]+senha_final[8]+senha_final[9]+senha_final[10]+senha_final[11]+senha_final[12]+senha_final[13]+senha_final[14]+senha_final[15])
       
cont = 0
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED or eventos == 'Finalizar':
        break
    if eventos == 'Gerar nova senha':
        novo = gera_senha()
        cont = 1
        janela['nova'].update(f'{novo}')
    if eventos == 'Copiar senha':
        if cont == 0:
            sg.popup_ok('ERRO !! O sistema ainda não calculou nova senha.')
        if cont == 1:
            pp.copy(novo)

janela.close()
