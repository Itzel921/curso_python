'''
Funciones auxiliares para el programa "Linea"

'''

def calcular_y (x,m,b):
    ''' Calcula "y" de acuerdo a la pendiente "m" y el punto de intersección en y "b". Retorna el valor de "y" '''
    return (m*x)+b

def test_linea():
    y = calcular_y(0.0, 2.0, 3.0)
    return y


if __name__ == "__main__":  
    if test_linea() == 3.0:
        print("Prueba exitosa")
    else:
        print("Prueba fallida")
        
