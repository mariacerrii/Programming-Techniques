#1. DAO.py — Recuperare i valori della tendina
@staticmethod
def getAllGenres():
    conn = DBConnect.get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT GenreId, Name
        FROM Genre
        ORDER BY Name
    """

    cursor.execute(query)
    result = []

    for row in cursor:
        result.append(row)

    cursor.close()
    conn.close()

    return result

#REGOLE DA SEGUIRE CHE POI INFLUENZANO ANCHE FILL

#CASO 1 — Ti serve soltanto un valore (Un solo valore per riga)
#ESEMPIO: Tendine semplici: anni, Paesi, generi
#Esempio: tendina Anno
#La traccia chiede di mostrare gli anni degli avvistamenti --> Ti serve soltanto year.
#DAO:
query = """
    SELECT DISTINCT YEAR(datetime) AS year
    FROM sighting
    ORDER BY year ASC
"""
cursor.execute(query)

#QUESTO è QUELLO CHE DEVI NOTARE:
result = []
for row in cursor:
    result.append(row["year"])
cursor.close()
conn.close()
return result

#QUINDI POI NEL CONTROLLER
for year in years:
        self._view.ddyear.options.append(
        ft.dropdown.Option(str(year))
    )

#CASO 2 — Ti servono più valori, ma non vuoi creare oggetti
#Esempio: tendina Stato --> Devi mostrare il nome dello Stato, ma utilizzare il suo codice.
#Ti servono quindi due informazioni: id E Name
#DAO:
query = """
    SELECT id, Name
    FROM state
    ORDER BY Name ASC
"""
cursor.execute(query)
result = []
for row in cursor:
    result.append(row)
cursor.close()
conn.close()
return result

#CONTROLLER
for row in states:
    self._view.ddstate.options.append(
        ft.dropdown.Option(
            key=row["id"],
            text=row["Name"]
        )
    )

#CASO 3 — Devi lavorare con oggetti
#Esempio: nodi del grafo
#La traccia dice che ogni nodo rappresenta un avvistamento UFO
# -->Nel prog
#DAO

# Creo oggetti della classe State
for row in cursor:
    result.append(

        State(
            row["id"],
            row["Name"],
            row["Capital"],
            row["Lat"],
            row["Lng"],
            row["Area"],
            row["Population"],
            row["Neighbors"]
        )
    )
cursor.close()
conn.close()
return result

#CONTROLLER:
def fillddstate(self):

    # Recupero gli oggetti State dal Model
    states = self._model.getAllStates()

    # Scorro gli oggetti
    for state in states:
        # Aggiungo ogni Stato alla tendina
        self._view.ddstate.options.append(
            ft.dropdown.Option(
                key=state.id,      # Valore restituito: "CO"
                text=state.name    # Testo visualizzato: "Colorado"
            )
        )

    # Aggiorno l'interfaccia
    self._view.update_page()


#2. MODEL.py — Recuperare i valori dal DAO
def getAllGenres(self):
    return DAO.getAllGenres()

------
def buildGraph(self, genreId):
    self._graph.clear()
    # Costruzione nodi e archi
    # utilizzando genreId nel DAO

#3 CONTROLLER.py — Riempire la tendina
#Supponendo che nella View esista dd_genre:
# PRIMA METTI TENDINE POI GRAFI E ARCHI (guarda luglio 24 che capisci subito come gestirla)
def fillDDGenre(self):
    genres = self._model.getAllGenres()

    self._view.dd_genre.options.clear()

    for g in genres:
        self._view.dd_genre.options.append(
            ft.dropdown.Option(
                key=str(g["GenreId"]),
                text=g["Name"]
            )
        )
    self._view.update_page()

#4. CONTROLLER.py — handle_grafo() con tendina
def __init__(self, view, model):
    # the view, with the graphical elements of the UI
    self._view = view
    # the model, which implements the logic of the program and holds the data
    self._model = model

    # Preparo i Paesi per la tendina
    self._countries = self._model.getAllCountries()
def handle_grafo(self, e):

    # Leggo il valore selezionato
    genreId = self._view.dd_genre.value

    # Controllo che sia stato selezionato
    if genreId is None:
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(
            ft.Text("Seleziona un genere!")
        )
        self._view.update_page()
        return

    # Costruisco il grafo
    self._model.buildGraph(int(genreId))

    # Stampo nodi e archi
    self._view.txt_result.controls.clear()
    self._view.txt_result.controls.append(
        ft.Text(f"Numero nodi: {self._model.getNumNodes()}")
    )

    self._view.txt_result.controls.append(
        ft.Text(f"Numero archi: {self._model.getNumEdges()}")
    )

    self._view.update_page()

#4 VIEW
#DEVI MODIFICARE LA VIEW:
#HAI QUESTA:
self._ddCountry = ft.Dropdown(label="Country")
#INSERISCI QUESTA:
self._controller.fillDDCountry()
#QUESTA LA HAI GIA
self._btnCreaGrafo