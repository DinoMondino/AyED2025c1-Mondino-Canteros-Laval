from random import randint, choices

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
# probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6] 

class Paciente:
    def __init__(self):
        n = len(nombres)
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]

    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_riesgo(self):
        return self.__riesgo
    
    def get_descripcion_riesgo(self):
        return self.__descripcion
    
    def comparar(self):
        pass
    
    def __str__(self):
        cad = self.__nombre + ' '
        cad += self.__apellido + '\t -> '
        cad += str(self.__riesgo) + '-' + self.__descripcion
        return cad
    

    class MonticuloBinario():
    def __init__(self,__lista=None):
        if __lista is None:
            self.__lista = [0]
        else:
            self.__tamanio=len(__lista)
            self.__lista = [0].extend(__lista)

        self.__tamanio = 0
        self.__contador=1
        self.actual = None
        

 def insertar(self, item):
        """Inserta un valor en la __lista y la ordena"""
        #recibimos el item y lo agregamos a la __lista del montículo
        self.__lista.append(item)
        #aumentamos el tamaño
        self.__tamanio+=1
        #como último paso, ordenamos el montículo
        self.infiltrar_arriba(self.__tamanio)

    def tamanio(self):
        return self.__tamanio

    def eliminarMin(self):
        """Quitamos el valor de la cima del montículo"""
        #Quitamos el paciente de arriba del montículo
        paciente = self.__lista[1]
        #Remplazamos el valor de arriba por el último agregado
        self.__lista[1] = self.__lista[self.__tamanio]
        #Quitamos el último valor agregado de la __lista
        self.__lista.pop()
        self.__tamanio-=1
        #Ordenamos la __lista filtrando hacia abajo el primer valor
        self.infiltrar_abajo(1)

        return paciente

