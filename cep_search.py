import PySimpleGUI as sg
import requests

sg.theme("Reddit")
layout = [
    [sg.Text(" " * 50), sg.Text("Encontra endereço", size=(40, 1))],
    [
        sg.Text("Digite o CEP: ", size=(30, 1)),
        sg.Input(key="CEP", size=(50, 1)),
    ],
    [sg.Button("Encontrar")],
    [sg.Output(size=(80, 5))],
]

window = sg.Window("Window", layout)

while True:

    events, values = window.read()
    cep = values["CEP"]
    if events == sg.WINDOW_CLOSED:
        break
    elif events == "Encontrar":
        request = requests.get(f"https://brasilapi.com.br/api/cep/v2/{cep}")
        if request.status_code == 200:
            data = request.json()
            del data["location"]
            del data["service"]
            print(data)
        else:
            print("Informações inválidas")
