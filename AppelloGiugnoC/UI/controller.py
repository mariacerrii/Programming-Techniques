import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

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

        # Se la tendina va popolata dopo la creazione:
        # self.fillDD()

        self._view.update_page()


    def handleStampaInfo(self,e):
        # PULISCO L'AREA DEI RISULTATI
        self._view._txt_result.controls.clear()

        # ____________________ GRADO MASSIMO ____________________
        # Recupero artista con il maggior numero di collegamenti
        bestArtist, degree = self._model.getMaxDegreeArtist()
        self._view._txt_result.controls.append(
            ft.Text(f"Artista con grado massimo: {bestArtist.Name}, grado: {degree}")
        )

        # ____________________ SOMMA PESI MASSIMA ____________________
        # Recupero artista con la somma dei pesi maggiore
        bestArtist, score = self._model.getBestArtist()
        self._view._txt_result.controls.append(
            ft.Text(f"Artista con somma pesi massima: {bestArtist.Name}, somma: {score}")
        )

        # ____________________ TOP 10 ARCHI ____________________
        # Recupero i 10 archi più pesanti
        topEdges = self._model.getTop10Edges()
        self._view._txt_result.controls.append(
            ft.Text("Top 10 archi:")
        )

        # Stampo gli archi con i rispettivi pesi
        for u, v, data in topEdges:
            self._view._txt_result.controls.append(
                ft.Text(f"{u.Name} - {v.Name}: {data['weight']}")
            )

        # AGGIORNO L'INTERFACCIA
        self._view.update_page()

    #RICORSIONE
    def handleSelezione(self,e):
        # 1. Leggo i parametri dalla VIEW
        valore = self._view.dd_artista.value
        # 2. Controllo che siano validi
        if valore is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text("Selezionare un nodo")
            )
            self._view.update_page()
            return

        # 3. Chiamo la ricorsione nel MODEL
        risultato = self._model.getBestPath(valore)
        # 4. Stampo il risultato
        self._view.txt_result.controls.clear()
        for nodo in risultato:
            self._view.txt_result.controls.append(
                ft.Text(str(nodo))
            )
        self._view.update_page()

    #questa la prendi dalla view
    def fillDDArtist(self):
        self._view._ddArtista.options.clear()

        artists = self._model.getArtists()
        print("NUMERO ARTISTI:", len(artists))

        for artist in artists:
            self._view._ddArtista.options.append(

                ft.dropdown.Option(
                    key=str(artist.ArtistId),
                    text=artist.Name
                )

            )
        print("OPZIONI INSERITE:", len(self._view._ddArtista.options))
        self._view.update_page()