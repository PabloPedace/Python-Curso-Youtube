#Tuplas
#Las tuplas son listas nmutables, es deicr, no se pueden modificar despues de su creacion.
#No permiten añadir, eliminar, mover elementos.
#Si permiten extraer porciones, pero el resultado de la extraccion
#es una nueva tupla
#No permiten busquedas 
#Si permiten comprobar si un elemento se encuentra en la tupla
#Sintaxis:
#nombreTupla=(elem1, elem2, elem3....)

miTupla=("Pablo", 13, 12, 1994, 12)
miLista=list(miTupla)
print(miTupla)
print(miTupla[2])
print(miTupla.count(12)) #Dos veces esta el numero 12
print(len(miTupla)) #Length: longitud de la tupla. Cuantos elementos hay

#Desempaquetado de tuplas

nombre, dia1, mes, año, dia2=miTupla
print(nombre)
print(dia1)
print(mes)
print(año)
print(dia2)

#Transformar una tupla en una lista
print(miLista)
#Transformar una lista en una tupla
#miTupla=tuple(miLista)

x = (1, 2, 3)

print(type(x))

y = tuple((1, 2, 3))
print(y)

#print(dir(x)

m = (1, 2)
print(m)
print(type(m)) #En la consola estoy teniendo un entero porque es un solo dato,
#la tupla debe tener multiples datos. Si hay un solo dato no se cosidera una tupla.

n = (1, 2, 3, 4, 5)
print(n[3])

#del x #Elimino la variable
#print(x)

locations = {
    (32.5216, 28.35482): "Londres",
    (56.25481, 56.358): "Roma",
    "Madrid": (23.8745, 25.9562)
}

print(locations)

