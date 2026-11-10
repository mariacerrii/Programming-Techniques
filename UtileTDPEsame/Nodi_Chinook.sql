--SQL PER NODI FATTI PER DATABSE CHINOOK
La cosa fondamentale: DISTINCT evita i duplicati, mentre WHERE applica il filtro richiesto.
--Traccia 29 giugno 2026 – B:
--I vertici sono gli album che contengono almeno un brano presente nella tabella Track.
DISTINCT --> Un album può contenere più brani.

SELECT DISTINCT a.AlbumId, a.Title, a.ArtistId
FROM Album a
JOIN Track t ON a.AlbumId = t.AlbumId"""

--Traccia 29 giugno 2026 – C:
--I vertici sono gli artisti che hanno almeno un brano presente nella tabella Track, tramite i rispettivi album
SELECT DISTINCT a.ArtistId, a.Name
FROM Artist a
JOIN Album a2 ON a2.ArtistId =a.ArtistId
JOIN Track t ON t.AlbumId =a2.AlbumId .

--Traccia 29 giugno 2026 – A:
--I vertici sono tutti i clienti (Customer) che risiedono in un paese selezionato dall’utente
--e che hanno effettuato almeno un acquisto,
--cioè possiedono almeno una fattura nella tabella Invoice.
 SELECT c.*, SUM(i.Total) AS Fatturato
FROM Customer c
JOIN Invoice i ON i.CustomerId = c.CustomerId
#selezionato da utente
WHERE c.Country =%s
GROUP BY c.CustomerId;

--Simulazione 11
--I vertici del grafo sono tutti gli artisti (Artist) che possiedono
--almeno un brano (Track) appartenente a un genere musicale selezionato dall’utente.
SELECT DISTINCT a.ArtistId, a.Name
FROM Artist a
JOIN Album a2 ON a2.ArtistId = a.ArtistId
JOIN Track t ON t.AlbumId = a2.AlbumId
JOIN Genre g ON g.GenreId = t.GenreId
WHERE g.Name = %s;

-- ATTENZIONE AL FILTRO:
-- Se la tendina restituisce il NOME (es. "Rock"):
--     WHERE g.Name = %s
--
-- Se la tendina restituisce l'ID (es. 1):
--     WHERE t.GenreId = %s
-- Non serve JOIN Genre se filtri direttamente per t.GenreId.

SELECT DISTINCT a.ArtistId, a.Name
FROM Artist a
JOIN Album al ON al.ArtistId = a.ArtistId
JOIN Track t ON t.AlbumId = al.AlbumId
JOIN Genre g ON g.GenreId = t.GenreId
WHERE g.Name = %s;

--ESERCIZI AGGIUNTI CHAT
--I vertici sono tutti i dipendenti (Employee) che risultano assegnati
--come responsabili di almeno un cliente (Customer).
SELECT DISTINCT e.EmployeeId, e.FirstName, e.LastName
FROM Employee e
JOIN Customer c ON e.EmployeeId = c.SupportRepId;

--playlist con almeno un brano Rock:
SELECT DISTINCT p.PlaylistId, p.Name
FROM Playlist p
JOIN PlaylistTrack pt ON p.PlaylistId = pt.PlaylistId
JOIN Track t ON pt.TrackId = t.TrackId
JOIN Genre g ON t.GenreId = g.GenreId
WHERE g.Name = %s;

--I vertici sono tutti i brani (Track) appartenenti a un genere musicale selezionato dall’utente.
SELECT DISTINCT t.TrackId
FROM Track t
JOIN Genre g ON g.GenreId =t.GenreId
WHERE g.GenreId =%s

--I vertici del grafo sono tutte le playlist (Playlist)
--che contengono almeno un brano (Track)
--appartenente a un genere musicale selezionato dall’utente.
SELECT DISTINCT p.PlaylistId, p.Name
FROM Playlist p
JOIN PlaylistTrack pt ON pt.PlaylistId = p.PlaylistId
JOIN Track t ON t.TrackId = pt.TrackId
JOIN Genre g ON t.GenreId = g.GenreId
WHERE g.Name = %s

--I vertici sono tutti i clienti (Customer) che hanno acquistato
--almeno un brano appartenente a un genere musicale selezionato dall’utente
SELECT DISTINCT c.CustomerId, c.FirstName, c.LastName
FROM Customer c
JOIN Invoice i ON i.CustomerId = c.CustomerId
JOIN InvoiceLine il On il.InvoiceId =i.InvoiceId
JOIN Track t ON t.TrackId =il.TrackId
JOIN Genre g ON g.GenreId =t.GenreId
WHERE g.GenreId =%s

--I vertici rappresentano tutti gli album (Album) che contengono almeno un brano (Track)
--acquistato da un cliente (Customer) residente in un Paese selezionato dall’utente.
SELECT DISTINCT a.AlbumId, a.Title, a.ArtistId
FROM Album a
JOIN Track t ON a.AlbumId = t.AlbumId
JOIN InvoiceLine il ON il.TrackId =t.TrackId
JOIN Invoice i ON i.InvoiceId =il.InvoiceId
JOIN Customer c ON c.CustomerId = i.CustomerId
WHERE c.Country =%s
GROUP BY a.AlbumId, a.Title, a.ArtistId

---DIPENDENTI E RESPONSABILI
--NODI: tutti i dipendenti presenti nella tabella Employee.
SELECT e.EmployeeId, e.FirstName, e.LastName
FROM Employee e



