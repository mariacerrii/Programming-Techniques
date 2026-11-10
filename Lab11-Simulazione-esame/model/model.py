import copy #capire a cosa serve

from dataclasses import dataclass
import itertools
import networkx as nx
from database.DAO import DAO
from collections import defaultdict
#defaultdict(dict) crea automaticamente un dizionario vuoto {}.


class Model:
    def __init__(self):
        # nx.Graph() --> grafo non orientato
        # nx.DiGraph() --> grafo orientato
        # weight --> attributo per assegnare un peso agli archi
        self._graph = nx.DiGraph()
         # I VERTICI SONO GLI ARTISTI
        self._nodes = []
        self._idMapAO = {}

        #RICORSIONE!!!!
        self._bestPath = []

    #____________________________________________
    # RICORSIONE 1: PERCORSO SEMPLICE PIÙ LUNGO
    # CON PESI DEGLI ARCHI STRETTAMENTE CRESCENTI
    #___________________________________________
    def getBestPath(self, source):
        # 1) Azzero il percorso migliore trovato
        self._bestPath = []

        # 2) Creo una lista contenente il nodo di partenza.
        # source è l'ID dell'artista selezionato.
        # self._idMapAO[int(source)] recupera l'oggetto Artist.
        partial = [self._idMapAO[int(source)]]

        # 3) Scorro tutti gli archi USCENTI dal nodo iniziale
        # v = nodo di arrivo dell'arco
        # data = dizionario contenente gli attributi dell'arco
        # data["weight"] = peso dell'arco
        for _, v, data in self._graph.out_edges(
                self._idMapAO[int(source)], data=True):
            # Aggiungo il nodo di arrivo al percorso parziale
            partial.append(v)

            # Avvio la ricorsione
            # Passo:
            # 1) partial = percorso costruito fino a questo momento
            # 2) data["weight"] = peso dell'ultimo arco attraversato
            self._ricorsione(partial, data["weight"])

            # BACKTRACKING
            # Rimuovo l'ultimo nodo aggiunto.
            # In questo modo posso provare un altro arco uscente dal nodo iniziale.
            partial.pop()

        # Restituisco il percorso migliore trovato.
        return self._bestPath

    def _ricorsione(self, partial, lastWeight):
        # 1) CONTROLLO SE HO TROVATO UN PERCORSO MIGLIORE
        # len(partial) = numero di nodi del percorso corrente
        # len(self._bestPath) = numero di nodi del miglior percorso

        # Se il percorso corrente contiene più nodi, lo salvo come nuova soluzione migliore.
        if len(partial) > len(self._bestPath):
            # deepcopy --> crea una copia indipendente della lista
            # Serve perché successivamente utilizzeremo pop() per modificare il percorso parziale.
            self._bestPath = copy.deepcopy(partial)

        # 2) RECUPERO IL NODO CORRENTE
        # partial[-1] restituisce l'ultimo elemento della lista.
        current = partial[-1]

        # 3) ESPLORO GLI ARCHI USCENTI DAL NODO CORRENTE
        # successor = possibile nodo successivo
        # data = attributi dell'arco
        for _, successor, data in self._graph.out_edges(
                current, data=True):

            # Recupero il peso dell'arco che sto valutando.
            weight = data["weight"]

            # 4) PRIMO VINCOLO: PESI STRETTAMENTE CRESCENTI
            # Posso attraversare il nuovo arco soltanto e il suo peso è MAGGIORE del peso precedente.
            if weight > lastWeight:

                # 5) SECONDO VINCOLO: PERCORSO SEMPLICE
                # Un percorso semplice non può contenere due volte lo stesso nodo.
                # Controllo quindi che successor non sia già presente nella lista partial.
                if successor not in partial:
                    # 6) AGGIUNGO IL NODO AL PERCORSO
                    partial.append(successor)

                    # 7) CHIAMATA RICORSIVA
                    # Proseguo la ricerca partendo dal nuovo nodo. Passo il nuovo peso come lastWeight.
                    self._ricorsione(partial, weight)

                    # 8) BACKTRACKING
                    # Rimuovo il nodo appena esplorato.
                    # Torno al percorso precedente per cercare eventuali altre soluzioni.
                    partial.pop()


    def buildGraph(self, genere):
        # 1) Svuoto il grafo
        self._graph.clear()
        # 2) Recupero gli artisti del genere selezionato
        self._nodes = DAO.getAllArtists(genere)
        # 3) Aggiungo i nodi
        self._graph.add_nodes_from(self._nodes)
        # 4) Creo il dizionario degli artisti
        self._idMapAO = {}
        for n in self._nodes:
            self._idMapAO[n.ArtistId] = n

        # Recupero gli acquisti dal DAO
        customer_artist_list = DAO.getCustomerArtistCounts(genere)
        # Creo un dizionario di dizionari
        customerMap = defaultdict(dict)
        # Organizzo gli acquisti per cliente
        for customer_id, artist_id, ntracks in customer_artist_list:
            customerMap[customer_id][artist_id] = ntracks

        #Creare dizioario popolarita
        artist_popularity = defaultdict(int)

        # CALCOLO LA POPOLARITÀ DI OGNI ARTISTA
        # Scorro tutti i clienti presenti in customerMap.
        for customer, artists in customerMap.items():
            # Per ogni cliente scorro gli artisti acquistati
            # artist_id = ID dell'artista
            # ntracks = numero di acquisti di quell'artista da parte del cliente
            for artist_id, ntracks in artists.items():
                # Sommo gli acquisti del cliente alla popolarità dell'artista.
                artist_popularity[artist_id] += ntracks

        # INDIVIDUO LE COPPIE DI ARTISTI CHE CONDIVIDONO UN CLIENTE
        # Scorro nuovamente tutti i clienti.
        for customer_id, artists in customerMap.items():
            #itertools.combinations(artists.keys(), 2) --> genera tutte le possibili coppie di 2 artisti acquistati dallo stesso cliente.
            # Non genera coppie con lo stesso artista (1, 1)
            # e non ripete la stessa coppia invertita (2, 1).
            for a, b in itertools.combinations(artists.keys(), 2):
                # RECUPERO LA POPOLARITÀ DEI DUE ARTISTI
                # a e b sono gli ID dei due artisti.
                # Recupero la loro popolarità dal dizionario creato prima.
                pop_a = artist_popularity[a]
                pop_b = artist_popularity[b]

                #calcolo peso arco
                weight = pop_a + pop_b

                # STABILISCO LA DIREZIONE DELL'ARCO
                # Il professore orienta l'arco dall'artista
                # MENO popolare verso quello PIÙ popolare.
                # Se a è meno popolare di b: creo un arco orientato a -> b.
                if pop_a < pop_b:
                    self._graph.add_edge(self._idMapAO[a], self._idMapAO[b], weight=weight)
                # Se a è più popolare di b: creo un arco orientato b -> a.
                elif pop_a > pop_b:
                    self._graph.add_edge(self._idMapAO[b], self._idMapAO[a], weight=weight)
                else:
                    # Se i due artisti hanno la stessa popolarità: creo DUE archi, uno per ogni direzione.
                    # Primo arco: a -> b
                    self._graph.add_edge(self._idMapAO[a], self._idMapAO[b], weight=weight)
                    # Secondo arco: b -> a
                    self._graph.add_edge(self._idMapAO[b], self._idMapAO[a], weight=weight)


    def getBestArtist(self):
        #DEFINISCO DUE VARIABILI
        # bestArtist: memorizzerà l’artista migliore trovato fino a quel momento.
        # bestScore: memorizzerà il suo punteggio.
        bestArtist = None
        bestScore = None


        for v in self._graph.nodes():

            # CALCOLIAMO PESI ARCHI USCENTI
            outWeight = 0
            #self._graph.out_edges(v)--> CHE PARTONO DA NODO V
            for _, _, data in self._graph.out_edges(v, data=True):
                #QUI SOMMANO TUTTI PESI ARCHI USCENTI
                outWeight += data["weight"]

            #PESI ARCHI ENTRANTI
            inWeight = 0
            for _, _, data in self._graph.in_edges(v, data=True):
                inWeight += data["weight"]

            # CALCOLIAMO LO SCORE (DA TESTO)
            score = outWeight - inWeight

            #TROVIAMO ARTISTA MIGLIORE
            if bestScore is None or score > bestScore:
                bestScore = score
                bestArtist = v

        return bestArtist.Name, bestScore

    def getTop5Edges(self):

        edges = sorted(
            self._graph.edges(data=True),
            key=lambda x: x[2]["weight"],
            reverse=True
        )

        return edges[:5]

    #   QUESTI FISSI
    def getGenres(self):
        return DAO.getAllGenres()

    def getArtists(self):
        return self._graph.nodes()

    def getNumNodes(self):
        return len(self._graph.nodes)

    def getNumEdges(self):
        return len(self._graph.edges)