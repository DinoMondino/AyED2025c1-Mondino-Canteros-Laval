"""Querer conectar todas las aldeas con la mínima distancia total y asegurando que cada aldea reciba el mensaje una 
única vez se resuelve con un Árbol de Expansión Mínima (MST). El algoritmo de Prim construye el MST comenzando desde 
una aldea inicial. En cada paso, agrega la arista de menor peso que conecta una aldea ya incluida en el MST 
con una aldea que aún no está en el MST. Esto garantiza que en cada etapa se está haciendo la conexión más barata.
"""
from modules.monticulo import MonticuloBinario, ColaDePrioridad

def prim(grafo, inicio):
    visitados = set()
    mst = [] # almacena las aristas del MST en el formato (origen, destino, peso)
    cola = ColaDePrioridad() #  para almacenar las aristas candidatas, priorizándolas por su peso.

    visitados.add(inicio)
    for vecino, peso in grafo[inicio]:
        cola.insertar((peso, inicio, vecino)) # insertar las aristas desde el nodo inicial

    while not cola.estaVacia(): 
        peso, u, v = cola.eliminarMin()
        if v in visitados: # si el nodo ya fue visitado, no lo procesamos
            continue
        visitados.add(v) # agregar el nodo recién visitado al conjunto de visitados
        mst.append((u, v, peso)) # agregar la arista al MST
        for vecino, costo in grafo[v]: #  Para cada vecino, si no ha sido visitado, se añade a la cola de prioridad.
            if vecino not in visitados:
                cola.insertar((costo, v, vecino)) 

    return mst

def construir_grafo(ruta_archivo):
    grafo = {} # diccionario para almacenar el grafo, donde las claves son aldeas y los valores son listas de tuplas (vecino, peso)
    try:
        with open(ruta_archivo, 'r') as archivo:
            for numero_linea, linea in enumerate(archivo, 1):
                if linea.strip():
                    partes = linea.strip().split(', ')
                    if len(partes) != 3: # verificar que la línea tenga exactamente 3 partes: origen, destino, peso
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