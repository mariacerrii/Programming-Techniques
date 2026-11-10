import copy
from time import time


class QuadratoMagico():
    def __init__(self, N):
        self.N = N
        self.n_chiamate = 0
        self.n_soluzioni = 0
        self.soluzioni = []

    # soluzione del quadrato magico rappresentata da un vettore di N**2 elementi,
    #ogni elemento rappresenta una cella del quadrato, ed il suo valore è il numero che
    # mettiamo nella cella
    def risolvi_quadrato(self):
        self.n_chiamate = 0
        self.n_soluzioni = 0
        self.soluzioni = []
        self._ricorsione([], set(range(1,self.N*self.N+1)))

    def _ricorsione(self, parziale, rimanenti):
        self.n_chiamate += 1
        #caso terminale
        if len(parziale) == self.N*self.N:
            if self._is_valid(parziale):
                self.n_soluzioni += 1
                self.soluzioni.append(copy.deepcopy(parziale))
            # print(parziale)
        #caso ricorsivo
        else:
            for numero in rimanenti:
                #) fare controllo dei vincoli
                #1)aggiungere numero a parziale
                parziale.append(numero)
                if self._is_parziale_valid(parziale):
                    #1b) tolgo il numero appena inserito dai rimanenti
                    nuovi_rimanenti = copy.deepcopy(rimanenti)
                    nuovi_rimanenti.remove(numero)
                    #2)andare avanti nella ricorsione
                    self._ricorsione(parziale, nuovi_rimanenti)
                #3) backtracking
                parziale.pop()

    def _is_parziale_valid(self, parziale):
        numero_magico = self.N*(self.N*self.N+1)/2
        #1) controllare righe
        n_righe_completate = len(parziale)//self.N
        for id_riga in range(n_righe_completate):
            riga = parziale[id_riga*self.N:(id_riga+1)*self.N]
            if sum(riga) != numero_magico:
                return False
        #2) controllare le colonne
        n_col_completate = max(len(parziale) -self.N*(self.N-1), 0)
        for id_col in range(n_col_completate):
            col = parziale[id_col : (self.N-1)*self.N + id_col + 1: self.N]
            if sum(col) != numero_magico:
                return False
        # #3) controllare diagonale 1
        # diagonale1 = potenziale_soluzione[0:self.N**2+1:self.N+1]
        # if sum(diagonale1) != numero_magico:
        #     return False
        # #4) controllare diagonale 2
        # somma = 0
        # for indice in range(self.N):
        #     somma += potenziale_soluzione[indice*self.N + (self.N-1 - indice)]
        # if somma != numero_magico:
        #     return False
        #5) passati tutti i controlli, possiamo ritornare True
        return True

    def _is_valid(self, potenziale_soluzione):
        numero_magico = self.N*(self.N*self.N+1)/2
        #1) controllare righe
        for id_riga in range(self.N):
            riga = potenziale_soluzione[id_riga*self.N:(id_riga+1)*self.N]
            if sum(riga) != numero_magico:
                return False
        #2) controllare le colonne
        for id_col in range(self.N):
            col = potenziale_soluzione[id_col : (self.N-1)*self.N + id_col + 1: self.N]
            if sum(col) != numero_magico:
                return False
        #3) controllare diagonale 1
        diagonale1 = potenziale_soluzione[0:self.N**2+1:self.N+1]
        if sum(diagonale1) != numero_magico:
            return False
        #4) controllare diagonale 2
        somma = 0
        for indice in range(self.N):
            somma += potenziale_soluzione[indice*self.N + (self.N-1 - indice)]
        if somma != numero_magico:
            return False

        #5) passati tutti i controlli, possiamo ritornare True
        return True

    def stampa_quadrato(self, soluzione):
        print("-------------")
        for riga in range(self.N):
            print(soluzione[riga * self.N: (riga+1) * self.N])
        print("-------------")

if __name__ == '__main__':
    qm = QuadratoMagico(3)
    start_time = time()
    qm.risolvi_quadrato()
    end_time = time()

    print(f"Tempo impiegato = {end_time - start_time}")
    print(f"Chiamate effettuate = {qm.n_chiamate}")
    print(f"Soluzioni trovate = {qm.n_soluzioni}")
    for soluzione in qm.soluzioni:
        qm.stampa_quadrato(soluzione)
