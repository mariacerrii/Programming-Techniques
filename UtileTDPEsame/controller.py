import flet as ft
# ============================================================
# FORMULARIO CONTROLLER - TECNICHE DI PROGRAMMAZIONE
# ============================================================
#
# DAO        -> Recupera i dati dal database
# MODEL      -> Costruisce il grafo ed esegue i calcoli
# CONTROLLER -> Legge gli input, chiama il Model e stampa
# VIEW       -> Contiene gli elementi grafici
#
# ATTENZIONE:
# - Controllare sempre i nomi dei controlli nella View.
# - Controllare i parametri richiesti dai metodi del Model.
# - Non tutti i metodi servono in ogni traccia.
#
# NOMI USATI IN QUESTO FORMULARIO:
#
# self._view._txt_result -> Colonna dei risultati
# self._view._ddNodo     -> Dropdown per selezionare un nodo
# self._view._txtN       -> TextField per inserire N
#
# Sono nomi di ESEMPIO: adattarli alla View fornita.
Se in view: self._ddArtist ---> In controller: self._view._ddArtist.value
self._txt_result --> self._view._txt_result.controls
self._txtN--> self._view._txtN.value
#
# ============================================================

class Controller:
    # ========================================================
    # 1. INIZIALIZZAZIONE
    # ========================================================

    def __init__(self, view, model):
        self._view = view
        self._model = model

    # ========================================================
    # 2. CREAZIONE GRAFO SENZA PARAMETRI
    # ========================================================
    #
    # USARE QUANDO:
    # La consegna chiede di costruire tutto il grafo.
    #
    # ========================================================

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

    # ========================================================
    # 3. CREAZIONE GRAFO CON FILTRO NUMERICO
    # ========================================================
    #
    # USARE QUANDO:
    # La consegna richiede un parametro, per esempio:
    # - anno minimo
    # - peso minimo
    # - numero minimo di elementi
    #
    # ADATTARE:
    # _txtFiltro e buildGraph(filtro)
    #
    # ========================================================

    def handleCreaGrafoConFiltro(self, e):
        valore = self._view._txtFiltro.value

        self._view._txt_result.controls.clear()

        if valore is None or not valore.strip():
            self._view._txt_result.controls.append(
                ft.Text("Inserire un valore")
            )
            self._view.update_page()
            return

        try:
            filtro = int(valore)
        except ValueError:
            self._view._txt_result.controls.append(
                ft.Text("Inserire un numero intero valido")
            )
            self._view.update_page()
            return

        # Chiamo il Model passando il filtro
        self._model.buildGraph(filtro)

        self._view._txt_result.controls.append(
            ft.Text(f"Numero nodi: {self._model.getNumNodes()}")
        )

        self._view._txt_result.controls.append(
            ft.Text(f"Numero archi: {self._model.getNumEdges()}")
        )

        self._view.update_page()

    # ========================================================
    # 4. CREAZIONE GRAFO CON DROPDOWN
    # ========================================================
    #
    # USARE QUANDO:
    # Il grafo dipende da una selezione della tendina.
    #
    # ========================================================

    def handleCreaGrafoConDropdown(self, e):
        valore = self._view._ddNodo.value

        self._view._txt_result.controls.clear()

        if valore is None:
            self._view._txt_result.controls.append(
                ft.Text("Selezionare un elemento")
            )
            self._view.update_page()
            return

        # Se il Dropdown contiene ID numerici:
        nodo_id = int(valore)

        # Il Model deve accettare questo parametro
        self._model.buildGraph(nodo_id)

        self._view._txt_result.controls.append(
            ft.Text(f"Numero nodi: {self._model.getNumNodes()}")
        )

        self._view._txt_result.controls.append(
            ft.Text(f"Numero archi: {self._model.getNumEdges()}")
        )

        self._view.update_page()

    # ========================================================
    # 5. RIEMPIMENTO DROPDOWN
    # ========================================================
    #
    # USARE QUANDO:
    # Bisogna caricare una tendina con i nodi.
    #
    # ADATTARE:
    # - _ddNodo
    # - getNodes()
    # - nodo.ID
    # - nodo.Name
    #
    # ========================================================
    def fillDD(self):
        self._view._ddNodo.options.clear()
        nodi = self._model.getNodes()
        for nodo in nodi:
            self._view._ddNodo.options.append(
                ft.dropdown.Option(
                    key=str(nodo.ID),
                    text=str(nodo.Name)
                )
            )

        self._view.update_page()

    # ========================================================
    # 6. STAMPA INFORMAZIONI SUL GRAFO
    # ========================================================
    #
    # ESEMPIO: APPELLO GIUGNO 2026 C
    #
    # - Artista con grado massimo
    # - Artista con somma pesi massima
    # - Top 10 archi
    #
    # ========================================================

    def handleStampaInfo(self, e):
        self._view._txt_result.controls.clear()

        # ---------------- GRADO MASSIMO ----------------

        nodo, grado = self._model.getMaxDegreeArtist()

        self._view._txt_result.controls.append(
            ft.Text(
                f"Nodo con grado massimo: {nodo.Name} - {grado}"
            )
        )

        # ---------------- SOMMA PESI MASSIMA ----------------

        nodo, somma = self._model.getBestArtist()

        self._view._txt_result.controls.append(
            ft.Text(
                f"Somma pesi massima: {nodo.Name} - {somma}"
            )
        )

        # ---------------- TOP 10 ARCHI ----------------

        archi = self._model.getTop10Edges()

        self._view._txt_result.controls.append(
            ft.Text("TOP 10 ARCHI:")
        )

        # CASO A:
        # Il Model restituisce (u, v, {"weight": peso})

        for u, v, data in archi:

            self._view._txt_result.controls.append(
                ft.Text(
                    f"{u.Name} - {v.Name}: {data['weight']}"
                )
            )

        # CASO B:
        # Se il Model restituisce (u, v, peso),
        # SOSTITUIRE il ciclo precedente con:
        #
        # for u, v, peso in archi:
        #     self._view._txt_result.controls.append(
        #         ft.Text(f"{u.Name} - {v.Name}: {peso}")
        #     )

        self._view.update_page()

    # ========================================================
    # 7. RICORSIONE - CAMMINO CON PARTENZA FISSATA
    # ========================================================
    #
    # USARE PER:
    # - Cammino semplice più lungo
    # - Cammino con pesi crescenti
    # - Cammino con pesi decrescenti
    #
    # Il Model restituisce una LISTA di nodi.
    #
    # ========================================================

    def handleRicorsioneCammino(self, e):
        self._view._txt_result.controls.clear()
        valore = self._view._ddNodo.value

        if valore is None:
            self._view._txt_result.controls.append(
                ft.Text("Selezionare un nodo di partenza")
            )
            self._view.update_page()
            return

        # Recupero l'oggetto nodo tramite ID
        nodo = self._model.getNodeById(int(valore))

        # Chiamo la ricorsione
        percorso = self._model.getBestPath(nodo)

        # Stampo il percorso
        self._view._txt_result.controls.append(
            ft.Text(f"Lunghezza percorso: {len(percorso)} nodi")
        )

        for elemento in percorso:
            self._view._txt_result.controls.append(
                ft.Text(str(elemento))
            )

        self._view.update_page()

    # ========================================================
    # 8. RICORSIONE - CAMMINO CON PUNTEGGIO
    # ========================================================
    #
    # USARE QUANDO:
    # Il Model restituisce:
    #
    # percorso, punteggio = getBestPath(nodo)
    #
    # ========================================================

    def handleRicorsioneConPunteggio(self, e):
        self._view._txt_result.controls.clear()

        valore = self._view._ddNodo.value

        if valore is None:
            self._view._txt_result.controls.append(
                ft.Text("Selezionare un nodo")
            )
            self._view.update_page()
            return

        nodo = self._model.getNodeById(int(valore))

        percorso, punteggio = self._model.getBestPath(nodo)

        self._view._txt_result.controls.append(
            ft.Text(f"Punteggio: {punteggio}")
        )

        for elemento in percorso:
            self._view._txt_result.controls.append(
                ft.Text(str(elemento))
            )

        self._view.update_page()

    # ========================================================
    # 9. RICORSIONE - GRUPPO DI N NODI
    # ========================================================
    #
    # USARE PER:
    # - Giugno 2026 C
    # - Settembre 2026 A
    #
    # Input:
    # - Nodo di partenza
    # - Numero N
    #
    # Output:
    # - Gruppo migliore
    # - Punteggio massimo
    #
    # ========================================================

    def handleRicorsioneGruppo(self, e):

        self._view._txt_result.controls.clear()

        valore = self._view._ddNodo.value
        valoreN = self._view._txtN.value

        if valore is None or not valoreN:
            self._view._txt_result.controls.append(
                ft.Text("Selezionare un nodo e inserire N")
            )
            self._view.update_page()
            return

        try:
            N = int(valoreN)
        except ValueError:
            self._view._txt_result.controls.append(
                ft.Text("N deve essere un intero")
            )
            self._view.update_page()
            return

        if N < 1:
            self._view._txt_result.controls.append(
                ft.Text("N deve essere almeno 1")
            )
            self._view.update_page()
            return

        nodo = self._model.getNodeById(int(valore))

        gruppo, punteggio = self._model.getBestGroup(nodo, N)

        if not gruppo:
            self._view._txt_result.controls.append(
                ft.Text("Nessuna soluzione trovata")
            )
            self._view.update_page()
            return

        self._view._txt_result.controls.append(
            ft.Text(f"Punteggio massimo: {punteggio}")
        )

        for elemento in gruppo:
            self._view._txt_result.controls.append(
                ft.Text(str(elemento))
            )

        self._view.update_page()

    # ========================================================
    # 10. RICORSIONE - SELEZIONE DI K NODI
    # ========================================================
    #
    # USARE QUANDO:
    # - Non c'è un nodo iniziale
    # - Si devono scegliere K nodi
    # - Eventualmente da componenti diverse
    #
    # ========================================================

    def handleRicorsioneK(self, e):

        self._view._txt_result.controls.clear()

        valoreK = self._view._txtN.value

        try:
            K = int(valoreK)
        except (ValueError, TypeError):
            self._view._txt_result.controls.append(
                ft.Text("Inserire un K valido")
            )
            self._view.update_page()
            return

        if K < 1:
            self._view._txt_result.controls.append(
                ft.Text("K deve essere almeno 1")
            )
            self._view.update_page()
            return

        soluzione, punteggio = self._model.getBestSelection(K)

        if not soluzione:
            self._view._txt_result.controls.append(
                ft.Text("Nessuna soluzione trovata")
            )
            self._view.update_page()
            return

        self._view._txt_result.controls.append(
            ft.Text(f"Punteggio: {punteggio}")
        )

        for nodo in soluzione:
            self._view._txt_result.controls.append(
                ft.Text(str(nodo))
            )

        self._view.update_page()

    # ========================================================
    # 11. RICORSIONE - DUE NODI E LUNGHEZZA K
    # ========================================================
    #
    # USARE QUANDO:
    # Si cerca un cammino:
    # - Da un nodo iniziale
    # - A un nodo finale
    # - Con K archi o K nodi
    #
    # ========================================================

    def handleRicorsioneDueNodi(self, e):

        self._view._txt_result.controls.clear()

        start_id = self._view._ddStart.value
        end_id = self._view._ddEnd.value
        valoreK = self._view._txtK.value

        if start_id is None or end_id is None:
            self._view._txt_result.controls.append(
                ft.Text("Selezionare entrambi i nodi")
            )
            self._view.update_page()
            return

        try:
            K = int(valoreK)
        except (ValueError, TypeError):
            self._view._txt_result.controls.append(
                ft.Text("Inserire un K valido")
            )
            self._view.update_page()
            return

        if K < 0:
            self._view._txt_result.controls.append(
                ft.Text("K non può essere negativo")
            )
            self._view.update_page()
            return

        start = self._model.getNodeById(int(start_id))
        end = self._model.getNodeById(int(end_id))

        percorso = self._model.findPath(start, end, K)

        if not percorso:
            self._view._txt_result.controls.append(
                ft.Text("Nessun percorso trovato")
            )
        else:
            for nodo in percorso:
                self._view._txt_result.controls.append(
                    ft.Text(str(nodo))
                )

        self._view.update_page()

    # ========================================================
    # 12. RICORSIONE - DUE PARAMETRI NUMERICI
    # ========================================================
    #
    # ESEMPIO: F1
    #
    # Input:
    # K = numero di team
    # M = numero minimo di edizioni
    #
    # ========================================================
    def handleRicorsioneKM(self, e):

        self._view._txt_result.controls.clear()

        try:
            K = int(self._view._txtK.value)
            M = int(self._view._txtM.value)
        except (ValueError, TypeError):
            self._view._txt_result.controls.append(
                ft.Text("Inserire K e M validi")
            )
            self._view.update_page()
            return

        if K < 1 or M < 0:
            self._view._txt_result.controls.append(
                ft.Text("Valori di K o M non validi")
            )
            self._view.update_page()
            return

        soluzione, punteggio = self._model.getBestTeams(K, M)

        if not soluzione:
            self._view._txt_result.controls.append(
                ft.Text("Nessuna soluzione trovata")
            )
            self._view.update_page()
            return

        self._view._txt_result.controls.append(
            ft.Text(f"Punteggio massimo: {punteggio}")
        )

        for nodo in soluzione:
            self._view._txt_result.controls.append(
                ft.Text(str(nodo))
            )

        self._view.update_page()

    # ========================================================
    # 13. STAMPA GENERICA DI UNA LISTA
    # ========================================================
    #
    # UTILE PER:
    # - Lista nodi
    # - Lista archi
    # - Percorsi
    # - Gruppi
    #
    # ========================================================

    def stampaLista(self, lista, titolo="Risultati"):

        self._view._txt_result.controls.clear()

        self._view._txt_result.controls.append(
            ft.Text(titolo)
        )

        for elemento in lista:
            self._view._txt_result.controls.append(
                ft.Text(str(elemento))
            )

        self._view.update_page()


