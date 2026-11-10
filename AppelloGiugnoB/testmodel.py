from model.model import Model

model = Model()
model.buildGraph()

print("Numero nodi:", model.getNumNodes())
print("Numero archi:", model.getNumEdges())