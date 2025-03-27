# módulo para organizar funciones o clases utilizadas en nuestro proyecto

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tam = 0
        self.actual = None # Variable para iteración

    def esta_vacia(self):
        if (self.cabeza == None) and (self.cola == None):
            return True
        else:
            return False
        
    def __len__(self):
        return self.tam
    
    def agregar_al_inicio(self,dato):
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
        if posicion == None:
            posicion = self.tam
        if (posicion > self.tam) or (posicion < 1) or (type(posicion) not in [int]):
            raise Exception("Posición incorrecta")
        
        elif posicion == 1:
            self.agregar_al_inicio(dato)

        elif (posicion == self.tam):
            self.agregar_al_final(dato)

        else:
            #creamos el nodo y le asignamos el dato del parametro
            nuevo_nodo = Nodo(dato)
            contador = 0
            """hacemos un while para obtener el nodo anterior y posterior al nuevo
            para poder agregarlo a la lista"""
            actual = self.cabeza
            while contador != (posicion-1):
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
            self.tam+=1

    def extraer(self,posicion):
        if posicion == None:
            posicion = self.tam
        if self.tam == 0:
            raise Exception("Lista vacía")
        if posicion < 1 or posicion > self.tam:
            raise Exception("La posición ingresada es incorrecta")
# El orden de complejidad para eliminar extremos es O(1).
        # Si la posicion es 0, tenemos 2 casos:
        elif posicion == 0:
            actual = self.cabeza
            #Caso 1: la cabeza es el único en la lista
            if actual.obtenerSiguiente() is None:                    
                self.cabeza = None
                self.cola = None
                self.tam-=1
                return actual.dato
            #Caso 2: la cabeza tiene un siguiente
            else:
                self.cabeza = actual.obtenerSiguiente()
                self.cabeza.asignarAnterior(None)
                self.tam-=1
                actual.asignarSiguiente(None)
                return actual.dato

        #Si pos es el último, tenemos 2 casos:
        elif (posicion == self.tam):
            #Caso 1: la cola es el único en la lista
            actual = self.cola
            if actual.obtenerAnterior() is None:
                self.cola = None
                self.cabeza = None
                self.tam-=1
                return actual.dato
            #Caso 2: la cola tiene un anterior
            else:
                self.cola = actual.obtenerAnterior()
                self.cola.asignarSiguiente(None)
                self.tam-=1
                actual.asignarAnterior(None)
                return actual.dato
            
        #Eliminamos una posición intermedia
        else:
            actual = self.cabeza
            cont = 0
            #Se busca el nodo que se quiere eliminar.
            while cont < posicion:
                actual = actual.obtenerSiguiente()
                cont+=1
            ant = actual.obtenerAnterior() # Anterior del que será eliminado
            sig = actual.obtenerSiguiente() # Siguiente del que será eliminado

            ant.asignarSiguiente(sig) # Se le asigna al ant sig como siguiente
            sig.asignarAnterior(ant) # Se le asigna al sig ant como anterior

            actual.asignarSiguiente(None)
            actual.asignarAnterior(None)
            self.tam+=(-1)
            return actual.dato

    def copiar(self):
        if self.cabeza is None:
            return ListaDobleEnlazada() # Si no hay elementos
        
        #Creamos una lista nueva y nos posicionamos en la cabeza de la lista a copiar
        nueva_lista = ListaDobleEnlazada()
        actual = self.cabeza
        #El while se detiene cuando no hay un siguiente nodo
        while actual is not None:
            # Obtengo el dato del nodo y creo otro nodo igual
            dato = actual.obtenerDato()
            nueva_lista.agregar_al_final(dato)
            # Se lee el nodo siguiente
            actual = actual.obtenerSiguiente()

        return nueva_lista   

    def invertir(self):
        #Caso de que la lista este vacia o tenga 1 elemento:
        if self.tam < 2:
            return None
        #Caso de que tenga 2 o más elementos
        else:
            actual = self.cabeza
            # Para intercambiar anterior y siguiente en toda la lista
            while actual is not None:
                sig = actual.obtenerSiguiente()
                ant = actual.obtenerAnterior()
                actual.asignarAnterior(sig)
                actual.asignarSiguiente(ant)
                actual = sig
            # Intercambio los extremos
            paso = self.cola
            self.cola = self.cabeza
            self.cabeza = paso

    def concatenar(self,lista_p):
        """Junta el último nodo de la lista con el primero de la lista parámetro
        formando una nueva lista"""
        #En caso promedio
        if (self.tam == 0) and (lista_p.tam !=0):
            actual = lista_p.cabeza.obtenerDato()
            while actual is not None:
                dato = actual.obtenerDato()
                self.agregar_al_final(dato)
                actual = actual.obtenerSiguiente()
            return ListaDobleEnlazada
        #En caso de que la lista parametro este vacia:
        elif (self.tam != 0) and (lista_p.tam == 0):
            return ListaDobleEnlazada
        #En caso de que los dos esten vacíos:
        elif (self.tam == 0) and (lista_p == 0):
            return None
        
    def __add__(self, lista_p):
        nueva_lista = self.copiar()
        nueva_lista.concatenar(lista_p)  # Concatenamos lista_p a la copia de la lista base
        return nueva_lista

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
