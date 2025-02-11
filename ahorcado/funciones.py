'''
funciones auxiliares del juego Ahorcado
'''

def carga_archivo_texto(archivo:str)->list:
    '''Carga un archivo de texto y regresa una lista con las palabras'''
    with open(archivo, 'r', encoding='utf-8') as file:
        oraciones = file.readlines()
    return oraciones


def carga_pantillas(nombre_plantilla:str)->dict:
    '''Carga una plantilla y regresa una lista con las palabras'''
    plantillas = {}
    for i in range(6):
        plantillas[i] = carga_archivo_texto(f'./plantillas/{nombre_plantilla}-{i}.txt')
    return plantillas



def despliega_plantila(diccionario:list, nivel:int):
    '''Despliega una plantilla del juego'''
    if nivel in diccionario:
        template = diccionario[nivel]
        for renglon in template:
            print(renglon)
            
            
def obten_palabras(lista: list)->list:
    #Obtiene las palabras de un texto
    texto = ' '.join(lista[120:])
    palabras = texto.split()
    minusculas = [palabra.lower() for palabra in palabras]
    set_palabras = set(minusculas)
    
    return list(set_palabras)        
             
              
if __name__ == '__main__':
    plantillas = carga_pantillas('plantilla')
    despliega_plantila(plantillas, 5)
    lista_oraciones = carga_archivo_texto('./datos/pg15532.txt')
    lista_palabras = obten_palabras(lista_oraciones)
    print(lista_palabras[:50])
   