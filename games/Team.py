#Clase Team: Equipo

from Athlete import Athlete
from Sport import Sport

class Team:
    #Clase para representar un equipo
    
    def __init__(self, name:str, sport:Sport, players:list):
        self.name = name
        self.sport = sport
        self.players = players	
    
    def __str__(self):
        return f"Team: {self.name}, {self.sport}, {self.players}"

    def __repr__(self): #Metodo para representar la clase como string
        return f"Team(name='{self.name}', sport={repr(self.sport)}, players={self.players})"
        
    def to_json(self)->dict: #Metodo para reprensetar la clase como diccionario
        return{"name":self.name, "sport":self.sport.to_json(), "players":[p.to_json() for p in self.players]}
    
if __name__ == "__main__":
    atleta1 = Athlete("John Adalberto")
    atleta2 = Athlete("Juan Perez")
    atleta3 = Athlete("Maria Lopez")
    atleta4 = Athlete("Pedro Martinez")
    atleta5 = Athlete("Ana Lopez")
    
    sdeporte = Sport("Basseball", 9, "MLB")
    lakers = Team("Los angeles azules", sdeporte, [atleta1, atleta2, atleta3, atleta4, atleta5])
    print(lakers)
    print(repr(lakers))
