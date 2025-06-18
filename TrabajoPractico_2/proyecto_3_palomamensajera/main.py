import os
from modules.Aldeas import construir_grafo, prim, procesar_red

def main():
    ruta = "docs/aldeas.txt"
    if not os.path.exists(ruta):
        print(f"Error: el archivo no existe en la ruta {ruta}")
        return

    grafo = construir_grafo(ruta)
    inicio = 'Peligros'
    mst = prim(grafo, inicio)
    recibe_de, envia_a = procesar_red(mst)

    # Mostrar estado de la red
    print("Estado de la red de mensajes:")
    aldeas = list(grafo.keys())
    for aldea in sorted(aldeas):
        origen = recibe_de.get(aldea, None)
        destinos = envia_a.get(aldea, [])

        if aldea == inicio:
            print(f"{aldea}: Origen (no recibe de nadie)")
        else:
            print(f"{aldea}: Recibe de {origen}")

        if destinos:
            print(f"  Envía réplica a: {', '.join(destinos)}")
        else:
            print("  No envía réplicas")

    # Conexiones MST
    print("\nConexiones para enviar el mensaje (MST):")
    for u, v, peso in sorted(mst):
        print(f"{u} > {v} ({peso} leguas)")

    # Distancia total
    total = sum(peso for _, _, peso in mst)
    print(f"\nDistancia total mínima para entregar el mensaje: {total} leguas")

if __name__ == "__main__":
    main()
