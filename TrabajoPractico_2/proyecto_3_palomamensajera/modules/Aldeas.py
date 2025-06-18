class MinHeap:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)
        self._up(len(self.data) - 1)

    def pop(self):
        if not self.data:
            return None
        self._swap(0, len(self.data) - 1)
        item = self.data.pop()
        self._down(0)
        return item

    def _up(self, idx):
        parent = (idx - 1) // 2
        while idx > 0 and self.data[idx] < self.data[parent]:
            self._swap(idx, parent)
            idx = parent
            parent = (idx - 1) // 2

    def _down(self, idx):
        child = 2 * idx + 1
        while child < len(self.data):
            right = child + 1
            if right < len(self.data) and self.data[right] < self.data[child]:
                child = right
            if self.data[idx] <= self.data[child]:
                break
            self._swap(idx, child)
            idx = child
            child = 2 * idx + 1

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def is_empty(self):
        return not self.data


def construir_grafo(archivo):
    grafo = {}
    with open(archivo, 'r') as file:
        for n, line in enumerate(file, 1):
            if line.strip():
                partes = line.strip().split(', ')
                if len(partes) != 3:
                    print(f"[Línea inválida #{n}] '{line.strip()}' — Se esperaba: origen, destino, distancia")
                    continue
                u, v, w = partes
                try:
                    w = int(w)
                except ValueError:
                    continue
                if u not in grafo:
                    grafo[u] = []
                if v not in grafo:
                    grafo[v] = []
                grafo[u].append((v, w))
                grafo[v].append((u, w))  # No dirigido
    return grafo


def prim(grafo, inicio):
    visitados = set()
    mst = []
    heap = MinHeap()

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


def procesar_red(mst):
    recibe_de = {}
    envia_a = {}

    for origen, destino, _ in mst:
        recibe_de[destino] = origen
        if origen not in envia_a:
            envia_a[origen] = []
        envia_a[origen].append(destino)

    return recibe_de, envia_a
