#File che usiamo per fare delle prove
from database.DAO import DAO
from model.model import Model
from model.genre import Genre

#Definiamo modello
model=Model()
#Istanza del modello
genere = Genre(1, "Rock")
model.buildGraph(genere)
#Len --> definiamo numero nodi, "lunghezza"
print("Numero nodi:", model.getNumNodes())
print("Numero archi:", model.getNumEdges())

#ricorsione!!
print(model.getBestArtist())
