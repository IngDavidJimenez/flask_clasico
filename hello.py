from flask import Flask
"""
Para ejecutar la app de Flask necesitamos un servidor web
que acepte las peticiones, las envie a nuestro programa en FalsK
y recoja los resultados para enviarlos al navegador.

Flask nos proporciona un servidor **solamente para desarrolo**
que nos facilita las pruebas en nuestro PC

Para que esto nos funcione correctamente necesitamos dos variables de entorno

-Linux/Mac
    export FLASK_APP=hello
    export FLASK_ENVIROMENT=development
    export FLASK_DEBUG=1
    esport FLASK_RUN_PORT=7777
-
    set FLASK_APP=hello
    set FLASK_ENVIROMENT=development
"""
app=Flask(__name__)#Crea una instancia de Flask 1° Paso
@app.route('/') #Decorador mapeo de ruta de acceso 2° Paso, ejecuta la funcion hola cuando en la URL se agrega '/'
def hola():
    return 'Hola, soy Flask. y tu, ¿Cómo te llamas?'
@app.route('/bye') 
def adios():
    return 'Adios, te veo luego?'
def segunda_funcion():
    return 'Vamos a ver que muestra y donde lo muestra'
@app.route('/new') 
def nuevo():
    return 'Soy otra ruta nueva'


