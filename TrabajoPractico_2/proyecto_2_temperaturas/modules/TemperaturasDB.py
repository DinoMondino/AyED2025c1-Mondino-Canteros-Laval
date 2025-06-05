from datetime import datetime
from Arbol_AVL import AVLTree

class Temperaturas_DB:
    def __init__(self):
        self.arbol= AVLTree()
        self.raiz = None
        self.cantidad=0

    def guardar_temperatura(self, temperatura, fecha):
        try:
            fecha = datetime.strptime(fecha, "%d-%m-%Y").date()
        except ValueError:
            raise ValueError("Formato de fecha incorrecto. Use 'dd-mm-aaaa'.")
        self.raiz = self.arbol.insertar(self.raiz, fecha, temperatura)
        self.cantidad += 1

    def devolver_temperatura(self, fecha):
        try:
            fecha = datetime.strptime(fecha, "%d-%m-%Y").date()
        except ValueError:
            raise ValueError("Formato de fecha incorrecto. Use 'dd-mm-aaaa'.")
        nodo = self.arbol.buscar(self.raiz, fecha)
        if nodo:
            return nodo.temperatura
        else:
            return None
        
    def listar_temperaturas_en_rango(self, fecha_inicio, fecha_fin):
        try:
            fecha_inicio = datetime.strptime(fecha_inicio, "%d-%m-%Y").date()
            fecha_fin = datetime.strptime(fecha_fin, "%d-%m-%Y").date()
        except ValueError:
            raise ValueError("Formato de fecha incorrecto. Use 'dd-mm-aaaa'.")
        return self.arbol.listar_en_rango(self.raiz, fecha_inicio, fecha_fin)
    
    def max_temp_rango(self, fecha_inicio, fecha_fin):
        temperaturas=self.listar_temperaturas_en_rango(fecha_inicio, fecha_fin)
        return max(temp for _, temp in temperaturas) if temperaturas else None
    
    def min_temp_rango(self, fecha_inicio, fecha_fin):  
       temperaturas=self.listar_temperaturas_en_rango(fecha_inicio, fecha_fin)
       return min(temp for _, temp in temperaturas) if temperaturas else None
    
    def temp_extremos_rango(self, fecha_inicio, fecha_fin):
        temperaturas=self.listar_temperaturas_en_rango(fecha_inicio, fecha_fin)
        if temperaturas:
            max_temp = max(temp for _, temp in temperaturas)
            min_temp = min(temp for _, temp in temperaturas)
            return min_temp, max_temp
        else:
            return None, None
        
    def borrar_temperatura(self, fecha):
        try:
           fecha = datetime.strptime(fecha, "%d-%m-%Y").date()
        except ValueError:
            raise ValueError("Formato de fecha incorrecto. Use 'dd-mm-aaaa'.")
        nodo = self.arbol.buscar(self.raiz, fecha)
        if nodo:
            self.raiz = self.arbol.eliminar(self.raiz, fecha)
            self.cantidad -= 1
            return True
        else:
            return False
    
    def cantidad_muestras(self):
        return self.cantidad
    

