from . import app


@app.route('/')
def home():
    """
    Muestra la lista de movimientos cargados
    """
    return 'Lista de movimientos'
@app.route('/nuevo')
def add_movement():
    """
    Crea un movimiento nuevo y lo carga en el archivo CSV
    """
    return 'Crea movimiento'
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




