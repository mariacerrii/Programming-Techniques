from model.model import Model

model = Model()
model.buildGraph()

# ____________________ PUNTO 1C ____________________
print("Numero nodi:", model.getNumNodes())
print("Numero archi:", model.getEdges())

# ____________________ PUNTO 1D ____________________

# 1. ARTISTA CON GRADO MASSIMO
artist, degree = model.getMaxDegreeArtist()
print(f"\nArtista con grado massimo: {artist.Name} - Grado: {degree}")

# 2. ARTISTA CON SOMMA DEI PESI MASSIMA
artist, score = model.getBestArtist()
print(f"\nArtista con somma dei pesi massima: {artist.Name} - Somma: {score}")

# 3. TOP 10 ARCHI CON PESO MAGGIORE
print("\nTOP 10 ARCHI:")
for v1, v2, data in model.getTop10Edges():
    print(f"{v1.Name} - {v2.Name} | Peso: {data['weight']}")

