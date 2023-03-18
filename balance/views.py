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
    Crea un movimiento nuevo y lo carga
    """
    return 'Lista de movimientos'

