from dataclasses import dataclass

@dataclass
class Track:
    TrackId:int
    Name:str
    AlbumId:int
    MediaTypeId:int
    GenreId:int
    Composer:str
    Milliseconds:int
    Bytes:int
    UnitPrice:float

#Conterrà una serie di metodi: hash, eq e str
    def __hash__(self):
        return hash(self.TrackId)

    def __eq__(self, other):
        #Due oggetti saranno uguali se avranno la stessa chiave primaria
        return self.TrackId == other.TrackId

    #Metodo che useremo quando vogliamo stampare questo oggetto
    def __str__(self):
        #Che informazioni ci potrebbero interessare?
        return f"{self.TrackId} - Album: {self.AlbumId}"
