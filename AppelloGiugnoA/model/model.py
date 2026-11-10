import copy #capire a cosa serve
from dataclasses import dataclass
import itertools
import networkx as nx
from database.DAO import DAO
from collections import defaultdict

class Model:
    def __init__(self):
        #GRAFO ORIENTATO
        self._graph = nx.DiGraph()#o nx.Di
        self._nodes = []
        self._idMapAO = {}

    def buildGraph(self, country):
        self._graph.clear()
        # Costruzione nodi e archi
        # utilizzando genreId nel DAO
        self._nodes = DAO.getAllCustomers(country)
        self._graph.add_nodes_from(self._nodes)
        self._idMapAO = {a.CustomerId: a for a in self._nodes}

        # ARCHI
        coppie = DAO.getAllEdges()

        #questa specificata in base a SQL.
        for row in coppie:
            id1 = row["v1"]
            id2 = row["v2"]

            # Recupero gli oggetti Customer
            if id1 not in self._idMapAO or id2 not in self._idMapAO:
                continue

            u = self._idMapAO[id1]
            v = self._idMapAO[id2]

            # PESO
            peso = u.Fatturato + v.Fatturato

            # DIREZIONE
            if u.Fatturato > v.Fatturato:
                self._graph.add_edge(u, v, weight=peso)

            elif v.Fatturato > u.Fatturato:
                self._graph.add_edge(v, u, weight=peso)

            else:
                self._graph.add_edge(u, v, weight=peso)
                self._graph.add_edge(v, u, weight=peso)

    # TENDINA --> 2) MODEL.py — Recuperare i valori dal DAO
    def getAllCountries(self):
        return DAO.getAllCountries()

    # ---------- STAMPE ----------
    def getNumNodes(self):
        return self._graph.number_of_nodes()

    def getNumEdges(self):
        return self._graph.number_of_edges()