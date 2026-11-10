#TESTMODEL
from database.DAO import DAO
from model.modello import Model

model = Model()
year=2004
shape="disk"
model.buildGraph(year,shape)

print("Numero nodi:", model.getNumNodes())
print("Numero archi:", model.getNumEdges())