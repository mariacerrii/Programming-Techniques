from dictionary import Dictionary
class Translator:
    def __init__(self):
        #Write an empty dict
        self.dictionary = Dictionary()

    def printMenu(self):
        # 1. Aggiungi nuova parola
        print("1) Aggiungi nuova parola")
        # 2. Cerca una traduzione
        print("2) Cerca una traduzione")
        # 3. Cerca con wildcard
        print("3) Cerca con wildcard")
        # 4. Exit
        print("4) Exit")

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        # File format (one entry per line):
        # <parola_aliena> <traduzione1> <traduzione2> ...
        file = open(dict, "r")
        for riga in file:
            riga = riga.strip()
            if riga == "":
                continue

            parti = riga.split()
            if len(parti) < 2:
                continue

            alien = parti[0]
            translations = parti[1:]  # lista di traduzioni
            self.dictionary.addWord(alien, translations)

        file.close()

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        if entry is None or len(entry) < 2:
            print("Formato non valido.")
            return

        alien = entry[0]
        translations = list(entry[1:])
        self.dictionary.addWord(alien, translations)
        self.dictionary.saveWord("dictionary.txt", alien, translations)
        print("Aggiunta completata.")

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        if query is None:
            print("Query non valida.")
            return

        alien = query.lower()
        if alien in self.dictionary:
            print("Traduzioni:", " ".join(self.dictionary[alien]))
        else:
            print("Parola non trovata.")

    def handleWildCard(self,query):
        # query is a string with a ? --> <parola_aliena>
        if query is None:
            print("Query non valida.")
            return

        #Normalizzazione
        pattern = query.lower()
        #Lista dei risultati
        matches = []

        #All the keys saved in dict
        for alien in self.dictionary.keys():
            #Lunghezze devono matchare
            if len(alien) != len(pattern):
                continue
            #Assumendo match:
            ok = True
            #Confronto carattere per carattere
            for i in range(len(pattern)):
                if pattern[i] == "?":
                    continue
                if pattern[i] != alien[i]:
                    ok = False
                    break

            if ok:
                matches.append(alien)

        if len(matches) == 0:
            print("Nessuna corrispondenza.")
        else:
            print("Corrispondenze trovate:")
            for w in matches:
                print("-", w, "->", " ".join(self.dictionary[w]))