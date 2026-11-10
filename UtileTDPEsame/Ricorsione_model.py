# ============================================================
# RICORSIONE GENERALE - MODEL
# ============================================================
# METODO PUBBLICO: inizializza e avvia la ricerca
def getBestSolution(self, parametro):

    # Migliore soluzione trovata
    self._bestSolution = []

    # Miglior punteggio trovato
    self._bestScore = float("-inf")

    # Avvio la ricorsione con una soluzione parziale
    self._ricorsione([], parametro, 0)

    return self._bestSolution, self._bestScore


# METODO RICORSIVO: esplora le possibili soluzioni
def _ricorsione(self, parziale, parametro, score):
    # 1. CONDIZIONE TERMINALE
    if len(parziale) == parametro:

        # 2. CONTROLLO SE LA SOLUZIONE È MIGLIORE
        if score > self._bestScore:

            self._bestScore = score
            self._bestSolution = parziale.copy()

        return

    # 3. GENERO I POSSIBILI CANDIDATI
    for nodo in self._graph.nodes:

        # 4. CONTROLLO I VINCOLI
        if nodo in parziale:
            continue

        # 5. AGGIUNGO IL CANDIDATO
        parziale.append(nodo)

        # 6. CHIAMATA RICORSIVA
        self._ricorsione(
            parziale,
            parametro,
            score + 1
        )

        # 7. BACKTRACKING
        parziale.pop()

# ============================================================
# CAMMINO SEMPLICE PIÙ LUNGO
# ============================================================
def getBestPath(self, source):
    self._bestPath = [source]
    self._ricorsione([source])
    return self._bestPath


def _ricorsione(self, parziale):
    # Aggiorno il miglior cammino
    if len(parziale) > len(self._bestPath):
        self._bestPath = parziale.copy()

    # Considero solo i vicini dell'ultimo nodo
    ultimo = parziale[-1]

    for vicino in self._graph.neighbors(ultimo):

        # Non posso ripetere nodi
        if vicino in parziale:
            continue

        # Aggiungo
        parziale.append(vicino)

        # Ricorsione
        self._ricorsione(parziale)

        # Backtracking
        parziale.pop()

# ============================================================
# CAMMINO CON PESI STRETTAMENTE CRESCENTI
# ============================================================
#PESI DECRESCENTI CAMBIA SOLO: if ultimoPeso is not None and peso >= ultimoPeso:

def getBestPath(self, source):
    self._bestPath = [source]
    self._ricorsione([source], None)
    return self._bestPath


def _ricorsione(self, parziale, ultimoPeso):
    # Aggiorno il miglior cammino
    if len(parziale) > len(self._bestPath):
        self._bestPath = parziale.copy()

    ultimo = parziale[-1]

    for vicino in self._graph.neighbors(ultimo):

        # Nodo già visitato
        if vicino in parziale:
            continue

        # Recupero peso dell'arco
        peso = self._graph[ultimo][vicino]["weight"]

        # Pesi strettamente crescenti
        if ultimoPeso is not None and peso <= ultimoPeso:
            continue

        # Aggiungo
        parziale.append(vicino)

        # Ricorsione
        self._ricorsione(parziale, peso)

        # Backtracking
        parziale.pop()

# ============================================================
# GRUPPO DI N NODI - MASSIMIZZAZIONE PUNTEGGIO
# ============================================================

def getBestGroup(self, source, N):
    self._bestGroup = []
    self._bestScore = float("-inf")

    # Parto dal nodo selezionato
    self._ricorsione([source], N)

    return self._bestGroup, self._bestScore


def _ricorsione(self, parziale, N):
    # 1. CONDIZIONE TERMINALE
    if len(parziale) == N:

        # Calcolo punteggio del gruppo
        score = sum(len(nodo.Tracks) for nodo in parziale)

        # Aggiorno migliore soluzione
        if score > self._bestScore:
            self._bestScore = score
            self._bestGroup = parziale.copy()

        return

    # 2. GENERO I CANDIDATI
    for candidato in self._graph.nodes:

        # Non posso selezionare due volte lo stesso nodo
        if candidato in parziale:
            continue

        # Deve essere collegato ad almeno un nodo del gruppo
        if not any(
            self._graph.has_edge(candidato, nodo)
            for nodo in parziale
        ):
            continue

        # Non devono esserci archi di peso 1
        if any(
            self._graph.has_edge(candidato, nodo)
            and self._graph[candidato][nodo]["weight"] == 1
            for nodo in parziale
        ):
            continue

        # 3. AGGIUNGO
        parziale.append(candidato)

        # 4. RICORSIONE
        self._ricorsione(parziale, N)

        # 5. BACKTRACKING
        parziale.pop()

# ============================================================
# SELEZIONE DI K NODI - INCLUDO / ESCLUDO
# ============================================================
def getBestSelection(self, K):

    self._bestSelection = []
    self._bestScore = float("-inf")

    nodi = list(self._graph.nodes)

    self._ricorsione(nodi, 0, [], K, 0)

    return self._bestSelection, self._bestScore

def _ricorsione(self, nodi, indice, parziale, K, score):

    # 1. HO SCELTO K NODI
    if len(parziale) == K:

        if score > self._bestScore:
            self._bestScore = score
            self._bestSelection = parziale.copy()

        return

    # 2. HO FINITO I CANDIDATI
    if indice == len(nodi):
        return

    # 3. NON HO ABBASTANZA CANDIDATI RIMASTI
    if len(parziale) + len(nodi) - indice < K:
        return

    nodo = nodi[indice]

    # 4. SCELGO IL NODO
    parziale.append(nodo)

    self._ricorsione(
        nodi,
        indice + 1,
        parziale,
        K,
        score + nodo.PUNTEGGIO
    )

    parziale.pop()

    # 5. NON SCELGO IL NODO
    self._ricorsione(
        nodi,
        indice + 1,
        parziale,
        K,
        score
    )
