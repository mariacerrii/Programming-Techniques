import copy #capire a cosa serve
from dataclasses import dataclass
import itertools
import networkx as nx
from database.DAO import DAO
from collections import defaultdict

# Dizionario: gruppo → insieme di nodi
gruppi = defaultdict(set)

#model
class Model:
    def __init__(self):
        self._graph = nx.DiGraph()
        self._nodes = []
        self._idMapAO = {}

    def buildGraph(self, year,shape):
        self._graph.clear()  # evita duplicati tra costruzioni
        self._nodes = DAO.getNodes(year,shape)
        self._graph.add_nodes_from(self._nodes)
        self._idMapAO = {a.id: a for a in self._nodes}

        # ARCHI - confronto diretto tra nodi
        for u, v in itertools.combinations(self._nodes, 2):
            # I due avvistamenti devono essere nello stesso Stato
            if u.state == v.state:
                # Arco dal più vecchio al più recente
                if u.datetime < v.datetime:
                    self._graph.add_edge(u, v)
                elif v.datetime < u.datetime:
                    self._graph.add_edge(v, u)


    #TENDINA ANNI X ANNI
    def getAllYears(self):
        return DAO.getAllYears()

    def getAllShapes(self):
        return DAO.getAllShapes()


    # ---------- STAMPE ----------
    def getNumNodes(self):
        return self._graph.number_of_nodes()

    def getNumEdges(self):
        return self._graph.number_of_edges()