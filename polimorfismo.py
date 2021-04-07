class Coche():

    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():

    def desplazamiento(self):
        print("Me dessplazo utilizando dos ruedas")

class Camion():

    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")

def desplazamientoVehiculo(vehiculo): #Polimorfismo
    vehiculo.desplazamiento()

miVehiculo=Camion()

desplazamientoVehiculo(miVehiculo)


