import heapq
from collections import defaultdict

def construir_grafo(aldea):
    grafo = defaultdict(list)
    with open(aldea, 'r') as file:
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
                grafo[u].append((v, w))
                grafo[v].append((u, w))  # Grafo no dirigido
    return grafo

def prim(grafo, inicio):
    visitados = set()
    mst = []  # (origen, destino, peso)
    heap = []

    visitados.add(inicio)
    for vecino, peso in grafo[inicio]:
        heapq.heappush(heap, (peso, inicio, vecino))

    while heap:
        peso, u, v = heapq.heappop(heap)
        if v in visitados:
            continue
        visitados.add(v)
        mst.append((u, v, peso))
        for vecino, costo in grafo[v]:
            if vecino not in visitados:
                heapq.heappush(heap, (costo, v, vecino))

    return mst

def procesar_red(mst):
    recibe_de = {}
    envia_a = defaultdict(list)

    for origen, destino, _ in mst:
        recibe_de[destino] = origen
        envia_a[origen].append(destino)

    return recibe_de, envia_a