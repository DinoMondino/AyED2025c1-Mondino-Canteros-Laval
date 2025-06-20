from random import randint, choices
import itertools # Importamos itertools para generar IDs únicos

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
# probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6]

# Generador de IDs únicos para el orden de llegada
next_id = itertools.count()

class Paciente:
    def __init__(self):
        self.nombre = nombres[randint(0, len(nombres) - 1)]
        self.apellido = apellidos[randint(0, len(apellidos) - 1)]
        self.riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.descripcion = descripciones_de_riesgo[self.riesgo - 1]
        self.orden_llegada = next(next_id) # Asignamos un ID único al paciente

    def __str__(self):
        return f"{self.nombre} {self.apellido} -> Riesgo: {self.riesgo}-{self.descripcion}, Orden de Llegada: {self.orden_llegada}"

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_riesgo(self):
        return self.riesgo

    def get_descripcion_riesgo(self):
        return self.descripcion

    # Implementamos los métodos de comparación para que el montículo sea genérico
    # y pueda comparar pacientes.
    def __lt__(self, other):
        # Primero compara por riesgo (menor riesgo, mayor prioridad)
        if self.riesgo < other.riesgo:
            return True
        elif self.riesgo == other.riesgo:
            # Si los riesgos son iguales, compara por orden de llegada (menor orden_llegada, mayor prioridad)
            return self.orden_llegada < other.orden_llegada
        return False

    def __gt__(self, other):
        # Inverso de __lt__
        if self.riesgo > other.riesgo:
            return True
        elif self.riesgo == other.riesgo:
            return self.orden_llegada > other.orden_llegada
        return False

    def __eq__(self, other):
        return self.riesgo == other.riesgo and self.orden_llegada == other.orden_llegada

## MonticuloBinario (Heap Binario Genérico)

class MonticuloBinario():
    def __init__(self, lista=None):
        # El primer elemento (índice 0) se mantiene como None para simplificar los cálculos de índices
        self.lista = [None] + (lista if lista else [])
        self.tamanio = len(self.lista) - 1 if lista else 0

    def insertar(self, item):
        """Inserta un valor en la lista y la ordena"""
        self.lista.append(item)
        self.tamanio += 1
        self.infiltrar_arriba(self.tamanio)

    def tamanio_actual(self): # Renombrado para evitar conflicto con la variable de instancia
        return self.tamanio

    def eliminarMin(self):
        """Quita el valor de la cima del montículo (el de mayor prioridad)"""
        if self.tamanio == 0:
            return None
        # El elemento de mayor prioridad está en la raíz (índice 1)
        min_item = self.lista[1]
        # Movemos el último elemento a la raíz
        self.lista[1] = self.lista[self.tamanio]
        # Removemos el último elemento de la lista
        self.lista.pop()
        self.tamanio -= 1
        # Reordenamos el montículo desde la raíz
        self.infiltrar_abajo(1)
        return min_item

    def infiltrar_abajo(self, pos):
        """Función usada en la eliminación de elementos en la cima del montículo
        o para filtrar cualquier elemento hacia abajo recibiendo la posición."""
        while (pos * 2) <= self.tamanio:
            pos_hijo = self._hijoMin(pos) # Usamos el método auxiliar para encontrar el hijo de menor valor
            # Comparamos los objetos directamente usando los operadores definidos en ellos
            if self.lista[pos] > self.lista[pos_hijo]:
                self.lista[pos], self.lista[pos_hijo] = self.lista[pos_hijo], self.lista[pos]
            pos = pos_hijo

    def infiltrar_arriba(self, pos):
        """Función utilizada en la inserción de elementos en la lista para
        ordenar el montículo o para infiltrar cualquier elemento hacia arriba
        especificando solo su posición."""
        while pos // 2 > 0:
            # Comparamos los objetos directamente usando los operadores definidos en ellos
            if self.lista[pos] < self.lista[pos // 2]:
                self.lista[pos], self.lista[pos // 2] = self.lista[pos // 2], self.lista[pos]
            pos //= 2

    def estaVacio(self):
        return self.tamanio == 0

    def buscarMin(self):
        return self.lista[1] if self.tamanio > 0 else None

    def _hijoMin(self, pos):
        """Método auxiliar para encontrar el índice del hijo de menor valor."""
        # Si solo tiene hijo izquierdo
        if (pos * 2 + 1) > self.tamanio:
            return pos * 2
        else:
            # Compara los hijos y devuelve el índice del menor
            if self.lista[pos * 2] < self.lista[pos * 2 + 1]:
                return pos * 2
            else:
                return pos * 2 + 1

    def __iter__(self):
        # Devuelve un iterador sobre los elementos válidos del montículo (sin el None inicial)
        # Esto es importante para que la iteración de la ColaDePrioridad funcione correctamente
        return iter(self.lista[1:])


## ColadePrioridad
class ColadePrioridad:
    def __init__(self):
        self.lista = MonticuloBinario()

    def insertar(self, item):
        self.lista.insertar(item)

    def eliminarMax(self): # Renombrado a eliminarMax para reflejar que elimina el de mayor prioridad (menor valor en un min-heap)
        return self.lista.eliminarMin()

    def __len__(self):
        return self.lista.tamanio_actual() # Usamos el nuevo nombre del método

    def __iter__(self):
        # Permite iterar directamente sobre los elementos en la cola de prioridad
        return iter(self.lista)

# Ejemplo de uso
if __name__ == "__main__":
    print("--- Ejemplo de uso de Cola de Prioridad ---")
    cola = ColadePrioridad()
    for _ in range(10):
        paciente = Paciente()
        cola.insertar(paciente)
        print(f"Insertando: {paciente}")

    print("\n--- Pacientes atendidos por orden de prioridad ---")
    while not cola.lista.estaVacio():
        print(cola.eliminarMax())
