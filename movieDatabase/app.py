#Programa principcipal de movie Database

from flask import Flask, render_template, request, redirect, url_for
import random
import os
import movie_clases as mc

app = Flask(__name__)   
sistema = mc.SistemaCine()
ruta = 'datos/movies_db - '

actores_csv = ruta + 'actores.csv'
peliculas_csv = ruta + 'peliculas.csv'
relaciones_csv = ruta + 'relacion.csv'
users_csv = ruta + 'users.csv'

sistema.cargar_csv(actores_csv, mc.Actor)
sistema.cargar_csv(peliculas_csv, mc.Pelicula)
sistema.cargar_csv(relaciones_csv, mc.Relacion)
sistema.cargar_csv(users_csv, mc.User)


@app.route('/')
def inicio():
    return render_template('index.html')



@app.route('/actores')
def actores():
    lista_Actores = sistema.actores.values()
    
    return render_template('actores.html', actores = lista_Actores)


@app.route('/peliculas')
def peliculas():
    lista_Peliculas = sistema.peliculas.values()
    return render_template('peliculas.html', peliculas = lista_Peliculas)



if __name__ == '__main__':
    app.run(debug=True)