#Archivo con las funciones necesarias de las Aplicación  Libros Web
import csv

def lee_archivo_csv(archivo:str)->list:
    #Lee un archivo csv y lo convierte en una lista de diccionarios
    
    with open(archivo, 'r', encoding='utf8') as file:
        return [x for x in csv.DictReader(file)]


def crea_diccionario(listas:list, llave:str)->dict:
    #Crea un diccionario un diccionario con la palabra llave como clave y el resto de los datos como valores
    
    return {x[llave].lower(): x for x in listas}


def buscar_en_diccionario(diccionario, palabra)->list:
    #Busca palabra en titulo de la lista de diccionarios
    lista = []
    palabra = palabra.lower()
    for titulo, libro in diccionario.items():
        if palabra in titulo.lower():
            lista.append(libro)
    return lista

def libros_empieza_con(lista:list, letra:str)->list:
    #Busca libros que empicen con letra
    
    return [x for x in lista if x['title'].lower().startswith(letra.lower())]   



if __name__ == '__main__':
    archivo_csv = "booklist2000.csv"
    lista_libros = lee_archivo_csv(archivo_csv)
    
    diccionario_libros = crea_diccionario(lista_libros, 'title')
    resultado = buscar_en_diccionario(diccionario_libros, 'flower')
    print(resultado)
    
    diccionario_autores  = crea_diccionario(lista_libros, 'author')
    resultado = buscar_en_diccionario(diccionario_autores, 'Sandra')
    print(resultado)
   
    resultado = libros_empieza_con(lista_libros, 'x')
    print(f"Libros que empiezan con la letra 'z': {len(resultado)}")