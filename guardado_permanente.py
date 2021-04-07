import pickle 

class Persona:

    def __init__(self, nombre, genero, edad):
        
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona nueva con el nombre de ", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:

    personas=[]

    def __init__(self):

        listaDePeronas=open("ficheroExterno", "ab+") #Agregar informacion binaria
        listaDePeronas.seek(0) #Desplaza a la posicion 0

        try:
            self.personas=pickle.load(listaDePeronas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))            
        except:
            print("El fichero está vacío")
        finally:
            listaDePeronas.close()
            del(listaDePeronas)

    def agregarPersonas(self, p):
        self.personas.append(p)

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonasEnFicheroExterno(self):
        listaDePeronas=open("ficheroExterno", "wb") #Escrbir binaria
        pickle.dump(self.personas, listaDePersonas)
        listaDePeronas.close()
        del(listaDePeronas)

    def mostrarInfoFicheroExterno(self):
        print("La informacion del fichero eterno es la siguiente: ")
        for p in self.personas:
            print (p)

miLista=ListaPersonas()
persona=Persona("Sandra", "Femenino", 29)
miLista.agregarPersonas(persona)
miLista.mostrarInfoFicheroExterno()

p=Persona("Sandra", "Feminino", 29)
miLista.agregarPersonas(p)
p=Persona("Antonio", "Masculino", 39)
miLista.agregarPersonas(p)
p=Persona("Ana", "Feminino", 19)
miLista.agregarPersonas(p)

miLista.mostrarPersonas()






































