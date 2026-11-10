from dataclasses import dataclass

@dataclass
class Artist:
    ArtistId:int
    Name:str

#Conterrà una serie di metodi: hash, eq e str
    def __hash__(self):
        return hash(self.ArtistId)

    def __eq__(self, other):
        #Due oggetti saranno uguali se avranno la stessa chiave primaria
        return self.ArtistId == other.ArtistId

    #Metodo che useremo quando vogliamo stampare questo oggetto
    def __str__(self):
        #Che informazioni ci potrebbero interessare? t
        return f"{self.Name}"
