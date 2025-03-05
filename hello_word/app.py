#Hola mundo de Flask

from flask import Flask

app = Flask(__name__)

@app.route('/')  #Home page o raíz o indice

def index():
    return '''<html>
                <head>
                    <title>Hoal mundo cruel</title>
                </head>
                
                <body>  
                    <h1>Hola Mundo ccruel</h1>
                    <p>Ir a la página de <a href= "/about"> Acerca de </a>/ </p>
                    <h3>Cómo estan?</h3>
                </body>
        </html>'''
        
        

@app.route('/about')  #Home page o raíz o indice

def about():
    return'''<html>
                <head>
                    <title>Hello world</title>
                </head>
                
                <body>  
                    <h1>Hola Mundo</h1>
                    <p>Ir a la página de <a href= "/"> Inicio </a>/</p>
                </body>
        </html>'''
        

if __name__ == '__main__':
    app.run(debug = True)  #Activa el modo de depuración 