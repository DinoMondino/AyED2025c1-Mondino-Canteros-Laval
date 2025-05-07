from random import randint, choices

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
# probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6] 

class Paciente:
    def __init__(self):
        self.nombre = nombres[randint(0, len(nombres) - 1)]
        self.apellido = apellidos[randint(0, len(apellidos) - 1)]
        self.riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.descripcion = descripciones_de_riesgo[self.riesgo - 1]

    def __str__(self):
        return f"{self.nombre} {self.apellido} -> {self.riesgo}-{self.descripcion}"

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

    

class MonticuloBinario():
    def __init__(self,__lista=None):
        self.lista = [0] + (lista if lista else [])
        self.tamanio = 0

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
        if self.tamanio == 0:
            return None
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
        while pos * 2 <= self.tamanio:
            pos_hijo = self.hijoMin(pos)
            if self.lista[pos].riesgo > self.lista[pos_hijo].riesgo:
                self.lista[pos], self.lista[pos_hijo] = self.lista[pos_hijo], self.lista[pos]
            pos = pos_hijo

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
            if self.lista[pos].riesgo < self.lista[pos // 2].riesgo:
                self.lista[pos], self.lista[pos // 2] = self.lista[pos // 2], self.lista[pos]
            pos //= 2

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

