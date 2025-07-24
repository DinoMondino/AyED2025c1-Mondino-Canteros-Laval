class NodoAVL: 
    def __init__(self, clave, valor):
        self.clave = clave # fecha
        self.valor = valor # temperatura
        self.altura = 1    # altura del nodo 
        self.izquierda = None
        self.derecha = None

class AVLTree:
    def insertar(self, nodo, clave, valor): # O(logn) 
        if not nodo:
            return NodoAVL(clave, valor)
        elif clave < nodo.clave:
            nodo.izquierda = self.insertar(nodo.izquierda, clave, valor)
        else:
            nodo.derecha = self.insertar(nodo.derecha, clave, valor)
        # inserción recursiva, busca la posición correcta
        nodo.altura = 1 + max(self.get_altura(nodo.izquierda), self.get_altura(nodo.derecha))
        balance = self.get_balance(nodo)
        # Verifica el balance del nodo y rotaciones
        if balance > 1 and clave < nodo.izquierda.clave:
            return self.rotar_derecha(nodo)
        if balance < -1 and clave > nodo.derecha.clave:
            return self.rotar_izquierda(nodo)
        if balance > 1 and clave > nodo.izquierda.clave:
            nodo.izquierda = self.rotar_izquierda(nodo.izquierda)
            return self.rotar_derecha(nodo)
        if balance < -1 and clave < nodo.derecha.clave:
            nodo.derecha = self.rotar_derecha(nodo.derecha)
            return self.rotar_izquierda(nodo)

        return nodo
    def rotar_derecha(self, y): # O(1); cuando el árbol Izq. está desbalanceado (factor de balance > 1)
        x = y.izquierda
        T2 = x.derecha
        x.derecha = y
        y.izquierda = T2
        y.altura = 1 + max(self.get_altura(y.izquierda), self.get_altura(y.derecha))
        x.altura = 1 + max(self.get_altura(x.izquierda), self.get_altura(x.derecha))
        return x
    
    def rotar_izquierda(self, x): # O(1); cuando el árbol Der. está desbalanceado (factor de balance < -1)
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
    
    def buscar(self, nodo, clave):  # O(logn) 
        if nodo is None or nodo.clave == clave:
            return nodo
        if clave < nodo.clave:
            return self.buscar(nodo.izquierda, clave)
        return self.buscar(nodo.derecha, clave)
    
    def listar_en_rango(self, nodo, clave_inicio, clave_fin): 
        # O(logn+k) - Donde k es el número de elementos en el rango.
        if nodo is None:
            return []
        resultado = []
        if clave_inicio <= nodo.clave <= clave_fin:
            resultado.append((nodo.clave, nodo.valor))
        if clave_inicio < nodo.clave:
            resultado.extend(self.listar_en_rango(nodo.izquierda, clave_inicio, clave_fin))
        if clave_fin > nodo.clave:
            resultado.extend(self.listar_en_rango(nodo.derecha, clave_inicio, clave_fin))
        return resultado
    
    def obtener_minimo(self, nodo): 
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda   
        return actual
    
    def eliminar(self, nodo, clave): # O(logn)
        if nodo is None:
            return nodo
        if clave < nodo.clave:
            nodo.izquierda = self.eliminar(nodo.izquierda, clave)
        elif clave > nodo.clave:
            nodo.derecha = self.eliminar(nodo.derecha, clave)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            temp = self.obtener_minimo(nodo.derecha)
            nodo.clave= temp.clave
            nodo.valor= temp.valor
            nodo.derecha = self.eliminar(nodo.derecha, temp.clave)

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
    
