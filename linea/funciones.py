'''
Funciones auxiliares para el programa "Linea"

'''
import matplotlib.pyplot as plt

def calcular_y (x,m,b):
    ''' Calcula "y" de acuerdo a la pendiente "m" y el punto de intersección en y "b". Retorna el valor de "y" '''
    return (m*x)+b

def grafica_linea(X: list, Y:list, m:float, b:float):
    plt.plot(X,Y)
    plt.title(f"Línea recta con pendiente={m}")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()
    
    
def test_linea():
    y = calcular_y(0.0, 2.0, 3.0)
    return y




if __name__ == "__main__":  
    if test_linea() == 3.0:
        print("Prueba exitosa")
    else:
        print("Prueba fallida")
        
