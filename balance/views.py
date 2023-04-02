from flask import render_template
from . import app
from .models import ListaMovimientos

@app.route('/')
def home():
    """
    Muestra la lista de movimientos cargados
    """
    lista=ListaMovimientos()
    lista.leer_desde_archivo()
    #movimientos=lista.lista_movimientos
    return render_template("inicio.html",movimientos=lista.lista_movimientos)
    #funcion para publicar html desde dependencia views controlador en base flask
@app.route('/nuevo')
def add_movement():
    """
    Crea un movimiento nuevo y lo carga en el archivo CSV
    """
    return render_template("nuevo.html")
@app.route('/modificar')
def update():
    """
    Permite Editar los datos de un movimiento
    """
    return 'Actualizar Movimiento'
@app.route('/borrar')
def delete():
    """
    Elimina un movimiento existente
    """
    return 'Eliminar movimiento'
#C-reate
#R-ead
#U-pdate
#D-elete




