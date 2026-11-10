# Lab 01

## Trivia Game

Si vuole realizzare un programma in Python per gestire un gioco di Trivia, basato su domande di cultura generale.

Tutte le domande sono elencate nel file "domande.txt". Ogni domanda è memorizzata in sei righe consecutive:
- la prima riga contiene il testo della domanda
- la seconda riga contiene un numero intero positivo, che indica il livello di difficoltà della domanda
- la terza riga contiene la risposta corretta
- la quarta, quinta e sesta riga contengono le risposte errate.

Tra una domanda e la successiva è presente una riga vuota.

***Esempio file "domande.txt"***
```
Capitale dell'Italia?
0
Roma
Milano
Berlino
Parigi

Autore del dipinto "L'urlo"?
2
Edvard Munch
Vincent van Gogh
Pablo Picasso
Claude Monet

Lingua ufficiale del Brasile?
0
Portoghese
Spagnolo
Inglese
Francese
		
Elemento chimico con simbolo "H"?
1
Idrogeno
Ossigeno
Carbonio
Ferro
```

Il numero totale di domande e il numero di domande per ogni livello di difficoltà non sono noti a priori. Il livello massimo di difficoltà non è noto a priori: si garantisce però che il livello minimo è zero e sono presenti domande per ogni livello successivo (fino al livello massimo). Le domande nel file "domande.txt" non sono ordinate in base al livello di difficoltà.

Il programma deve proporre una domanda e la lista di risposte. La domanda proposta è selezionata casualmente dal livello di difficoltà corrente. Anche la risposte proposte devono essere stampate in ordine casuale.

Il gioco comincia proponendo una domanda di livello di difficoltà 0. Se il giocatore risponde correttamente, il programma incrementa di 1 il livello di difficoltà e propone una nuova domanda. Il gioco termina quando il giocatore ha dato una risposta errata oppure quando risponde correttamente ad una domanda di livello massimo.

Per ogni risposta corretta, il giocatore guadagna un punto. Al termine del gioco, il programma visualizza il punteggio raggiunto e chiede al giocatore di inserire il proprio nickname. 

Infine, il programma deve salvare nel file "punti.txt" il punteggio raggiunto, nel formato *Nickname punteggio*. In particolare, il file è già presente, e quindi va aggiornato. Le informazioni contenute nel file sono la lista di elementi *Nickname punteggio* delle partite precedenti.  

Considerando che il file può contenere anche altre righe, il file di output deve essere salvato inserendo i punteggi dei giocatori in ordine decrescente di punteggio.

HINTS:
- Definire la classe "domanda" che abbia come attributi tutte le caratteristiche della domanda da sottoporre all'utente.
- La logica del gioco in una prima fase può essere interamente contenuta in un file di main.
- Valutare come ulteriore miglioria la possibilità di definire una classe "game" che gestisca le dinamiche di gioco, da chiamare nel file di main, insieme ad una classe Player per gestire una lista di giocatori e punteggi. 

***Esempio file "punti.txt"***
```
Paolo 4
Lucia 1
Mario 1
Giuseppe 0
```

***Esempio di esecuzione***

```
Livello 0) Lingua ufficiale del Brasile?
        1. Spagnolo  
        2. Francese  
        3. Portoghese
        4. Inglese
Inserisci la risposta: 3
Risposta corretta!

Livello 1) Elemento chimico con simbolo "H"?
        1. Ferro
        2. Idrogeno
        3. Carbonio
        4. Ossigeno
Inserisci la risposta: 2
Risposta corretta!

Livello 2) Autore del dipinto "L'urlo"?
        1. Edvard Munch
        2. Claude Monet
        3. Pablo Picasso
        4. Vincent van Gogh
Inserisci la risposta: 4
Risposta sbagliata! La risposta corretta era: 1

Hai totalizzato 2 punti!
Inserisci il tuo nickname: Marta

```

Al termine dell'esempio risultato, il contenuto del file "punti.txt" è il seguente:
***Esempio file "punti.txt"***
```
Paolo 4
Marta 2
Lucia 1
Mario 1
Giuseppe 0
```
