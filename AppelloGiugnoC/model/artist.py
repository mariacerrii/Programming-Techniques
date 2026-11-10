from dataclasses import dataclass, field

@dataclass
class Artist:
    ArtistId: int
    Name: str

    #ELEMENTI AGGIUNTI CONSGLIATI DAL TESTO
    # Lista di tutti i brani dell'artista
    tracks: list = field(default_factory=list)
    # Insieme delle playlist in cui compare almeno un suo brano
    playlists: set = field(default_factory=set)

    def __hash__(self):
        return hash(self.ArtistId)

    def __eq__(self, other):
        if not isinstance(other, Artist):
            return NotImplemented
        return self.ArtistId == other.ArtistId

    def __str__(self):
        return f"{self.Name}"