#Listas
#Estructura de datos que nos permite almacenar gran cantidad
#de valores(equivalente a los array en otros lenguajes de programacion)
#En Python las lista pueden guardar diferente tipo de valores(en otros
#lenguajes no ocurre esto con los array)
#Se pueden expandir dinamicamente añadiendo nuevos elementos(otra)
#novedad respecto a los arrays en otros lenguajes
#
#Sintaxis
#nombreLista=[elem1, elem2, elem3....]

miLista=["María", "Pepe", "Marta", "Antonio"] * 3
print(miLista)
print(miLista[2])
print(miLista[-3])

#Porcion

print(miLista[0:3]) #Incluye el indice 0, 1 y 2, el 3 lo excluye
print(miLista[:2]) #Incluye el indice 1 y 1
print(miLista[2:]) #Incluye el indice 2 y 3

miLista.append("Carlos")
miLista.insert(2,"Sandra")
miLista.extend(["Pablo", "Ana", "Lucia"])
print(miLista) 
print(miLista.index("Pablo"))
print("Ana" in miLista) 

demo_list = [100, "Hello", True, [1, 2, 3, 'Hello World']]
print(demo_list)

colors = ["red", "blue", "green", "red"]

numero_lista = list((1, 2, 3, 4))
print(numero_lista)

numeros_listas = list((1, 2, 3, 4))
print(type(numeros_listas))

r = list(range(1, 11)) 
print(r)

print(type(colors))
print(dir(colors))
print(len(colors)) #Longitud
print(colors[1])
print("green" in colors)
print("orange" in colors)
print(colors)
#colors[1] = "black"
#print(colors)

#colors.append(("white", "yellow")) #Adjuntar
#colors.append(["white", "yellow"]) #Ampliar
colors.extend(["white", "yellow"])
print(colors)

(colors.insert(1, "violet")) #Inserta en cualquier posicion
colors.insert(len(colors), "violet") #Inserta en la ultima posicion 
colors.pop() #o colors.pop(2) #Elimino el ultimo elemento
colors.remove("green") #Elimio el elemento green
#colors.clear() #Limpia todos los valores
colors.sort() #Ordena alfabeticamente
colors.sort(reverse=True) #Ordena alfabeticamente de manera inversa
print(colors.index("red"))
print(colors.index("yellow"))
print(colors.count("red"))
print(colors)













