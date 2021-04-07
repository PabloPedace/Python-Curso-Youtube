#Diccionarios
#Estructura de datos que nos permite almacenar valores de diferente tipo(
#enteros, cadenas de texto, decimales) e incluso lista y otros diccionarios
#La principal caracteristica de los diccionarios es que los datos se almacenan asociados
#a una clave de tal forma que se crea una asociacion
#de tipo clave:valor para cada elemento almacenado.
#Los elementos almacenados no estan ordenados. El orden es indiferente
#a la hora de almacenar informacion en un diccionario.


Beethoven = {
    "Compositor": "Ludwig van Beethoven",
    "Nacionalidad": "Alemania",
    "Fecha de nacimiento": 1770,
    "Fecha de muerte": 1827,
    "Ópera": "Fidelio",
    "Año": 1814
}

#Añadir elementos al diccionario

Beethoven["Sinfonía N°3"]="Heróica"

print(Beethoven)
print(type(Beethoven))

#Elimino un elemento del diccionario

#del Beethoven["Año"]

Wagner = {
    "Compositor": "Richas Wagner",
    "Nacionalidad": "Alemania",
    "Fecha de nacimiento": 1813,
    "Fecha de muerte": 1883,
    "Ópera": "Tristán e Isolda",
    "Año": 1865
}

print(Wagner)
print(type(Wagner))

Verdi = {
    "Compositor": "Giuseppe Verdi",
    "Nacionalidad": "Italia",
    "Fecha de nacimiento": 1813,
    "Fecha de muerte": 1901,
    "Ópera": "Otelo",
    "Año": 1887
}

print(Verdi)
print(type(Verdi))

print(dir(Wagner))
print(Wagner.keys())
print(Verdi.copy())
print(Beethoven.items())

#del Beethoven #Elimino la variable
#print(Beethoven)

#Diccionario dentro de una lista
productos = [
    {"name": "libro", "price": 500},
    {"name": "libro", "price": 1000}
]

print(productos)
print(type(productos))

midiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":{"Temporadas":(1991, 1992, 1993, 1996, 1997, 1998)}}
print(midiccionario.keys()) #Me muestra las claves
print(midiccionario.values()) #Me muestra los valores
print(len(midiccionario)) #Me muestra la longitud del diccionario
print(midiccionario)

