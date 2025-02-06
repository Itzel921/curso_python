'''tablero.py: Dibuja el tablero del juego del gato'''
import random

def dibuja_tablero(simbolos: dict):
    '''
    Dibuja tablero del juego de el gato
    '''
    print(f'''
    {simbolos['1']} | {simbolos['2']} | {simbolos['3']}
    ---------
    {simbolos['4']} | {simbolos['5']} | {simbolos['6']}
    ---------
    {simbolos['7']} | {simbolos['8']} | {simbolos['9']}
    ''')


def ia(simbolos: dict):
    """Estrategia de la computadora"""
    ocupado = True
    while ocupado is True:
        x = random.choice(list(simbolos.keys()))
        if simbolos[x] not in ["X", "O"]:
            simbolos[x] = "O"
            ocupado = False


def usuario(simbolos: dict):
    """Estrategia del usuario"""
    ocupado = True
    lista_numeros = [str(i) for i in range (1, 10)] #del 1 al 9
    while ocupado is True:
        x = input("Elija un numero del 1 al 9: ")
        if x in lista_numeros:
            if simbolos[x] not in ["X", "O"]:
                simbolos[x] = "X"
                ocupado = False
            else:
                print("Esa casilla ya esta ocupada")
    

def juego(simbolos: dict):
    """Juego del gato"""
    lista_combinaciones = [
        ["1", "2", "3"], #Filas
        ["4", "5", "6"], 
        ["7", "8", "9"], 
        
        ["1", "4", "7"], #Columnas
        ["2", "5", "8"], 
        ["3", "6", "9"], 
        
        ["1", "5", "9"], #Diagonales
        ["3", "5", "7"]
    ]
    en_juego = True
    movimientos = 0
    dibuja_tablero(simbolos)
    
    while en_juego:
        usuario(simbolos)
        dibuja_tablero(simbolos)
        movimientos += 1
        gana = checa_winner(simbolos, lista_combinaciones)
        if gana is not None or movimientos == 9:
            en_juego = False
            continue

        ia(simbolos)
        dibuja_tablero(simbolos)
        movimientos += 1
        gana = checa_winner(simbolos, lista_combinaciones)
        if gana is not None or movimientos == 9:
            en_juego = False
            continue
    return gana


def checa_winner(simbolos: dict, combinaciones: list):
    """Checa si hay un ganador"""
    for c in combinaciones:
        if simbolos[c[0]] == simbolos[c[1]] == simbolos[c[2]]:
            return simbolos[c[0]]
    return None

def actualizaScore(score:dict, ganador:str):
    """Actualiza el score"""
    X = score["X"]
    O = score["O"]
    
    if ganador is not None:
        print(f"El ganador es {ganador}")
        if ganador == "X":
              X["G"] += 1
              O["P"] += 1
        elif ganador == "O":
              X["P"] += 1
              O["G"] += 1
        else:
              X["E"] += 1
              O["E"] += 1
                
    else:
        print("Empate")  #En caso de que g no traiga algún valor
        X["E"] += 1
        O["E"] += 1


def despliega_tablero(score:dict):
    """Despliega el score"""
    print(f''' X | G: {score["X"]["G"]}  P: {score["X"]["P"] }  E: {score["X"]["E"]}\n O | G: {score["O"]["G"]}  P: {score["O"]["P"]}  E: {score["O"]["E"]}''')


if __name__ == '__main__':
        numeros = [str(i) for i in range(1,10)]
        dsimbolos = {x: x for x in numeros}
        g = juego(dsimbolos)
        
        if g is not None:
            print(f'El ganador es {g}')
        else:
            print('Empate')
        
        