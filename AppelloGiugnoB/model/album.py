from dataclasses import dataclass, field

@dataclass
class Album:
    AlbumId: int
    Title:str
    ArtistId:int

    #ELEMENTI AGGIUNTI CONSGLIATI DAL TESTO
    # Lista di tutti i brani di quell'album
    tracks: list = field(default_factory=list)

    def __hash__(self):
        return hash(self.AlbumId)

    def __eq__(self, other):
        if not isinstance(other, Album):
            return NotImplemented
        return self.AlbumId == other.AlbumId

    def __str__(self):
        return f"{self.AlbumId}"

