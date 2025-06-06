from modules.TemperaturasDB import Temperaturas_DB

def mostrar_menu():
    print("\n   MENÚ  ")
    print("1-Guardar temperatura")
    print("2-Consultar temperatura por fecha")
    print("3-Listar temperaturas en rango")
    print("4-Temperaturas máxima y mínima en rango")
    print("5-Eliminar temperatura por fecha")
    print("6-Ver cantidad de muestras")
    print("7-Listar temperaturas formateadas en rango")
    print("8-Salir")


def pedir_fecha(mensaje):
    return input(f"{mensaje} (dd-mm-aaaa): ")

def main():
    db=Temperaturas_DB()
    while True:
        mostrar_menu()
        opcion=input("Selecciones una opción:")

        if opcion=="1":
            fecha=pedir_fecha("Ingresar fecha")
            try:
                temperatura=float(input("Ingresar temperatura: "))
                db.guardar_temperatura(temperatura,fecha)
                print("La temperatura ha sido guardada")
            except :
                print(ValueError)
            

        if opcion=="2":
            fecha_consulta= pedir_fecha("Ingresar la fecha a consultar:")
            temp=db.devolver_temperatura(fecha)
            if temp is not None:
                print(f"Temperatura: {temp} °C")
            else:
                print("No se encontró la temperatura para la fecha ingresada")


        if opcion=="3":
            fecha1=pedir_fecha("Ingresar fecha de inicio:")
            fecha2=pedir_fecha("Ingresar fecha final:")
            try:
                datos=db.listar_temperaturas_en_rango(fecha1,fecha2)
                if datos:
                    for fecha, temp in datos:
                        print(f"{fecha.strftime('%d/%m/%Y')}: {temp} °C")
                else:
                        print("No hay datos en ese rango")
            except:
                print(ValueError)


        if opcion=="4":
            fecha1=pedir_fecha("Ingresar fecha de inicio:")
            fecha2=pedir_fecha("Ingresar fecha final:")
            temp_min,temp_max=db.temp_extremos_rango(fecha1,fecha2)
            if temp_min or temp_max is not None:
                print(f"Temperatura Mínima: {temp_min} °C")
                print(f"Temperatura Máxima: {temp_max} °C")
            else:
                print("No se encontraron datos en ese rango")
        
        if opcion=="5":
            fecha=pedir_fecha("Ingresar la fecha a eliminar: ")
            if db.borrar_temperatura(fecha):
                print("Temperatura eliminada")
            else:
                print("No se encontró una temperatura correspondiente a esa fecha")
            

        if opcion=="6":
            print(f"Cantidad de muestras: {db.cantidad_muestras()}")


        if opcion=="7":
            fecha1=pedir_fecha("Ingresar fecha de inicio:")
            fecha2=pedir_fecha("Ingresar fecha final:")
            try:
                lista=db.devolver_temperaturas(fecha1,fecha2)
                if lista:
                    print("\n Temperaturas:")
                    for i in lista:
                        print(i)
                else:
                    print("No hay registros en ese rango")
            except:
                print(ValueError)



        elif opcion=="8":
            break

if __name__== "__main__":
    main()
