#Archivo con las funciones necesarias de las Aplicación  Libros Web
import csv

def lee_archivo_csv(archivo:str)->list:
    #Lee un archivo csv y lo convierte en una lista de diccionarios
    
    with open(archivo, 'r', encoding='utf8') as file:
        return [x for x in csv.DictReader(file)]


def crea_diccionario_titulos(listas:list)->dict:
    #Crea un diccionario con los titulos como clave y el resto de los datos como valores
    
    return {x['title']: x for x in listas}


def busca_en_titulo(diccionario, palabra)->list:
    #Busca palabra en titulo de la lista de diccionarios
    lista = []
    for titulo, libro in diccionario.items():
        if palabra in titulo.lower():
            lista.append(libro)
    return lista


if __name__ == '__main__':
    archivo_csv = "booklist2000.csv"
    
    lista_libros = lee_archivo_csv(archivo_csv)
    diccionario_libros = crea_diccionario_titulos(lista_libros)
    resultado = busca_en_titulo(diccionario_libros, 'flower')
    print(resultado)
    