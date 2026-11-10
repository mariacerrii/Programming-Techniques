import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        # Preparo Album per la tendina
        self._albums = self._model.getAllAlbums()


    def handleCreaGrafo(self, e):
        # Costruisco il grafo
        self._model.buildGraph()

        # Pulisco i risultati precedenti
        self._view._txt_result.controls.clear()

        # Stampo le informazioni
        self._view._txt_result.controls.append(
            ft.Text("Grafo correttamente creato")
        )

        self._view._txt_result.controls.append(
            ft.Text(f"Numero nodi: {self._model.getNumNodes()}")
        )

        self._view._txt_result.controls.append(
            ft.Text(f"Numero archi: {self._model.getNumEdges()}")
        )

        self.fill_ddAlbum()

        self._view.update_page()

    def fill_ddAlbum(self):
        albums = self._model.getAllAlbums()
        self._view._ddAlbum.options.clear()

        for album in albums:
            self._view._ddAlbum.options.append(
                ft.dropdown.Option(str(album))
            )

        self._view.update_page()

    def handleStampaInfo(self,e):
        numero, album = self._model.getInfoComponenti()

        self._view._txt_result.controls.clear()

        # Numero totale componenti
        self._view._txt_result.controls.append(
            ft.Text(f"Numero componenti connesse: {numero}")
        )

        # Dimensione componente maggiore
        self._view._txt_result.controls.append(
            ft.Text(f"Componente maggiore: {len(album)} album")
        )

        # Dettagli degli album in ordine alfabetico
        for a in album:
            self._view._txt_result.controls.append(
                ft.Text(
                    f"Album: {a.Title} | "
                    f"Numero brani: {len(a.tracks)}"
                )
            )
        self._view.update_page()

    def handleSelezione(self,e):
        pass