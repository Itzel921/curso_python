class Athlete:
    #Athelte class, whit only name attribute
    
    def __init__(self, name:str):
        self.name = name
    
    def __str__(self):  
        return f"Athlete: {self.name}"
    
    def __repr__(self):
        return f"Athlete('{self.name}')"
    
    def display(self):
        print(f"{self.name}")
        
        
if __name__ == "__main__":
    a = Athlete("John Adalberto")
    a.display() #Es como se va a mostrar la cadena
    print(a)
    print(repr(a)) #El repr es como se debe de representar/ como se hizo esa cadena
    print(f"a: {id(a)}")
     
    b = eval(repr(a)) #Hace una copia de a
    print(b)
    print(f"b: {id(b)}")
