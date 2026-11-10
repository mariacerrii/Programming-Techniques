-- ARCHI NON ORIENTATI
-- Evitare autoarchi e coppie inverse
WHERE t1.ID < t2.ID

-- ARCHI ORIENTATI
-- Evitare soltanto autoarchi
--ENTRAMBI I VERSI
WHERE t1.ID != t2.ID
-- DAL PIù VECCHIO AL PIù RECENTE
WHERE t1.Data < t2.Data

--29 giugno 2026, tipologia B
--Il grafo non orientato e non pesato.
--I nodi del grafo sono gli album che contengono almeno un brano
ARCHI
--Due album distinti sono collegati da un arco se contengono
--almeno un brano appartenente allo stesso genere musicale

SELECT DISTINCT
    t1.AlbumId AS v1,
    t2.AlbumId AS v2
FROM Track t1
JOIN Track t2 ON t1.GenreId = t2.GenreId
WHERE t1.AlbumId < t2.AlbumId

--29 giugno 2026, tipologia C
--grafo non orientato e pesato
-- I nodi rappresentano gli artisti presenti nel database che hanno pubblicato almeno un brano musicale.
ARCHI
--Due artisti distinti sono collegati da un arco se esiste almeno una playlist
--che contiene almeno un brano di entrambi gli artisti.
PESO DEGLI ARCHI
--Il peso di un arco è pari al numero di playlist distinte condivise dai due artisti.
SELECT
    a1.ArtistId AS v1,
    a2.ArtistId AS v2,
    COUNT(DISTINCT pt1.PlaylistId) AS peso
FROM Artist a1

JOIN Album al1 ON al1.ArtistId = a1.ArtistId
JOIN Track t1 ON t1.AlbumId = al1.AlbumId
JOIN PlaylistTrack pt1 ON pt1.TrackId = t1.TrackId
-- METTI CONFRONTO ENTRAMBI
JOIN PlaylistTrack pt2 ON pt2.PlaylistId = pt1.PlaylistId
--rifai lo stesso al contrario
JOIN Track t2 ON t2.TrackId = pt2.TrackId
JOIN Album al2 ON al2.AlbumId = t2.AlbumId
JOIN Artist a2 ON a2.ArtistId = al2.ArtistId
--condizione NON ORIENTATO
WHERE a1.ArtistId < a2.ArtistId

GROUP BY a1.ArtistId, a2.ArtistId

--GIUGNO TIPOLOGIA A
--grafo orientato e pesato
--I nodi rappresentano i clienti appartenenti a un Paese selezionato dall’utente che hanno effettuato almeno un acquisto.
ARCHI
DUE QUERY:
Prima query SQL → NODI + FATTURATO
--A ogni cliente è associato il suo fatturato totale, calcolato sommando gli importi delle sue fatture

Seconda query SQL → INFORMAZIONI PER GLI ARCHI
--Due clienti distinti sono collegati se hanno acquistato almeno un brano dello stesso artista.

DIREZIONE
L’arco è orientato:
* Dal cliente con fatturato maggiore a quello con fatturato minore.
* Se i fatturati sono uguali, vengono creati due archi, uno per ogni direzione.

PESO --> Il peso dell’arco è la somma dei fatturati totali dei due clienti

--Prima: ho preso nodi e l'ho aggiornata
SELECT c.CustomerId, c.FirstName, c.LastName, SUM(i.Total) AS Fatturato
FROM Customer c
JOIN Invoice i ON i.CustomerId = c.CustomerId
WHERE c.Country = %s
GROUP BY c.CustomerId, c.FirstName, c.LastName
ORDER BY c.CustomerId

ARCHI --> HO GESTITO LE COPPIE
SELECT DISTINCT
    c1.CustomerId AS v1,
    c2.CustomerId AS v2
FROM Customer c1
JOIN Invoice i1 ON i1.CustomerId = c1.CustomerId
JOIN InvoiceLine il1 ON il1.InvoiceId = i1.InvoiceId
JOIN Track t1 ON t1.TrackId = il1.TrackId
JOIN Album al1 ON al1.AlbumId = t1.AlbumId
JOIN Album al2 ON al2.ArtistId = al1.ArtistId
JOIN Track t2 ON t2.AlbumId = al2.AlbumId
JOIN InvoiceLine il2 ON il2.TrackId = t2.TrackId
JOIN Invoice i2 ON i2.InvoiceId = il2.InvoiceId
JOIN Customer c2 ON c2.CustomerId = i2.CustomerId
WHERE c1.CustomerId < c2.CustomerId


-- SIMU11 - ARCHI
-- Due artisti sono collegati se almeno un cliente
-- ha acquistato brani di entrambi.
-- SQL: recupera le coppie di artisti.
-- MODEL: gestisce direzione e peso.
-- < evita coppie duplicate e autoarchi.

SELECT DISTINCT
    al1.ArtistId AS v1,
    al2.ArtistId AS v2

FROM Invoice i1
JOIN InvoiceLine il1 ON il1.InvoiceId = i1.InvoiceId
JOIN Track t1 ON t1.TrackId = il1.TrackId
JOIN Album al1 ON al1.AlbumId = t1.AlbumId

