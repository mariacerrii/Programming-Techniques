import copy #capire a cosa serve
from dataclasses import dataclass
import itertools
import networkx as nx
from database.DAO import DAO
from collections import defaultdict

class Model:
    def __init__(self):
            # nx.Graph() --> grafo non orientato
            # nx.DiGraph() --> grafo orientato
            # weight --> attributo per assegnare un peso agli archi
            self._graph = nx.Graph()
            # I VERTICI SONO GLI ARTISTI
            self._nodes = []
            self._idMapAO = {}

            # RICORSIONE!!!!
            ##self._bestPath = []

    def getBestGroup(self, starting_artist, N):
        self._bestGroup = []
        self._maxTracks = 0
        parziale = [starting_artist]
        self._ricorsione(parziale, N)
        return self._bestGroup, self._maxTracks

    def _ricorsione(self, parziale, N):
        # CASO BASE
        if len(parziale) == N:
            total = sum(len(a.tracks) for a in parziale)
            if total > self._maxtracks:
                self._maxtracks = total
                self._bestGroup = parziale.copy()
            return

        # PROVO TUTTI I NODI
        for candidate in self._graph.nodes:
            # Non posso ripetere un artista
            if candidate in parziale:
                continue
            # Deve essere collegato ad almeno un artista del gruppo
            adjacent = any(
                self._graph.has_edge(candidate, existing)
                for existing in parziale
            )

            if not adjacent:
                continue

            # Non deve avere archi di peso 1 con nessun artista

            blocked = any(
                self._graph.has_edge(candidate, existing)
                and self._graph[candidate][existing]["weight"] == 1
                for existing in parziale

            )

            if blocked:
                continue

            # AGGIUNGO
            parziale.append(candidate)

            # RICORSIONE
            self._ricorsione(parziale, N)

            # BACKTRACKING
            parziale.pop()

    def buildGraph(self):
        # 1) Svuoto il grafo
        self._graph.clear()
        # 2) Recupero gli artisti del genere selezionato
        self._nodes = DAO.getAllArtists()
        # 3) Aggiungo i nodi
        self._graph.add_nodes_from(self._nodes)
        # 4) Creo il dizionario degli artisti
        self._idMapAO = {}
        for n in self._nodes:
            self._idMapAO[n.ArtistId] = n

        # ____________________ ARCHI ____________________
        # Recupero dal DAO tutte le coppie di artisti
        # che condividono almeno una playlist, con il relativo peso
        edges = DAO.getAllEdges()

        # Scorro tutte le coppie restituite dal DAO
        for edge in edges:
            # Recupero l'oggetto Artist del primo artista
            # utilizzando il suo ID e il dizionario _idMapAO
            v1 = self._idMapAO[edge["Artist1"]]
            # Recupero l'oggetto Artist del secondo artista
            v2 = self._idMapAO[edge["Artist2"]]

            # Recupero il peso dell'arco
            # cioè il numero di playlist distinte condivise
            peso = edge["peso"]

            # Aggiungo al grafo l'arco tra i due artisti
            # assegnandogli il peso calcolato
            self._graph.add_edge(v1, v2, weight=peso)

    #ARTISTA CON GRADO MASSIMO
    def getMaxDegreeArtist(self):
        bestArtist = None
        bestDegree = None

        for v in self._graph.nodes():
            # NUMERO DI ARCHI INCIDENTI AL NODO
            degree = self._graph.degree(v)
            if bestDegree is None or degree > bestDegree:
                bestDegree = degree
                bestArtist = v
        return bestArtist, bestDegree

    #ARTISTA CON SOMMA GRADI MAGGIORE
    def getBestArtist(self):
        # DEFINISCO DUE VARIABILI
        bestArtist = None
        bestScore = None

        # SCORRO TUTTI I NODI DEL GRAFO
        for v in self._graph.nodes():
            # CALCOLO LA SOMMA DEI PESI DEGLI ARCHI INCIDENTI
            score = 0
            for _, _, data in self._graph.edges(v, data=True):
                score += data["weight"]
            # TROVO L'ARTISTA CON LA SOMMA MAGGIORE
            if bestScore is None or score > bestScore:
                bestScore = score
                bestArtist = v
        return bestArtist, bestScore

    # Migliori 10 vertici
    def getTop10Edges(self):
        edges = sorted(self._graph.edges(data=True),
            # PRIMA ORDINO PER PESO DECRESCENTE
            # POI PER NOMI DEGLI ARTISTI IN ORDINE ALFABETICO
            key=lambda x: (-x[2]["weight"],
                min(x[0].Name, x[1].Name),
                max(x[0].Name, x[1].Name)
            )
        )
        return edges[:10]

    def getTracks(self):
        return DAO.getAllTracks()

    def getArtists(self):
        return self._graph.nodes()

    def getNumNodes(self):
        return len(self._graph.nodes)

    #attenta!!
    def getNumEdges(self):
        return self._graph.number_of_edges()  # Numero di archi

    def getEdges(self):
        return self._graph.edges(data=True)  # Lista degli archi con attributi