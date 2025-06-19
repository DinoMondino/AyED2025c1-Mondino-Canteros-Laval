class MonticuloMinimo:
    def __init__(self):
        self.datos = []

    def push(self, elemento):
        self.datos.append(elemento)
        self._subir(len(self.datos) - 1)

    def pop(self):
        if not self.datos:
            return None
        self._intercambiar(0, len(self.datos) - 1)
        minimo = self.datos.pop()
        self._bajar(0)
        return minimo

    def _subir(self, indice):
        padre = (indice - 1) // 2
        while indice > 0 and self.datos[indice] < self.datos[padre]:
            self._intercambiar(indice, padre)
            indice = padre
            padre = (indice - 1) // 2

    def _bajar(self, indice):
        hijo_izquierdo = 2 * indice + 1
        while hijo_izquierdo < len(self.datos):
            hijo_derecho = hijo_izquierdo + 1
            hijo_menor = hijo_izquierdo

            if hijo_derecho < len(self.datos) and self.datos[hijo_derecho] < self.datos[hijo_izquierdo]:
                hijo_menor = hijo_derecho

            if self.datos[indice] <= self.datos[hijo_menor]:
                break

            self._intercambiar(indice, hijo_menor)
            indice = hijo_menor
            hijo_izquierdo = 2 * indice + 1

    def _intercambiar(self, i, j):
        self.datos[i], self.datos[j] = self.datos[j], self.datos[i]

    def is_empty(self):
        return not self.datos

def prim(grafo, inicio):
    visitados = set()
    mst = []
    heap = MonticuloMinimo()

    visitados.add(inicio)
    for vecino, peso in grafo[inicio]:
        heap.push((peso, inicio, vecino))

    while not heap.is_empty():
        peso, u, v = heap.pop()
        if v in visitados:
            continue
        visitados.add(v)
        mst.append((u, v, peso))
        for vecino, costo in grafo[v]:
            if vecino not in visitados:
                heap.push((costo, v, vecino))
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