JOIN Invoice i2 ON i2.CustomerId = i1.CustomerId
JOIN InvoiceLine il2 ON il2.InvoiceId = i2.InvoiceId
JOIN Track t2 ON t2.TrackId = il2.TrackId
JOIN Album al2 ON al2.AlbumId = t2.AlbumId

WHERE al1.ArtistId < al2.ArtistId;

-- ESERCIZI CHAT

--ORDINE DA PIù VECCHIA A PIù RECENTE
--grafo orientato e non pesato.
-- Nodi: tutte le fatture presenti nella tabella Invoice.
--Archi: due fatture sono collegate se:
    --Appartengono allo stesso cliente.
    --Hanno date differenti.
    -- L’arco è diretto dalla fattura più vecchia a quella più recente.
SELECT
    i1.InvoiceId AS v1,
    i2.InvoiceId AS v2

FROM Invoice i1

JOIN Invoice i2
    ON i1.CustomerId = i2.CustomerId
--> QUI DEFINISCE SIA CHE SONO DIVERSE SIA ORDINE ARCO
WHERE i1.InvoiceDate < i2.InvoiceDate;


-- grafo non orientato e non pesato
--NODI: tutti i clienti (Customer) che hanno effettuato almeno un acquisto.
--ARCHI: due clienti distinti sono collegati se hanno acquistato almeno uno stesso brano musicale (Track).
SELECT DISTINCT
    c1.CustomerId AS v1,
    c2.CustomerId AS v2
FROM Customer c1
JOIN Invoice i1 ON i1.CustomerId = c1.CustomerId
JOIN InvoiceLine il1 ON il1.InvoiceId = i1.InvoiceId
JOIN InvoiceLine il2 ON il2.TrackId = il1.TrackId
JOIN Invoice i2 ON i2.InvoiceId = il2.InvoiceId
JOIN Customer c2 ON c2.CustomerId = i2.CustomerId
WHERE c1.CustomerId < c2.CustomerId


--NODI: tutti i clienti (Customer) che hanno effettuato almeno un acquisto.
--ARCHI: due clienti distinti sono collegati se hanno acquistato almeno un brano appartenente allo stesso genere musicale (Genre).
-- PESO: il numero di generi musicali distinti acquistati da entrambi i clienti.
SELECT
    c1.CustomerId AS v1,
    c2.CustomerId AS v2,
    COUNT(DISTINCT t1.GenreId) AS peso
FROM Customer c1
JOIN Invoice i1 ON i1.CustomerId = c1.CustomerId
JOIN InvoiceLine il1 ON il1.InvoiceId = i1.InvoiceId
JOIN Track t1 ON t1.TrackId = il1.TrackId
JOIN Track t2 ON t1.GenreId = t2.GenreId
JOIN InvoiceLine il2 ON il2.TrackId = t2.TrackId
JOIN Invoice i2 ON i2.InvoiceId = il2.InvoiceId
JOIN Customer c2 ON c2.CustomerId = i2.CustomerId
WHERE c1.CustomerId < c2.CustomerId
GROUP BY c1.CustomerId, c2.CustomerId;


--ARCHI: esiste un arco orientato dal dipendente al suo responsabile diretto
SELECT
    e.EmployeeId AS v1,
    e.ReportsTo AS v2
FROM Employee e
WHERE e.ReportsTo IS NOT NULL;

--PLAYLIST CON BRANI IN COMUNE
--ARCHI: due playlist distinte sono collegate se condividono almeno un brano (Track).
--PESO: il numero di brani distinti condivisi dalle due playlist.
SELECT
    pt1.PlaylistId AS v1,
    pt2.PlaylistId AS v2,
    COUNT(DISTINCT pt1.TrackId) AS peso

FROM PlaylistTrack pt1
JOIN PlaylistTrack pt2
    ON pt1.TrackId = pt2.TrackId
WHERE pt1.PlaylistId < pt2.PlaylistId
GROUP BY pt1.PlaylistId, pt2.PlaylistId;

--BRANI STESSO ALBUM
--ARCHI: due brani distinti sono collegati se appartengono allo stesso album
SELECT
    t1.TrackId AS v1,
    t2.TrackId AS v2
FROM Track t1
JOIN Track t2 ON t1.AlbumId = t2.AlbumId
WHERE t1.TrackId < t2.TrackId;

-- GRUPO BY + HAVING (ALMENO 10 BRAVI)
--I vertici del grafo rappresentano tutti gli artisti che hanno pubblicato almeno 10 brani musicali.
SELECT a.ArtistId, a.Name,
    COUNT(t.TrackId) AS NumeroBrani
FROM Artist a
JOIN Album al ON al.ArtistId = a.ArtistId
JOIN Track t ON t.AlbumId = al.AlbumId
GROUP BY a.ArtistId, a.Name
HAVING COUNT(t.TrackId) >= 10;

--NOTA
-- WHERE: filtra le righe
WHERE t.GenreId = %s

-- HAVING: filtra i gruppi
HAVING COUNT(t.TrackId) >= 10