#Serializacion
#Bibliotecas necesarias:
#Pickle: Metodo dump(): volcado de datos al fichero binario externo
#        Metodo load(): carga de los datos del fichero binario externo

import pickle

lista_nombres=["Pedro", "Ana", "María", "Isabel"]

fichero_binario=open("lista_nombres", "wb") #wb:escritura binaria

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()  

del (fichero_binario)

########leer el fichero

import pickle

fichero=open("lista_nombres", "rb") #rb: lectura binaria

lista=pickle.load(fichero)

print(lista)













