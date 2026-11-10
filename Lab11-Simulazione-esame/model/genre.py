from dataclasses import dataclass

@dataclass
class Genre:
    GenreId:int
    Name:str

 #Conterrà una serie di metodi: hash, eq e str
    def __hash__(self):
        return hash(self.GenreId)

    def __eq__(self, other):
        #Due oggetti saranno uguali se avranno la stessa chiave primaria
        return self.GenreId == other.GenreId

    #Metodo che useremo quando vogliamo stampare questo oggetto
    def __str__(self):
        #Che informazioni ci potrebbero interessare? t
        return f"{self.Name}"
