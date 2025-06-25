
from modules.monticulo import MonticuloBinario, ColaDePrioridad
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