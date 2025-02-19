#Clase sport

class Sport:
    #Clase para representar un depporte
    def __init__(self, name:str, players:int, league:str):
        self.name = name
        
        if isinstance(players,int): #Verificamos que sea un entero
            self.players = players
        else:
            self.players = int(players)
        self.league = league
        
    def __str__ (self):
        return f"Sport:{self.name}, {self.players}, {self.league}"
    
    def __repr__(self): #Metodo para reprentar la clase como String
        return f"Sport(name={self.name}',players = {self.players}, league = '{self.league}')"
    
    def to_jason(self)->dict: #Metodo para representar la clase como diccionario
        return {"name":self.name, "players":self.players, "league":self.league}
    
if __name__ == "__main__":
    s = Sport("Boloncesto", 11, "FIFA")
    print(s)
    print(repr(s))  
    print(s.to_jason())
    
    nfl = Sport("Football", 11, "NFL")
    lmp = Sport("Baseball", 9, "LMP")
    mlb = Sport("Soccer", 11, "MLS")
    nba = Sport("Basketball", 5, "NBA")
            
    lista_deportes = [nfl,lmp,mlb,nba]
    archivo_deportes = "deportes.txt"
    with open (archivo_deportes, "w") as file:
        for d in lista_deportes:
            file.write(repr(d) + "\n")
            
    sport_list = []
    with open(archivo_deportes, "r") as file:
        for line in file:
            d  = eval(line)
            sport_list.append(d)
    print(sport_list)
    print()
    print(sport_list[0].to_json())
    
    """import json
    archivo_json = "deportes.json"
    with open(archivo_json, "w") as file:
        for d in sport_list:
            json.dump(d.to_json(),file)
            file.write("\n")
            
    #Leemos el archivo json
    sport_list_json = []"""