# módulo para organizar funciones o clases utilizadas en nuestro proyecto

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tam = 0
        self.actual = None #V ariable para iteración

    def esta_vacia(self):
        if (self.cabeza == None) and (self.cola == None)
            return True
        else
            return False
        
    def __len__(self):
        return self.tam
    
    def agregar_al_inicio(self,dato):
        """Recibe un dato, crea el nodo y lo agrega al inicio"""
        nuevo_nodo = Nodo(dato)
        # Le asignamos como siguiente la cabeza de la lista
        # Reviso primero si no está vacia, if true, el dato será la cabeza y cola
        if (self.cabeza == None) and (self.cola == None):
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
            self.tamanio+=1
        # If false, el dato será la nueva cabeza, la cabeza anterior será el nodo siguiente al dato.
        else:
            actual = self.cabeza # Me posiciono en la cabeza
            nuevo_nodo.asignarSiguiente(actual) # Le asigno al dato el siguiente
            actual.asignarAnterior(nuevo_nodo) # Le asigno al la antigua cabeza el dato como anterior
            self.cabeza = nuevo_nodo # Cambio la cabeza para que sea el dato
            self.tamanio+=1









# Clase nodo para items en LDE
 class Nodo:
    def __init__(self, p_dato):
        self.dato=p_dato
        self.siguiente=None # Se guarda el objeto del nodo siguiente, no el valor
        self.anterior=None

    def obtenerDato(self):
        return self.dato

    def obtenerSiguiente(self):
        return self.siguiente
    
    def obtenerAnterior(self):
        return self.anterior

    def asignarDato(self,nuevodato):
        self.dato = nuevodato