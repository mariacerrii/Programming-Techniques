from database.DB_connect import DBConnect
from model.album import Album
#dao
class DAO:
    @staticmethod
    def getAllAlbums():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
           SELECT DISTINCT a.AlbumId, a.Title, a.ArtistId
            FROM Album a
            JOIN Track t ON a.AlbumId = t.AlbumId
        """
        cursor.execute(query)
        result = [Album(**row) for row in cursor]
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """
               SELECT DISTINCT
            t1.AlbumId AS v1,
            t2.AlbumId AS v2
            FROM Track t1
            JOIN Track t2 ON t1.GenreId = t2.GenreId
            WHERE t1.AlbumId < t2.AlbumId
           """

        cursor.execute(query)
        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllCountries():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """
                select distinct c.Country
                from customer c
                where c.Country is not null
                order by c.Country
                """

        cursor.execute(query)

        for row in cursor:
            results.append(row["Country"])

        cursor.close()
        conn.close()
        return results

