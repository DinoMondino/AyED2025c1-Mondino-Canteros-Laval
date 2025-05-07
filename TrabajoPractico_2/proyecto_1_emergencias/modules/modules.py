from random import randint, choices

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
# probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6] 

class Paciente:
    def __init__(self):
        n = len(nombres)
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]

    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_riesgo(self):
        return self.__riesgo
    
    def get_descripcion_riesgo(self):
        return self.__descripcion
    
    def comparar(self):
        pass
    
    def __str__(self):
        cad = self.__nombre + ' '
        cad += self.__apellido + '\t -> '
        cad += str(self.__riesgo) + '-' + self.__descripcion
        return cad
    

class MonticuloBinario():
    def __init__(self,__lista=None):
        if __lista is None:
            self.__lista = [0]
        else:
            self.__tamanio=len(__lista)
            self.__lista = [0] + __lista
        self.__tamanio = 0
        self.__contador=1
        self.actual = None
        

    def insertar(self, item):
            """Inserta un valor en la __lista y la ordena"""
            #recibimos el item y lo agregamos a la __lista del montículo
            self.__lista.append(item)
            #aumentamos el tamaño
            self.__tamanio+=1
            #como último paso, ordenamos el montículo
            self.infiltrar_arriba(self.__tamanio)

    def tamanio(self):
        return self.__tamanio

    def eliminarMin(self):
        """Quitamos el valor de la cima del montículo"""
        #Quitamos el paciente de arriba del montículo
        paciente = self.__lista[1]
        #Remplazamos el valor de arriba por el último agregado
        self.__lista[1] = self.__lista[self.__tamanio]
        #Quitamos el último valor agregado de la __lista
        self.__lista.pop()
        self.__tamanio-=1
        #Ordenamos la __lista filtrando hacia abajo el primer valor
        self.infiltrar_abajo(1)

        return paciente

    def infiltrar_abajo(self,pos):
        """función usada en la eliminación de elementos en la cima
        del montículo o para filtrar cualquier elemento para abajo
        recibiendo la posición"""
        
        #Hacemos un while para el caso de que el nodo actual tenga hijos
        while self.__tamanio >= pos*2 :
            #Como tenemos dos nodos, no sabemos cual es el menor de los dos.
            #Así que averiguamos cual de los dos es 
            poshijo = self.hijoMin(pos)

            #Ahora comparamos cual si el padre es mayor o no
            if self.__lista[pos].get_riesgo() > self.__lista[poshijo].get_riesgo():        
                aux = self.__lista[poshijo]
                self.__lista[poshijo] = self.__lista[pos]
                self.__lista[pos] = aux
            pos = poshijo

    def hijoMin(self,pos):
        #En caso de que tenga un solo hijo:
        if pos*2+1 > self.__tamanio:
            #Devolvemos el hijo de la izquierda(pos*2)
            return pos * 2
        #En caso de que tenga dos hijos:
        else:
            #Comparamos cual de los dos es menor y lo devolvemos
            if self.__lista[pos*2].get_riesgo() < self.__lista[pos*2+1].get_riesgo():
                return pos * 2
            else:
                return pos * 2 + 1

    def infiltrar_arriba(self, pos):
        """función utilizada en la inserción de elementos en la __lista para
        ordenar el montículo o para infiltrar cualquier elemento para arriba
        especificando solo su posición"""
        while pos // 2 > 0:
            #Si el nodo hijo es menor que el padre, los intercambia
            if self.__lista[pos].get_riesgo() < self.__lista[pos // 2].get_riesgo():        
                aux = self.__lista[pos // 2]
                self.__lista[pos // 2] = self.__lista[pos]
                self.__lista[pos] = aux
            #Ahora comparamos con el padre del padre
            pos = pos // 2

    def estaVacio(self):
        if self.__tamanio==0:
            return True
        else:
            return False

    def buscarMin(self):
        return self.__lista[1]
    
    def __iter__(self):
        # Devolver el primer nodo de la lista para comenzar la iteración
        if self.tamanio() > 0:
            self.actual = self.__lista[1]
            self.__contador = 1
            return self
        else:
            return self

    def __next__(self):
        if self.__contador > self.__tamanio:
            #En caso de que se termine la lista, se termina la iteración
            raise StopIteration
        else:
            #Obtiene el nodo siguiente
            self.actual = self.__lista[self.__contador]
            self.__contador+=1
            return self.actual

class ColadePrioridad:
    def __init__(self):
        self.__lista = MonticuloBinario()

    def insertar(self, item):
        self.__lista.insertar(item)

    def eliminarMin(self):
        return self.__lista.eliminarMin()
    

    
if __name__ == "__main__":
    """mini testeo de funciones"""
    lista = MonticuloBinario()
    paciente1 = Paciente()
    print(paciente1.get_riesgo())
    paciente2 = Paciente()
    print(paciente2.get_riesgo())
    paciente3 = Paciente()
    print(paciente3.get_riesgo())
    paciente4 = Paciente()
    print(paciente4.get_riesgo())

    lista.insertar(paciente1)
    lista.insertar(paciente2)
    lista.insertar(paciente3)
    lista.insertar(paciente4)

    #lista.eliminarMin()
    print(lista.buscarMin())
    lista.eliminarMin()
    print(lista.buscarMin())
    lista.eliminarMin()
    print(lista.buscarMin())
    print(lista.tamanio())

