class MonticuloBinario:
    def __init__(self):
        self.lista = []

    def insertar(self, item):
        self.lista.append(item)
        self._subir(len(self.lista) - 1)

    def eliminarMin(self):
        if not self.lista:
            return None
        self._intercambiar(0, len(self.lista) - 1)
        minimo = self.lista.pop()
        self._bajar(0)
        return minimo

    def estaVacio(self):
        return not self.lista

    def _subir(self, i):
        padre = (i - 1) // 2
        while i > 0 and self.lista[i] < self.lista[padre]:
            self._intercambiar(i, padre)
            i = padre
            padre = (i - 1) // 2

    def _bajar(self, i):
        hijo_izq = 2 * i + 1
        while hijo_izq < len(self.lista):
            hijo_der = hijo_izq + 1
            hijo_menor = hijo_izq

            if hijo_der < len(self.lista) and self.lista[hijo_der] < self.lista[hijo_izq]:
                hijo_menor = hijo_der

            if self.lista[i] <= self.lista[hijo_menor]:
                break

            self._intercambiar(i, hijo_menor)
            i = hijo_menor
            hijo_izq = 2 * i + 1

    def _intercambiar(self, i, j):
        self.lista[i], self.lista[j] = self.lista[j], self.lista[i]

class ColaDePrioridad:
    def __init__(self):
        self.monticulo = MonticuloBinario()

    def insertar(self, item):
        self.monticulo.insertar(item)

    def eliminarMin(self):
        return self.monticulo.eliminarMin()

    def estaVacia(self):
        return self.monticulo.estaVacio()