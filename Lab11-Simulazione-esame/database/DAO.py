from database.DB_connect import DBConnect
from model.genre import Genre
from model.artist import Artist

class DAO():
    @staticmethod
    def getAllGenres():
            # Nodi --> elementi Generi
            conn = DBConnect.get_connection()
            result = []
            cursor = conn.cursor(dictionary=True)
            query = """SELECT *
                    from Genre g 
                    """
            #order by g.Name
            cursor.execute(query)
            for row in cursor:
                # genre definito in un altro file (creato)
                result.append(Genre(**row))
                #results.append(row["Name"])
            cursor.close()
            conn.close()
            return result

    @staticmethod
    def getAllArtists(genere):
        #Vertici --> Artisti
        #Possiedono ALMENO un brano track appartente al genere
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT a.ArtistId, a.Name
                FROM Artist a
                JOIN Album a2 ON a.ArtistId = a2.ArtistId
                JOIN Track t ON a2.AlbumId = t.AlbumId
                JOIN Genre g ON t.GenreId = g.GenreId
                WHERE g.GenreId = %s  """
        #DISTINCT evita di ottenere più volte lo stesso artista
        #RIGA 3: Collego Artist ad Album tramite ArtistId - Ogni album appartiene a un artista
        #RIGA 4: Collego Album a Track tramite AlbumId
        #RIGA 5: Collego Track a Genre tramite GenreId
        #WHERE: Filtro i risultati in base al genere selezionato. In questo esempio GenreId = 1 corrisponde a Rock.

        #cursor.execute(query,(genere.GenreId,)) #ATTENTA A SECONDA VOCE
        cursor.execute(query, (genere.GenreId,))
        for row in cursor:
            # genre definito in un altro file (creato)
            result.append(Artist(**row))
        cursor.close()
        conn.close()
        return result



    #2 METODI
    # 1) .getPopolarita(v1) → un solo artista
    #DA UN ARTISTA RICEVIAMO LA SUA POPOLARITA
    #DA TESTO: PESO è SOMMA DUE POPOLARITA

    #@staticmethod
    #def getPopolarita(v1):
        # Calcola la popolarità di un artista
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """SELECT a.ArtistId,
                    SUM(il.Quantity) AS popolarita
                    FROM Artist a
                    JOIN Album al ON a.ArtistId = al.ArtistId
                    JOIN Track t ON al.AlbumId = t.AlbumId
                    JOIN InvoiceLine il ON t.TrackId = il.TrackId
                    WHERE a.ArtistId = %s
                    GROUP BY a.ArtistId
                """
        cursor.execute(query, (v1.ArtistId,))
        # Recupero una sola riga --> .fetchone()
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row is not None:
            return row["popolarita"]
        return 0

    @staticmethod
    def getCustomerArtistCounts(genere):
        conn = DBConnect.get_connection()
        results = []
        cursor = conn.cursor(dictionary=True)
        query = """select i.CustomerId, art.ArtistId, count(*) as ntracks
                          from invoice i, invoiceline i2, track t, genre g, artist art,album a
                          where i.InvoiceId  = i2.InvoiceId 
                          and t.TrackId = i2.TrackId 
                          and t.AlbumId = a.AlbumId
                          and g.GenreId = t.GenreId
                          and art.ArtistId = a.ArtistId 
                          and g.Name = %s
                          group by i.CustomerId, art.ArtistId"""
        cursor.execute(query, (genere.Name,))
        for row in cursor:
            results.append((row["CustomerId"], row["ArtistId"], row["ntracks"]))
        cursor.close()
        conn.close()
        return results


