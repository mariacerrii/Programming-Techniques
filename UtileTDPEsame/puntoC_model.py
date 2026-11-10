import networkx as nx


# ============================================================
# 1. TOP 5 NODI CON PIÙ ARCHI USCENTI + SOMMA PESI USCENTI
# GRAFO ORIENTATO E PESATO
# ============================================================
def getTop5ArchiUscenti(self):
    risultati = []

    for nodo in self._grafo.nodes:
        numero = self._grafo.out_degree(nodo)
        peso = self._grafo.out_degree(nodo, weight="weight")
        risultati.append((nodo, numero, peso))

    risultati.sort(key=lambda x: x[1], reverse=True)
    return risultati[:5]

# ============================================================
# 2. TOP 5 NODI CON GRADO MAGGIORE
# QUALSIASI GRAFO
# ============================================================
def getTop5Nodi(self):
    nodi = sorted(
        self._grafo.nodes,
        key=lambda n: self._grafo.degree(n),
        reverse=True
    )[:5]

    return [(nodo, self._grafo.degree(nodo)) for nodo in nodi]



# ============================================================
# 3. COMPONENTI DEBOLMENTE CONNESSE
# GRAFO ORIENTATO
# ============================================================
def getComponentiDeboli(self):
    componenti = list(nx.weakly_connected_components(self._grafo))

    if not componenti:
        return 0, []

    maggiore = max(componenti, key=len)

    return len(componenti), list(maggiore)


# ============================================================
# 4. COMPONENTI CONNESSE DI DIMENSIONE > 1
# GRAFO NON ORIENTATO
# ============================================================
def getComponentiMaggioriDiUno(self):
    componenti = list(nx.connected_components(self._grafo))

    componenti = [c for c in componenti if len(c) > 1]
    componenti.sort(key=len, reverse=True)

    return componenti


# ============================================================
# 5. NODO CON MASSIMO NUMERO DI ARCHI USCENTI
# GRAFO ORIENTATO
# ============================================================
def getNodoMaxArchiUscenti(self):
    if self._grafo.number_of_nodes() == 0:
        return None

    nodo = max(
        self._grafo.nodes,
        key=lambda n: self._grafo.out_degree(n)
    )
    return nodo, self._grafo.out_degree(nodo)

# ============================================================
# 6. ARTISTA CON INFLUENZA MASSIMA
# INFLUENZA = PESI USCENTI - PESI ENTRANTI
# GRAFO ORIENTATO E PESATO
# ============================================================
def getArtistaMaxInfluenza(self):
    if self._grafo.number_of_nodes() == 0:
        return None

    risultati = []

    for nodo in self._grafo.nodes:
        peso_uscente = self._grafo.out_degree(nodo, weight="weight")
        peso_entrante = self._grafo.in_degree(nodo, weight="weight")

        influenza = peso_uscente - peso_entrante
        risultati.append((nodo, influenza))

    return max(risultati, key=lambda x: x[1])


# ============================================================
# 7A / 8A. NODO CON GRADO MAGGIORE
# ============================================================
def getNodoMaxGrado(self):
    if self._grafo.number_of_nodes() == 0:
        return None

    nodo = max(
        self._grafo.nodes,
        key=lambda n: self._grafo.degree(n)
    )

    return nodo, self._grafo.degree(nodo)


# ============================================================
# 7B / 8B. NODO CON SOMMA PESI INCIDENTI MASSIMA
# ============================================================
def getNodoMaxPesoIncidente(self):
    if self._grafo.number_of_nodes() == 0:
        return None

    nodo = max(
        self._grafo.nodes,
        key=lambda n: self._grafo.degree(n, weight="weight")
    )

    return nodo, self._grafo.degree(nodo, weight="weight")


# ============================================================
# 7C. TOP 5 ARCHI CON PESO MAGGIORE
# ============================================================
def getTop5ArchiPeso(self):
    return sorted(
        self._grafo.edges(data=True),
        key=lambda x: x[2].get("weight", 1),
        reverse=True
    )[:5]


# ============================================================
# 7C BIS. TOP 5 ARCHI PER PESO DECRESCENTE
# A PARITÀ: NOMI ALFABETICI CRESCENTI
#
# MODIFICARE "name" CON L'ATTRIBUTO REALE DEI NODI
# ============================================================
def getTop5ArchiPesoAlfabetico(self):
    def chiave(arco):
        u, v, dati = arco

        nome_u = str(getattr(u, "name", str(u)))
        nome_v = str(getattr(v, "name", str(v)))

        # Per grafi non orientati: normalizza l'ordine dei nomi
        if not self._grafo.is_directed():
            nome_u, nome_v = sorted((nome_u, nome_v))

        return (-dati.get("weight", 1), nome_u, nome_v)

    return sorted(self._grafo.edges(data=True), key=chiave)[:5]


