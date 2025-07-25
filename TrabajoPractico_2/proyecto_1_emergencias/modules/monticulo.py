## MonticuloBinario
class MonticuloBinario():
    def __init__(self, lista=None, es_min_heap=True):
        # El primer elemento (índice 0) se mantiene como None para simplificar los cálculos de índices
        self.lista = [None] + (lista if lista else [])
        self.tamanio = len(self.lista) - 1 if lista else 0
        self.es_min_heap = es_min_heap # atributo para determinar si es min o max heap

    def _insertar(self, item):
        """Inserta un valor en la lista y la ordena; O(logn)"""
        self.lista.append(item)
        self.tamanio += 1
        self._infiltrar_arriba(self.tamanio)

    def _tamanio_actual(self):
        return self.tamanio

    def _eliminarMin(self): 
        """Quita el valor de la cima del montículo (el de mayor prioridad); O(logn)"""
        if self.tamanio == 0:
            return None
        item = self.lista[1]
        self.lista[1] = self.lista[self.tamanio]
        self.lista.pop()
        self.tamanio -= 1
        self._infiltrar_abajo(1) 
        return item

    def _infiltrar_abajo(self, pos):
        """Función usada en la eliminación de elementos en la cima del montículo
        o para filtrar cualquier elemento hacia abajo recibiendo la posición."""
        while (pos * 2) <= self.tamanio:
            pos_hijo = self._hijoMin(pos) 
            if self.es_min_heap:
                if self.lista[pos] > self.lista[pos_hijo]:
                    self.lista[pos], self.lista[pos_hijo] = self.lista[pos_hijo], self.lista[pos]
            else: # Es max-heap
                if self.lista[pos] < self.lista[pos_hijo]:
                    self.lista[pos], self.lista[pos_hijo] = self.lista[pos_hijo], self.lista[pos]
            pos = pos_hijo

    def _infiltrar_arriba(self, pos):
        """Función utilizada en la inserción de elementos en la lista para
        ordenar el montículo o para infiltrar cualquier elemento hacia arriba
        especificando solo su posición."""
        while pos // 2 > 0:
            if self.es_min_heap:
                if self.lista[pos] < self.lista[pos // 2]:
                    self.lista[pos], self.lista[pos // 2] = self.lista[pos // 2], self.lista[pos]
            else: # Es max-heap
                if self.lista[pos] > self.lista[pos // 2]:
                    self.lista[pos], self.lista[pos // 2] = self.lista[pos // 2], self.lista[pos]
            pos //= 2

    def _estaVacio(self):
        return self.tamanio == 0

    def _buscarMin(self): 
        return self.lista[1] if self.tamanio > 0 else None #O(1)

    def _hijoMin(self, pos):
        """Método auxiliar para encontrar el índice del hijo de mayor prioridad (menor para min-heap, mayor para max-heap)."""
        # Si solo tiene hijo izquierdo
        if (pos * 2 + 1) > self.tamanio:
            return pos * 2
        else:
            if self.es_min_heap:
                if self.lista[pos * 2] < self.lista[pos * 2 + 1]:
                    return pos * 2
                else:
                    return pos * 2 + 1
            else: # Es max-heap
                if self.lista[pos * 2] > self.lista[pos * 2 + 1]:
                    return pos * 2
                else:
                    return pos * 2 + 1

    def __iter__(self):
        return iter(self.lista[1:])


## ColadePrioridad
class ColadePrioridad:
    def __init__(self, es_min_heap=True):
        self.lista = MonticuloBinario() 

    def insertar(self, item):
        self.lista._insertar(item)

    def eliminarMax(self): 
        return self.lista._eliminarMin()

    def __len__(self):
        return self.lista._tamanio_actual()

    def __iter__(self):
        return iter(self.lista)