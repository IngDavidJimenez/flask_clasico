
import csv
from . import RUTA_FICHERO
"""
Un movimiento debe tener:
1. Fecha
2. Concepto
3. Tipo(I-ngreso, G-asto)
4. Cantidad
"""
class Movimiento:
    def __init__(self,fecha,concepto,tipo,cantidad):
        self.fecha=fecha
        self.concepto=concepto
        self.tipo = tipo
        self.cantidad = cantidad

class ListaMovimientos:
    """
    Almacenar y gestionar la lista de todos los movimientos
    """
    def __init__(self):
        self.lista_movimientos= []
    

    def leer_desde_archivo(self):
        #fichero=open(RUTA_FICHERO,'r')
        #fichero.close()
        with open(RUTA_FICHERO,'r') as fichero:
            reader= csv.DictReader(fichero)
            for fila in reader:
                #print(fila['fecha'],fila['concepto'],fila['ingreso_gasto'],fila['cantidad'])
                self.lista_movimientos.append(fila)

    

            
            



    
