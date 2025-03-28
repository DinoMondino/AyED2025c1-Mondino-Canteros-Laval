# módulo para organizar funciones o clases utilizadas en nuestro proyecto

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0
        self.actual = None # Variable para iteración

    def __iter__(self):
        actual = self.cabeza
        elementos = []
        while actual:
            elementos.append(actual.dato)  # Agregar el dato del nodo actual
            actual = actual.siguiente  # Avanzar al siguiente nodo
        return iter(elementos)

    def esta_vacia(self):
        if (self.cabeza == None) and (self.cola == None):
            return True
        else:
            return False
        
    def __len__(self):
        return self.tamanio
    
    def agregar_al_inicio(self,dato):
        nuevo_nodo = Nodo(dato)
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

    def agregar_al_final(self,dato):
        # Asignamos al nodo final el dato.
        nuevo_nodof = Nodo(dato)        
        if (self.cabeza == None) and (self.cola == None): # Si esta vacia
            self.cola = nuevo_nodof
            self.cabeza = nuevo_nodof
            self.tamanio+=1

        else:
            actual = self.cola
            nuevo_nodof.asignarAnterior(actual) # A el dato le agrego como anterior la cola existente
            actual.asignarSiguiente(nuevo_nodof) # A la cola existente le agrego como siguiente el dato
            self.cola = nuevo_nodof #Defino al dato como la nueva cola
            self.tamanio+=1


    def insertar(self,dato,posicion = "defaul"):
        # Reviso que la posición esté correcta
        if posicion == "defaul" and self.tamanio != 0:
            posicion = self.tamanio-1
            
        if (posicion > self.tamanio) or (posicion < 0) or (type(posicion) not in [int]):
            raise Exception("Posición incorrecta")
        
        elif posicion == 0:
            self.agregar_al_inicio(dato)

        elif (posicion == self.tamanio):
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

    def extraer(self, posicion="defaul"):
        if posicion == "defaul" and self.tamanio != 0:  # Si no se pasa una posición, extrae el último elemento
            posicion = self.tamanio - 1
        if isinstance(posicion, int) and posicion < 0:
            posicion = self.tamanio + posicion
        if self.tamanio == 0:  # Verificamos si la lista está vacía
            raise Exception("Lista vacía")

        if posicion < 0 or posicion >= self.tamanio or not isinstance(posicion, int):  # Validamos la posición
            raise Exception("La posición ingresada es incorrecta")

        # Caso 1: Extraer el primer elemento
        if posicion == 0:
            actual = self.cabeza
            if actual.obtenerSiguiente() is None:  # Solo un elemento en la lista
                self.cabeza = self.cola = None
            else:  # Más de un elemento
                self.cabeza = actual.obtenerSiguiente()
                self.cabeza.asignarAnterior(None)
            self.tamanio -= 1
            return actual.obtenerDato()

        # Caso 2: Extraer el último elemento
        elif posicion == self.tamanio -1:
            actual = self.cola
            if actual.obtenerAnterior() is None:  # Solo un elemento en la lista
                self.cabeza = self.cola = None
            else:  # Más de un elemento
                self.cola = actual.obtenerAnterior()
                self.cola.asignarSiguiente(None)
            self.tamanio -= 1
            return actual.obtenerDato()

        # Caso 3: Extraer un elemento intermedio
        else:
            actual = self.cabeza
            for _ in range(posicion):  # Navegar hasta el nodo en la posición
                actual = actual.obtenerSiguiente()
            anterior = actual.obtenerAnterior()
            siguiente = actual.obtenerSiguiente()
            
            if anterior is not None:
                anterior.asignarSiguiente(siguiente)  # Actualizamos el siguiente del nodo anterior
            if siguiente is not None:
                siguiente.asignarAnterior(anterior)  # Actualizamos el anterior del nodo siguiente
            
            self.tamanio -= 1
            return actual.obtenerDato()

    def copiar(self):
        if self.cabeza is None:
            return self # Si no hay elementos
        
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
        if self.tamanio < 2:
            return None
        #Caso de que tenga 2 o más elementos
        else:
            actual = self.cabeza
            # Para intercambiar anterior y siguiente en toda la lista
            while actual is not None:
                actual.siguiente, actual.anterior = actual.anterior, actual.siguiente
                actual = actual.anterior
            self.cabeza, self.cola = self.cola, self.cabeza
            if self.cabeza is not None:
                self.cabeza.asignarAnterior(None)
            if self.cola is not None:
                self.cola.asignarSiguiente(None)
            return self

    def concatenar(self,lista_p):
        #En caso promedio
        if self.tamanio != 0 and lista_p.tamanio != 0:
            actual = lista_p.cabeza
            while actual is not None:
                dato = actual.obtenerDato()
                self.agregar_al_final(dato)
                actual = actual.obtenerSiguiente()
            return self
        # En caso de que la lista base este vacia:
        elif (self.tamanio == 0) and (lista_p.tamanio !=0):
            actual = lista_p.cabeza
            while actual is not None:
                dato = actual.obtenerDato()
                self.agregar_al_final(dato)  # Método que añade un dato al final de la lista
                actual = actual.obtenerSiguiente()
            return self
        #En caso de que la lista parametro este vacia:
        elif (self.tamanio != 0) and (lista_p.tamanio == 0):
            return self
        #En caso de que los dos esten vacíos:
        elif (self.tamanio == 0) and (lista_p == 0):
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
