class Model:
    def __init__(self):
        self._graph = nx.Graph() #o nx.Di
        self._nodes = []
        self._idMapAO = {}

    def buildGraph(self):
        # COSTRUZIONE NODI
        # ...
        # COSTRUZIONE ARCHI
        # ...


    # ---------- STAMPE ----------
    def getNumNodes(self):

        return self._graph.number_of_nodes()

    def getNumEdges(self):

        return self._graph.number_of_edges()


# TIPI DI GRAFO - NETWORKX
# GRAFO NON ORIENTATO / NON DIRETTO
self._graph = nx.Graph()
self._graph = nx.Graph()

# GRAFO ORIENTATO / DIRETTO
# Sono sinonimi: i collegamenti hanno una direzione
self._graph = nx.DiGraph()

# GRAFO PESATO
# Può essere sia orientato sia non orientato.
self._graph.add_edge(u, v, weight=peso)

# GRAFO NON PESATO
self._graph.add_edge(u, v)

# GRAFO SEMPLICE
# Non ammette archi multipli tra gli stessi nodi né autoarchi.
# nx.Graph() non crea archi multipli, ma gli autoarchi
# devono essere evitati esplicitamente nel codice.

#Grafo NON orientato (nx.Graph()) → eviti le coppie duplicate e gli autoarchi.
#Grafo orientato (nx.DiGraph()) → eviti gli autoarchi,
# ma non necessariamente le coppie inverse, perché A → B e B → A sono due archi diversi.

#EVITARE COPPIE DUPLICATE (SE RICHIESTO)
# - Grafo non orientato
for u, v in itertools.combinations(self._nodes, 2):
    # Verificare la condizione della traccia
    if condizione:
        self._graph.add_edge(u, v)

#TESTMODEL
from model.model import Model

model = Model()
model.buildGraph()

print("Numero nodi:", model.getNumNodes())
print("Numero archi:", model.getNumEdges())



