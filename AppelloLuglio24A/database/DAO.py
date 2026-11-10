from database.DB_connect import DBConnect
from model.state import State
from model.sighting import Sighting

class DAO():
    def __init__(self):
        pass

    #TENDINA ANNO (ordine descrescente)
    def getAllYears():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT DISTINCT YEAR(datetime) AS year
            FROM sighting s 
            ORDER BY year DESC;
        """
        cursor.execute(query)

        # QUESTO è QUELLO CHE DEVI NOTARE:
        result = []
        for row in cursor:
            result.append(row["year"])

        cursor.close()
        conn.close()
        return result

    #TENDINA FORMA (ordine descrescente)
    def getAllShapes():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT DISTINCT shape
        FROM sighting s 
        ORDER BY "shape" ASC    
        """
        cursor.execute(query)

        result = []
        for row in cursor:
            result.append(row["shape"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all_states():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select * 
                    from state s"""
            cursor.execute(query)

            for row in cursor:
                result.append(
                    State(row["id"],
                          row["Name"],
                          row["Capital"],
                          row["Lat"],
                          row["Lng"],
                          row["Area"],
                          row["Population"],
                          row["Neighbors"]))

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_all_sightings():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select * 
                    from sighting s 
                    order by `datetime` asc """
            cursor.execute(query)

            for row in cursor:
                result.append(Sighting(**row))
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def getNodes(year,shape):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """
                SELECT *
                FROM sighting s
                WHERE YEAR(s.datetime) = %s
                AND s.shape = %s
            """
        cursor.execute(query, (year, shape))

        result = []
        for row in cursor:
            result.append(Sighting(**row))

        cursor.close()
        conn.close()

        return result

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
            s1.id AS v1,
            s2.id AS v2
        FROM sighting s1
        JOIN sighting s2 ON s1.state =s2.state
        WHERE s1.state = s2.state
        """

        cursor.execute(query)
        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result