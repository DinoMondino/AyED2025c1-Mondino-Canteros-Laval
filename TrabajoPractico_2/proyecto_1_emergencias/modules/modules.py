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
        return self.nombre
    
    def get_apellido(self):
        return self.apellido
    
    def get_riesgo(self):
        return self.riesgo
    
    def get_descripcion_riesgo(self):
        return self.descripcion
    
    def comparar(self):
        pass

    

class MonticuloBinario():
    def __init__(self,lista=None):
        self.lista = [None] + (lista if lista else [])
        self.tamanio = 0

    def insertar(self, item):
            """Inserta un valor en la lista y la ordena"""
            #recibimos el item y lo agregamos a la lista del montículo
            self.lista.append(item)
            #aumentamos el tamaño
            self.tamanio+=1
            #como último paso, ordenamos el montículo
            self.infiltrar_arriba(self.tamanio)

    def tamanio(self):
        return self.tamanio

    def eliminarMin(self):
        """Quitamos el valor de la cima del montículo"""
        if self.tamanio == 0:
            return None
        #Quitamos el paciente de arriba del montículo
        if self.tamanio == 0:
            return None
        paciente = self.lista[1]
        self.lista[1] = self.lista[self.tamanio]
        self.lista.pop()
        self.tamanio -= 1
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


    def infiltrar_arriba(self, pos):
        """función utilizada en la inserción de elementos en la __lista para
        ordenar el montículo o para infiltrar cualquier elemento para arriba
        especificando solo su posición"""
        while pos // 2 > 0:
            if self.lista[pos].riesgo < self.lista[pos // 2].riesgo:
                self.lista[pos], self.lista[pos // 2] = self.lista[pos // 2], self.lista[pos]
            pos //= 2

    def estaVacio(self):
        if self.tamanio==0:
            return True
        else:
            return False

    def buscarMin(self):
        return self.lista[1] if self.tamanio > 0 else None
    
    def hijoMin(self, pos):
        if pos * 2 + 1 > self.tamanio:
            return pos * 2
        if self.lista[pos * 2].riesgo < self.lista[pos * 2 + 1].riesgo:
            return pos * 2
        return pos * 2 + 1

    def __next__(self):
        if self.contador > self.tamanio:
            #En caso de que se termine la lista, se termina la iteración
            raise StopIteration
        else:
            #Obtiene el nodo siguiente
            self.actual = self.lista[self.contador]
            self.contador+=1
            return self.actual

class ColadePrioridad:
    def __init__(self):
        self.lista = MonticuloBinario()

    def insertar(self, item):
        self.lista.insertar(item)

    def eliminarMax(self):
        return self.lista.eliminarMin()
    
    def __len__(self):
        return self.lista.tamanio
    
    def __iter__(self):
        # Devuelve un iterador sobre los elementos válidos del montículo (sin el None inicial)
        return iter(self.lista.lista[1:])
    
# Ejemplo de uso
cola = ColadePrioridad()
for _ in range(10):
    paciente = Paciente()
    cola.insertar(paciente)

while not cola.lista.estaVacio():
    print(cola.eliminarMax())
    