# ============================================================
# 7D. NODO PIÙ GIOVANE
# MODIFICARE "date_of_birth" SE NECESSARIO
# ============================================================
def getNodoPiuGiovane(self):
    nodi = [
        n for n in self._grafo.nodes
        if getattr(n, "date_of_birth", None) is not None
    ]

    if not nodi:
        return None

    return max(nodi, key=lambda n: n.date_of_birth)


# ============================================================
# 7E. NODO PIÙ ANZIANO
# ============================================================
def getNodoPiuAnziano(self):
    nodi = [
        n for n in self._grafo.nodes
        if getattr(n, "date_of_birth", None) is not None
    ]

    if not nodi:
        return None

    return min(nodi, key=lambda n: n.date_of_birth)


# ============================================================
# 9 / 11. COMPONENTE MAGGIORE ORDINATA PER GRADO DECRESCENTE
# ============================================================
def getComponenteMaxPerGrado(self):
    grafo = self._grafo.to_undirected()

    componenti = list(nx.connected_components(grafo))

    if not componenti:
        return 0, []

    maggiore = max(componenti, key=len)

    risultati = sorted(
        [(n, grafo.degree(n)) for n in maggiore],
        key=lambda x: x[1],
        reverse=True
    )

    return len(componenti), risultati

# ============================================================
#  variabile di quello sopra in ORDINE ALFABETICO + NUMERO BRANI (GIUGNO B)
# ============================================================

def getInfoComponenti(self):
    # Trovo tutte le componenti connesse
    componenti = list(nx.connected_components(self._grafo))

    if len(componenti) == 0:
        return 0, []

    # Trovo la componente più grande
    maggiore = max(componenti, key=len)

    # Ordino gli album alfabeticamente per titolo
    album_ordinati = sorted(
        maggiore,
        key=lambda a: a.Title
    )

    return len(componenti), album_ordinati


# ============================================================
# 10. COMPONENTE MAGGIORE ORDINATA PER
# PESO MASSIMO DEGLI ARCHI INCIDENTI
# ============================================================
def getComponenteMaxPerPeso(self):
    grafo = self._grafo.to_undirected()

    componenti = list(nx.connected_components(grafo))

    if not componenti:
        return 0, []

    maggiore = max(componenti, key=len)

    risultati = []

    for nodo in maggiore:
        pesi = [
            dati.get("weight", 1)
            for _, _, dati in grafo.edges(nodo, data=True)
        ]

        peso_max = max(pesi) if pesi else 0
        risultati.append((nodo, peso_max))

    risultati.sort(key=lambda x: x[1], reverse=True)

    return len(componenti), risultati


# ============================================================
# 12. PERCORSO PIÙ LUNGO NELL'ALBERO DFS
# ATTENZIONE: NON È NECESSARIAMENTE IL CAMMINO
# SEMPLICE PIÙ LUNGO DEL GRAFO ORIGINALE
# ============================================================
def getPercorsoMassimoDFS(self, source):
    if source not in self._grafo:
        return []

    albero = nx.dfs_tree(self._grafo, source=source)

    foglie = [
        n for n in albero.nodes
        if albero.out_degree(n) == 0
    ]

    percorso_massimo = [source]

    for foglia in foglie:
        percorso = nx.shortest_path(albero, source, foglia)

        if len(percorso) > len(percorso_massimo):
            percorso_massimo = percorso

    return percorso_massimo


# ============================================================
# 13 / 14. NODI ADIACENTI ORDINATI PER PESO DECRESCENTE
# ============================================================
def getViciniOrdinati(self, source):
    if source not in self._grafo:
        return []

    risultati = []

    for vicino in self._grafo.neighbors(source):
        peso = self._grafo[source][vicino].get("weight", 1)
        risultati.append((vicino, peso))

    risultati.sort(key=lambda x: x[1], reverse=True)

    return risultati


# ============================================================
# 15A. VISITA DFS - NODI RAGGIUNGIBILI
# INCLUDE IL NODO DI PARTENZA
# ============================================================
def getDFS(self, source):
    if source not in self._grafo:
        return []

    return list(nx.dfs_preorder_nodes(self._grafo, source=source))


# ============================================================
# 15B. VISITA BFS - NODI RAGGIUNGIBILI
# INCLUDE IL NODO DI PARTENZA
# ============================================================
def getBFS(self, source):
    if source not in self._grafo:
        return []

    return list(nx.bfs_tree(self._grafo, source=source).nodes)