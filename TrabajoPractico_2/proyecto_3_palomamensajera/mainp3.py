import os
from modules.Aldeas import construir_grafo, prim

def main():
    ruta_archivo = "/home/emanuel/Documentos/AyED2025c1-Mondino-Canteros-Laval/TrabajoPractico_2/proyecto_3_palomamensajera/docs/aldeas.txt"
    if not os.path.exists(ruta_archivo):
        print(f"Error: el archivo no existe en la ruta {ruta_archivo}")
        return

    grafo = construir_grafo(ruta_archivo)
    if not grafo:
        print("No se pudo construir el grafo.")
        return

    aldea_inicial = next(iter(grafo.keys()))
    mst = prim(grafo, aldea_inicial)

    recibe_de = {}
    envia_a = {}

    for origen, destino, _ in mst:
        recibe_de[destino] = origen
        envia_a.setdefault(origen, []).append(destino)

    aldeas = sorted(grafo.keys())
    print("Estado de la red de mensajes:")
    for aldea in aldeas:
        if aldea == aldea_inicial:
            print(f"{aldea}: Origen (no recibe de nadie)")
        else:
            origen = recibe_de.get(aldea, "¿Desconocido?")
            print(f"{aldea}: Recibe de {origen}")

        destinos = envia_a.get(aldea, [])
        if destinos:
            print(f"  Envía réplica a: {', '.join(destinos)}")
        else:
            print(f"  No envía réplicas")

    print("\nConexiones para enviar el mensaje (Árbol de Expansión Mínima):")
    for origen, destino, distancia in sorted(mst):
        print(f"{origen} > {destino} ({distancia} leguas)")

    distancia_total = sum(distancia for _, _, distancia in mst)
    print(f"\nDistancia total mínima para entregar el mensaje: {distancia_total} leguas")


if __name__ == "__main__":
    main()


