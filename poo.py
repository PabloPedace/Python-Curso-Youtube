#Programacion orientada a objetos
#Consiste en trasladar la naturaleza de los objetos de la vida real
#al codigo de programacion.
#Naturaleza de un objeto de la vida real: los objetos tienen un estado, un comportamiento y unas propiedades.
#Ejemplo: objeto coche
#¿Cuál es el estado de un coche? Un coche puede estar parado, circulando, aparcado etc
#¿Qué propiedades tiene un coche? Un coche tiene un color, un peso, un tamaño.
#¿Qué comportamiento tiene un coche? Un coche puede arrancar, frenar, acelerar, girar.
#Objeto:
#Tiene propiedades (atributos):
#Color
#Peso
#Alto
#Largo
#Tiene un comportamiento (¿Qué es capaz de hacer?):
#Arrancar
#Frenar
#Girar
#Acelerar
#Ventajas de POO:
#Programas divididos en trozos, partes, modulos o clases. Modularizacion.
#Muy reutilizable. Herencia.
#Si existe fallo en alguna linea del codigo, el programa continuara con su funcionamineto. Tratamiento de Excepciones.
#Encapsulamiento.
#Vocabulario en la POO
#Clase: modelo donde se redactan las caracterisitcas comunes de un grupo de objetos (chasis y ruedas).
#Objeto
#Ejemplar de clase. Instancia de clase.
#Modularizacion
#Encapsulamiento / encapsulacion.
#Herencia
#Polimorfismo

#Objeto: nomenclatura del punto.

#Herencia:
#Para reutilizar codigo en caso de crear objetos similares


class Coche():
    #Metodo Constructor: _init_
    def __init__(self):

        #Clases: caracterisitcas comunes del coche
        self.__largoChasis=250 #Encapusla la variable largoChasis
        self.__anchoChasis=120 #Encapusla la variable anchoChasis
        self.__ruedas=4 #Encapusla la variable ruedas
        self.__enmarcha=False #Encapusla la variable enmarcha

    #self: objeto perteneciente a la clase, es como el "this"
    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos

        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()

        if(self.__enmarcha and chequeo):
            return "El coche está en marcha"
        elif(self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo"
        else:
            return "El coche está parado"

    def estado(self):
        print("El coche tiene " , self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ",
            self.__largoChasis)
    
    def __chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina="Ok"
        self.aceite="Ok"
        self.puertas="Cerradas"

        if(self.gasolina=="Ok" and self.aceite=="Ok" and self.puertas=="Cerradas"):
            return True
        else:
            return False

miCoche=Coche() #Instanciar una clase

print(miCoche.arrancar(True))

miCoche.estado()

print("----------A continuación creamos el segundo objeto----------")

miCoche2=Coche()

print(miCoche2.arrancar(False))

miCoche2.ruedas=2

miCoche2.estado()































































