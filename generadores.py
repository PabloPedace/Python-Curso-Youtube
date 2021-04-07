#Generadores
#Estructuras que extraen valores de una funcion y se almacenan en objetos iterables (que se pueden recorrer).
#Estos valores se almacenan de uno en uno.
# Cada vez que un generador almacena un valor, esta permanece en un estado pausado hasta que se
#solicita el siguiente. Esta caracteristica es conocida como "suspension de estado".
#Son mas eficientes que las funciones tradicionales.
#Muy utiles con listas de valores infinitos
#Bajo determinados escenarios, sera muy util que un generador devuelva los valores de uno en uno.

#Sintaxis:

# def gerenaNumeros():
#     yield numeros -> return

def generaPares(limite):

    num=1

    miLista=[]

    while num < limite:

        miLista.append(num*2)

        num=num+1

    return miLista    

print(generaPares(10))

######################

def generaPares(limite):

    num=1

    while num < limite:

        yield num*2

        num=num+1

devuelvePares=generaPares(10)    

for i in devuelvePares:

    print(i)

###########################

def generaPares(limite):

    num=1

    while num < limite:

        yield num*2

        num=num+1

devuelvePares=generaPares(10)    

print(next(devuelvePares))

print("Aquí podría ir más código...")

print(next(devuelvePares))

print("Aquí podría ir más código...")

print(next(devuelvePares))

############## yield from

def devuelve_ciudades(*ciudades):

    for elemento in ciudades:
        #for subElemento in elemento:     
        yield from elemento

ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))












