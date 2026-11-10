from dataclasses import dataclass, field

@dataclass
class Customer:
    CustomerId: int
    FirstName: str
    LastName: str
    Company:str
    Address:str
    City:str
    State:str
    Country:str
    PostalCode:str
    Phone:str
    Fax:str
    Email:str
    SupportRepId:int
    #NUOVA VOCE ALLA CLASSE
    Fatturato: float


    def __hash__(self):
        return hash(self.CustomerId)

    def __eq__(self, other):
        if not isinstance(other, Customer):
            return NotImplemented
        return self.CustomerId == other.CustomerId

    def __str__(self):
        return f"{self.FirstName} {self.LastName} ({self.Country})"