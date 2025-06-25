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

def prim(grafo, inicio):
    visitados = set()
    mst = []
    cola = ColaDePrioridad()

    visitados.add(inicio)
    for vecino, peso in grafo[inicio]:
        cola.insertar((peso, inicio, vecino))

    while not cola.estaVacia():
        peso, u, v = cola.eliminarMin()
        if v in visitados:
            continue
        visitados.add(v)
        mst.append((u, v, peso))
        for vecino, costo in grafo[v]:
            if vecino not in visitados:
                cola.insertar((costo, v, vecino))

    return mst

def construir_grafo(ruta_archivo):
    grafo = {}
    try:
        with open(ruta_archivo, 'r') as archivo:
            for numero_linea, linea in enumerate(archivo, 1):
                if linea.strip():
                    partes = linea.strip().split(', ')
                    if len(partes) != 3:
                        print(f"[Línea inválida #{numero_linea}] '{linea.strip()}' — Se esperaba: origen, destino, distancia")
                        continue
                    origen, destino, peso = partes
                    try:
                        peso = int(peso)
                    except ValueError:
                        print(f"[Línea inválida #{numero_linea}] Peso no es un número: '{peso}'")
                        continue
                    if origen not in grafo:
                        grafo[origen] = []
                    if destino not in grafo:
                        grafo[destino] = []
                    grafo[origen].append((destino, peso))
                    grafo[destino].append((origen, peso))  # grafo no dirigido
    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta_archivo}")
        return None
    return grafo