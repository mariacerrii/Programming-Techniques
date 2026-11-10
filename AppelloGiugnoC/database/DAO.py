from database.DB_connect import DBConnect
from model.track import Track
from model.artist import Artist

class DAO():
    @staticmethod
    def getAllArtists():
        # Vertici --> Artisti che hanno almeno un brano

        # nella tabella Track, tramite Album

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
               SELECT DISTINCT a.ArtistId, a.Name
               FROM Artist a
               JOIN Album a2 ON a.ArtistId = a2.ArtistId
               JOIN Track t ON a2.AlbumId = t.AlbumId
           """
        cursor.execute(query)
        for row in cursor:
            result.append(Artist(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT ap1.ArtistId AS Artist1, ap2.ArtistId AS Artist2, COUNT(*) AS peso
            FROM ( SELECT DISTINCT al.ArtistId, pt.PlaylistId
            FROM Album al
            JOIN Track t ON al.AlbumId = t.AlbumId
            JOIN PlaylistTrack pt ON t.TrackId = pt.TrackId) ap1
            JOIN ( SELECT DISTINCT al.ArtistId, pt.PlaylistId
            FROM Album al
            JOIN Track t ON al.AlbumId = t.AlbumId
            JOIN PlaylistTrack pt ON t.TrackId = pt.TrackId) ap2 ON ap1.PlaylistId = ap2.PlaylistId
            WHERE ap1.ArtistId < ap2.ArtistId
            GROUP BY ap1.ArtistId, ap2.ArtistId"""

        cursor.execute(query)
        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return result
