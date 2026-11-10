class Dictionary:
    def __init__(self):
        self.data={}

    def addWord(self,alien,translations):
        """
        alien: string
        translations: string oppure lista di stringhe
        """
        alien = alien.lower()

        #Normalizzo translations a lista
        if isinstance(translations, str):
            translations = [translations]
        translations = [t.lower() for t in translations]

        if alien not in self.data:
            self.data[alien] = []

        for tr in translations:
            if tr not in self.data[alien]:
                self.data[alien].append(tr)

    def translate(self,alien):
        """Ritorna lista traduzioni o none se non trovato"""
        alien = alien.lower()
        return self.data.get(alien, None)

    def translateWordWildCard(self,pattern):
        """ pattern contiene '?' che matcha un singolo carattere.
        Ritorna lista di parole aliene che matchano"""
        pattern = pattern.lower()
        matches = []

        for alien in self.data.keys():
            if len(alien) != len(pattern):
                continue

            ok = True
            for i in range(len(pattern)):
                if pattern[i] == "?":
                    continue
                if pattern[i] != alien[i]:
                    ok = False
                    break

            if ok:
                matches.append(alien)

        return matches

    def saveWord(self, filename, alien, translations):
        alien = alien.lower()

        if isinstance(translations, str):
            translations = [translations]
        translations = [t.lower() for t in translations]

        with open(filename, "a") as file:  # <-- APPEND MODE
            file.write(alien + " " + " ".join(translations) + "\n")
        file.close()