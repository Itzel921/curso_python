#Programa principal del juego del ahorcado

import os
import argparse
import string
import unicodedata
from random import choice
import funciones as fn

def main(archivo_texto:str, nombre_plantilla = 'plantilla'):
    #Programa orincipal del juego del ahorcado
    
    #Cargamos las plntillas
    plantillas =fn.carga_pantillas(nombre_plantilla)
    
    #Cargamos la oraciones
    oraciones = fn.carga_archivo_texto(archivo_texto)
    
    #Obtenemos las palabras
    palabras = fn.obten_palabras(oraciones)
    o = 5      #5 oprtunidades de fallar
    p = choice(palabras)  #Elegimos una palabra al azar 
    abecedario = {letra:letra for letra in string.ascii_lowercase}
    adivinadas = set()
    
    while o > 0:
        print("")
        fn.despliega_plantilla(plantillas, o)
        o = fn.adivina_letra(abecedario, p, adivinadas, o)
     
        if p == ''.join([letra if letra in adivinadas else '_' for letra in p]):
            print("Felicidades adivinaste la palabra")     
            break
        
    fn.despliega_plantilla(plantillas, o)
    print(f"La palabra era: ", {p})    
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Juego del ahorcado')
    parser.add_argument('-a', '--archivo', help='Archivo de texto con palabras a advinar', default = './datos/pg15532.txt')
    args = parser.parse_args()
    archivo = args.archivo
    
    if os.stat(archivo) is False:
        print(f"El archivo {archivo} no existe")
    else: 
        main(archivo)