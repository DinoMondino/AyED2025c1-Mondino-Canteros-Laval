## MonticuloBinario
class MonticuloBinario():
    def __init__(self, lista=None, es_min_heap=True):
        # El primer elemento (índice 0) se mantiene como None para simplificar los cálculos de índices
        self.lista = [None] + (lista if lista else [])
        self.tamanio = len(self.lista) - 1 if lista else 0
        self.es_min_heap = es_min_heap # Nuevo atributo para determinar si es min o max heap

    def _insertar(self, item):
        """Inserta un valor en la lista y la ordena"""
        self.lista.append(item)
        self.tamanio += 1
        self._infiltrar_arriba(self.tamanio)

    def _tamanio_actual(self):
        return self.tamanio

    def _eliminar(self): # Renombrado a 'eliminar' para ser genérico (elimina min o max según el tipo de heap)
        """Quita el valor de la cima del montículo (el de mayor prioridad)"""
        if self.tamanio == 0:
            return None
        item = self.lista[1]
        self.lista[1] = self.lista[self.tamanio]
        self.lista.pop()
        self.tamanio -= 1
        self._infiltrar_abajo(1) # Usar el nombre privado
        return item

    def _infiltrar_abajo(self, pos):
        """Función usada en la eliminación de elementos en la cima del montículo
        o para filtrar cualquier elemento hacia abajo recibiendo la posición."""
        while (pos * 2) <= self.tamanio:
            pos_hijo = self._obtener_hijo_prioritario(pos) # Usar el nombre privado
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

    def _buscar_prioritario(self): # Renombrado para ser genérico
        return self.lista[1] if self.tamanio > 0 else None

    def _obtener_hijo_prioritario(self, pos):
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

    def eliminarMax(self): # Este nombre es engañoso si la cola es min-heap. Considera renombrarlo a eliminar_prioritario
        return self.lista._eliminar() # Ahora llama al método genérico 'eliminar'

    def __len__(self):
        return self.lista._tamanio_actual()

    def __iter__(self):
        return iter(self.lista)