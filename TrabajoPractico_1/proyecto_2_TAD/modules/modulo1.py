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
        # Reviso primero si no está vacia, if true, el dato será la cabeza y cola
        if (self.cabeza == None) and (self.cola == None):
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
            self.tam+=1
        # If false, el dato será la nueva cabeza, la cabeza anterior será el nodo siguiente al dato.
        else:
            actual = self.cabeza # Me posiciono en la cabeza
            nuevo_nodo.asignarSiguiente(actual) # Le asigno al dato el siguiente
            actual.asignarAnterior(nuevo_nodo) # Le asigno al la antigua cabeza el dato como anterior
            self.cabeza = nuevo_nodo # Cambio la cabeza para que sea el dato
            self.tam+=1

    def agregar_al_final(self,dato):
        # Asignamos al nodo final el dato.
        nuevo_nodof = Nodo(dato)        
        if (self.cabeza == None) and (self.cola == None): # Si esta vacia
            self.cola = nuevo_nodof
            self.cabeza = nuevo_nodof
            self.tam+=1

        else:
            actual = self.cola
            nuevo_nodof.asignarAnterior(actual) # A el dato le agrego como anterior la cola existente
            actual.asignarSiguiente(nuevo_nodof) # A la cola existente le agrego como siguiente el dato
            self.cola = nuevo_nodof #Defino al dato como la nueva cola
            self.tam+=1


    def insertar(self,dato,posicion):
        # Reviso que la posición esté correcta
        if (posicion > self.tam-1) or (posicion < 0) or (type(posicion) not in [int]):
            raise Exception("Posición incorrecta")
        
        elif posicion == 0:
            self.agregar_al_inicio(dato)

        elif (posicion == self.tamanio) and (posicion !=0):
            self.agregar_al_final(dato)

        else:
            #creamos el nodo y le asignamos el dato del parametro
            nuevo_nodo = Nodo(dato)
            contador = 0
            """hacemos un while para obtener el nodo anterior y posterior al nuevo
            para poder agregarlo a la lista"""
            actual = self.cabeza
            while contador != (posicion):
                    actual = actual.obtenerSiguiente()
                    contador+=1
            # Ahora el nodo actual es el que está en la posición en la que queremos insertar
            # Obtenemos el anterior al actual
                actual_anterior = actual.obtenerAnterior()

            # Cambiamos el anterior del actual (nuevo nodo) y el siguiente del nuevo (actual)
                nuevo_nodo.asignarSiguiente(actual)
                actual.asignarAnterior(nuevo_nodo)
                #Lo mismo con el anterior al actual, su siguiente será nuevo nodo
                actual_anterior.asignarSiguiente(nuevo_nodo)
                nuevo_nodo.asignarAnterior(actual_anterior)
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
    
    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente

    def asignarAnterior(self,nuevoanterior):
        self.anterior = nuevoanterior
