#Expresiones regulares
#Son una secuencia de caracteres que forman un patron de busqueda
#Sirven para el trabajo y procesamiento de texto
#Ejemplos:
#Buscar un texto que se ajusta a un formato determinado(correo electronico)
#Buscar sin existe o no una cadena de caracteres dentro de un texto
#Contar el numero de coincidencias dentro de un texto
#Etc.

import re

cadena="Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"

print(re.search("aprender", cadena))
print(re.search("aprenderrrr", cadena))

textoBuscar="aprender"

if re.search(textoBuscar, cadena) is not None:

    print("He encontrado el texto")

else:

    print("No he encontrado el texto")    

textoEncontrado=re.search(textoBuscar, cadena)

print(textoEncontrado.start())

print(textoEncontrado.end())

print(textoEncontrado.span())

textoBuscar="Python"

print(re.findall(textoBuscar, cadena))

print(len(re.findall(textoBuscar, cadena)))
