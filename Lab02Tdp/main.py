import translator as tr
t = tr.Translator()
#First of all, read the dictionary
t.loadDictionary("dictionary.txt")

while(True):
    t.printMenu()
    scelta = input("Scelta:")
    print("1) Inserisci parola")
    print("2) Cerca parola")
    print("3) Esci")

    # Input control, it may be 1/2/3
    if scelta not in ["1", "2", "3"]:
        print("Scelta non valida.")
        continue

    if scelta == "1":
        aliena=input("Parola aliena:")
        traduzione = input("Traduzione:")
        t.handleAdd((aliena, traduzione))
        #txtIn = input()
    elif scelta == "2":
        aliena = input("Parola aliena: ")
        t.handleTranslate(aliena)
    elif scelta == "3":
        pattern = input("Pattern con ?: ")
        t.handleWildCard(pattern)

    elif scelta == "4":
        print("Uscita.")
        break

        #ciaoooo