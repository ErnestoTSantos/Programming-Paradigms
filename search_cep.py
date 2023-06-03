import PySimpleGUI as sg
import requests


class SearchCPF:
    def request(cep) -> str:
        request = requests.get(f"https://brasilapi.com.br/api/cep/v2/{cep}")

        return request


class Searching:
    def __init__(self) -> None:
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

        self.window = sg.Window("Window", layout)

    def search_cpf(self):
        while True:
            events, values = self.window.read()
            cep = values["CEP"]
            if events == sg.WINDOW_CLOSED:
                break
            elif events == "Encontrar":
                print(self._get_cep(cep))

    def _get_cep(self, cep):
        search = SearchCPF
        request_cep = search.request(cep)
        if request_cep.status_code == 200:
            data = request_cep.json()
            del data["location"]
            del data["service"]
            return data
        return "Informações inválidas"


get_informations = Searching()
get_informations.search_cpf()
