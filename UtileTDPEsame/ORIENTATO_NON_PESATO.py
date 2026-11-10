#1) MODEL — Struttura generale
import itertools
import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        # GRAFO ORIENTATO E NON PESATO
        self._graph = nx.DiGraph()
        self._nodes = []
        self._idMapAO = {}

    def buildGraph(self, filtro):
        self._graph.clear()

        # MODIFICARE: recupero nodi dal DAO
        self._nodes = DAO.getNodes(filtro)

        # NON MODIFICARE
        self._graph.add_nodes_from(self._nodes)

        # MODIFICARE: attributo ID
        self._idMapAO = {a.id: a for a in self._nodes}

        # QUI INSERIRE IL METODO PER COSTRUIRE GLI ARCHI

    def getNumNodes(self):
        return self._graph.number_of_nodes()

    def getNumEdges(self):
        return self._graph.number_of_edges()

#2) ARCHI — METODO E (confronto diretto) --> come LUGLIO24A
#Usalo quando le informazioni necessarie sono già presenti negli oggetti dei nodi.
#Esempio: fatture Chinook dello stesso cliente, collegate dalla più vecchia alla più recente.
# MODEL — Inserire dentro buildGraph()
for u, v in itertools.combinations(self._nodes, 2):

    # MODIFICARE: condizione di collegamento
    if u.CustomerId == v.CustomerId:

        # MODIFICARE: direzione
        if u.InvoiceDate < v.InvoiceDate:
            self._graph.add_edge(u, v)

        elif v.InvoiceDate < u.InvoiceDate:
            self._graph.add_edge(v, u)

#2)ARCHI — METODO A (getAllEdges())
#Usalo quando devi recuperare le coppie di nodi tramite SQL.
#DAO
@staticmethod
def getAllEdges():
    conn = DBConnect.get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT DISTINCT
            -- MODIFICARE
            n1.Id AS v1,
            n2.Id AS v2
        FROM ...
        JOIN ...
        WHERE ...
    """

    cursor.execute(query)
    result = []
    for row in cursor:
        result.append(row)

    cursor.close()
    conn.close()
    return result

#MODEL
edges = DAO.getAllEdges()
for edge in edges:

    id1 = edge["v1"]
    id2 = edge["v2"]

    if id1 not in self._idMapAO or id2 not in self._idMapAO:
        continue

    u = self._idMapAO[id1]
    v = self._idMapAO[id2]

    if u == v:
        continue

    # ATTENZIONE ALLA DIREZIONE!
    # Se SQL restituisce già v1 → v2:
    self._graph.add_edge(u, v)

    #DIREZIONI — Schema da ricordare
    #dal maggiore al minore
    if u.valore > v.valore:
        self._graph.add_edge(u, v)

    elif v.valore > u.valore:
        self._graph.add_edge(v, u)

    #dal minore al maggiore
    if u.data < v.data:
        self._graph.add_edge(u, v)

    elif v.data < u.data:
        self._graph.add_edge(v, u)

    #parità
    else:
        self._graph.add_edge(u, v)
        self._graph.add_edge(v, u)