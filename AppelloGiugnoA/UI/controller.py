import flet as ft
from model import customer

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        # Preparo i Paesi per la tendina
        self._countries = self._model.getAllCountries()

    def fillDDCountry(self):
        #AL PLURALE QUA!!!
        countries = self._model.getAllCountries()
        for c in countries:
            self._view._ddCountry.options.append(ft.dropdown.Option(c))
        self._view.update_page()


    #con selezione a tendina
    def handleCreaGrafo(self, e):
        self._view._txt_result.controls.clear()

        country = self._view._ddCountry.value

        if country is None:
            self._view.create_alert("Selezionare un paese.")
            return

        try:
            self._model.buildGraph(country)
            self._view._txt_result.controls.append(
                ft.Text("Grafo correttamente creato.")
            )
            self._view._txt_result.controls.append(
                ft.Text(f"Numero nodi: {self._model.getNumNodes()}")
            )

            self._view._txt_result.controls.append(
                ft.Text(f"Numero archi: {self._model.getNumEdges()}")
            )
            self._view.update_page()

        except Exception as ex:
            self._view.create_alert(f"Errore nella creazione del grafo: {ex}")

    def handleStampaInfo(self,e):
        pass

    def handleSequenza(self,e):
        pass