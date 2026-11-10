import flet as ft
from UI.view import View
from model.modello import Model



class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # Preparo Anni per la tendina
        self._years = self._model.getAllYears()
        #Preparo forme per tendina
        self._years = self._model.getAllShapes()


    def fillddyear(self):
        years = self._model.getAllYears()
        self._view.ddyear.options.clear()

        for year in years:
            self._view.ddyear.options.append(
                ft.dropdown.Option(str(year))
            )

        self._view.update_page()

    def fillddshape(self):
        shapes = self._model.getAllShapes()
        self._view.ddshape.options.clear()

        for shape in shapes:
            self._view.ddshape.options.append(
                ft.dropdown.Option(str(shape))
            )
        self._view.update_page()

    def handle_graph(self, e):
        # Leggo il valore selezionato
        year = self._view.ddyear.value

        # Controllo che sia stato selezionato
        if year is None:
            self._view.txt_result1.controls.clear()
            self._view.txt_result1.controls.append(
                ft.Text("Seleziona un anno!")
            )
            self._view.update_page()
            return

        # Leggo il valore selezionato
        shape = self._view.ddshape.value

        # Controllo che sia stato selezionato
        if shape is None:
            self._view.txt_result1.controls.clear()
            self._view.txt_result1.controls.append(
                    ft.Text("Seleziona una forma!")
                )
            self._view.update_page()
            return

        #Costruisco il grafo
        self._model.buildGraph(int(year), str(shape))

        # Stampo nodi e archi
        self._view.txt_result1.controls.clear()
        self._view.txt_result1.controls.append(
            ft.Text(f"Numero nodi: {self._model.getNumNodes()}")
        )

        self._view.txt_result1.controls.append(
            ft.Text(f"Numero archi: {self._model.getNumEdges()}")
        )

        self._view.update_page()

    def handle_path(self, e):
        pass
