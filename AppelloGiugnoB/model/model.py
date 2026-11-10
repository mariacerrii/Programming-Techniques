import copy #capire a cosa serve
from dataclasses import dataclass
import itertools
import networkx as nx
from database.DAO import DAO
from collections import defaultdict
from itertools import combinations

# grafo semplice, non pesato e non diretto

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        # I VERTICI SONO
        self._nodes = []
        self._idMapAO = {}


    def buildGraph(self):
        self._graph.clear()
        #NODI
        self._nodes = DAO.getAllAlbums()
        self._graph.add_nodes_from(self._nodes)
        self._idMapAO = {a.AlbumId: a for a in self._nodes}
        # COSTRUZIONE ARCHI
        edges = DAO.getAllEdges()
        for edge in edges:

            # NON MODIFICARE
            id1 = edge["v1"]
            id2 = edge["v2"]

            # Controllo che entrambi i nodi esistano
            if id1 not in self._idMapAO or id2 not in self._idMapAO:
                continue

            # Recupero gli oggetti dalla mappa
            u = self._idMapAO[id1]
            v = self._idMapAO[id2]
            self._graph.add_edge(u, v)

    #COMPONENTI CONNESSE - PUNTO C
    def getInfoComponenti(self):
        # Trovo tutte le componenti connesse
        componenti = list(nx.connected_components(self._graph))

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

    def getAllAlbums(self):
        return DAO.getAllAlbums()


    # ---------- STAMPE ----------
    def getNumNodes(self):
        return self._graph.number_of_nodes()

    def getNumEdges(self):
        return self._graph.number_of_edges()

