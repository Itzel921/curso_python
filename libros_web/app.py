#Programa principal de Libros Web

from flask import Flask, render_template, request
import funciones as fn

app = Flask(__name__)

archivo_csv = "booklist2000.csv"
lista_libros = fn.lee_archivo_csv(archivo_csv)
diccionario_titulos = fn.crea_diccionario(lista_libros, 'title')
diccionario_autores = fn.crea_diccionario(lista_libros, 'author')

@app.route('/')
def inicio():
    #Página de inicio de la aplicación
    return render_template('index.html')  


@app.route('/buscar', methods=['GET','POST'])
def busqueda_titulo():
    #Página de búsqueda por título
    
    titulo = request.form['titulo']
    resultado = fn.buscar_en_diccionario(diccionario_titulos, titulo)
    
    return render_template('resultado.html', lista_libros = resultado)



if __name__ == '__main__':
    app.run(debug=True)