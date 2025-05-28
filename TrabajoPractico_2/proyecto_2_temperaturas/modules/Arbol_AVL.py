
class NodoAVL: 
    def __init__(self, fecha, temperatura):
        self.fecha = fecha
        self.temperatura = temperatura
        self.altura = 1
        self.izquierda = None
        self.derecha = None

class AVLTree:
    def insertar(self, nodo, fecha, temperatura):
        if not nodo:
            return NodoAVL(fecha, temperatura)
        elif fecha < nodo.fecha:
            nodo.izquierda = self.insertar(nodo.izquierda, fecha, temperatura)
        else:
            nodo.derecha = self.insertar(nodo.derecha, fecha, temperatura)

        nodo.altura = 1 + max(self.get_altura(nodo.izquierda), self.get_altura(nodo.derecha))
        balance = self.get_balance(nodo)

        # Rotaciones
        if balance > 1 and fecha < nodo.izquierda.fecha:
            return self.rotar_derecha(nodo)
        if balance < -1 and fecha > nodo.derecha.fecha:
            return self.rotar_izquierda(nodo)
        if balance > 1 and fecha > nodo.izquierda.fecha:
            nodo.izquierda = self.rotar_izquierda(nodo.izquierda)
            return self.rotar_derecha(nodo)
        if balance < -1 and fecha < nodo.derecha.fecha:
            nodo.derecha = self.rotar_derecha(nodo.derecha)
            return self.rotar_izquierda(nodo)

        return nodo
    def rotar_derecha(self, y):
        x = y.izquierda
        T2 = x.derecha
        x.derecha = y
        y.izquierda = T2
        y.altura = 1 + max(self.get_altura(y.izquierda), self.get_altura(y.derecha))
        x.altura = 1 + max(self.get_altura(x.izquierda), self.get_altura(x.derecha))
        return x
    
    def rotar_izquierda(self, x):
        y = x.derecha
        T2 = y.izquierda
        y.izquierda = x
        x.derecha = T2
        x.altura = 1 + max(self.get_altura(x.izquierda), self.get_altura(x.derecha))
        y.altura = 1 + max(self.get_altura(y.izquierda), self.get_altura(y.derecha))
        return y
    
    def get_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura
    
    def get_balance(self, nodo):    
        if not nodo:
            return 0
        return self.get_altura(nodo.izquierda) - self.get_altura(nodo.derecha)
    
    def buscar(self, nodo, fecha):  
        if nodo is None or nodo.fecha == fecha:
            return nodo
        if fecha < nodo.fecha:
            return self.buscar(nodo.izquierda, fecha)
        return self.buscar(nodo.derecha, fecha)
    
    def listar_en_rango(self, nodo, fecha_inicio, fecha_fin):
        if nodo is None:
            return []
        resultado = []
        if fecha_inicio <= nodo.fecha <= fecha_fin:
            resultado.append((nodo.fecha, nodo.temperatura))
        if fecha_inicio < nodo.fecha:
            resultado.extend(self.listar_en_rango(nodo.izquierda, fecha_inicio, fecha_fin))
        if fecha_fin > nodo.fecha:
            resultado.extend(self.listar_en_rango(nodo.derecha, fecha_inicio, fecha_fin))
        return resultado
    
    def obtener_minimo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda   
        return actual
    
    def eliminar(self, nodo, fecha):
        if nodo is None:
            return nodo
        if fecha < nodo.fecha:
            nodo.izquierda = self.eliminar(nodo.izquierda, fecha)
        elif fecha > nodo.fecha:
            nodo.derecha = self.eliminar(nodo.derecha, fecha)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            temp = self.obtener_minimo(nodo.derecha)
            nodo.fecha = temp.fecha
            nodo.temperatura = temp.temperatura
            nodo.derecha = self.eliminar(nodo.derecha, temp.fecha)

        nodo.altura = 1 + max(self.get_altura(nodo.izquierda), self.get_altura(nodo.derecha))
        balance = self.get_balance(nodo)

        # Rotaciones
        if balance > 1 and self.get_balance(nodo.izquierda) >= 0:
            return self.rotar_derecha(nodo)
        if balance < -1 and self.get_balance(nodo.derecha) <= 0:
            return self.rotar_izquierda(nodo)
        if balance > 1 and self.get_balance(nodo.izquierda) < 0:
            nodo.izquierda = self.rotar_izquierda(nodo.izquierda)
            return self.rotar_derecha(nodo)
        if balance < -1 and self.get_balance(nodo.derecha) > 0:
            nodo.derecha = self.rotar_derecha(nodo.derecha)
            return self.rotar_izquierda(nodo)

        return nodo
    
