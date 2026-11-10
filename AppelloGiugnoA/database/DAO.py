from database.DB_connect import DBConnect
from model.customer import Customer

class DAO():
    @staticmethod
    #CLIENTI PER FATTURATO
    def getAllCustomers(country):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """
               SELECT c.*, SUM(i.Total) AS Fatturato
        FROM Customer c
        JOIN Invoice i ON i.CustomerId = c.CustomerId
        WHERE c.Country = %s
        GROUP BY c.CustomerId, c.FirstName, c.LastName
        ORDER BY c.CustomerId
                """
        #CI INTERESSA ALTRO ELEMENTO
        cursor.execute(query, (country,))
        #oggetti nella dataclass
        for row in cursor:
            results.append(Customer(**row))
        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllEdges():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """
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
        """

        cursor.execute(query)
        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

    # TENDINA: 1) DAO.py — Recuperare i valori della tendina
    @staticmethod
    def getAllCountries():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
             SELECT DISTINCT c.Country
             FROM Customer c
             WHERE c.Country IS NOT NULL
             ORDER BY c.Country
        """

        cursor.execute(query)
        result = []

        for row in cursor:
            #ATTENTA A QUESTA RIGA
            result.append(row["Country"])

        cursor.close()
        conn.close()
        return result