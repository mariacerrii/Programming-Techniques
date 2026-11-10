from database.DAO import DAO
from model.model import Model

model = Model()
# Paese da utilizzare per il test
country = "Canada"
# Costruisco il grafo
model.buildGraph(country)

print("Numero nodi:", model.getNumNodes())
print("Numero archi:", model.getNumEdges())