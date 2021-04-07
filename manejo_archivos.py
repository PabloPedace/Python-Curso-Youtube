from io import open

archivo_texto=open("archivo.txt","w")

frase="Estupendo día para estudiar Python \n,  el martes"

archivo_texto.write(frase)

archivo_texto.close()

##############Lee el texto.txt

archivo_texto=open("archivo.txt","r")

print(archivo_texto.read()) #Lee el texto.txt

archivo_texto.seek(0)

print(archivo_texto.read())

#lineas_texto=archivo_texto.readlines() #Lee el texto decorrido
#print(lineas_texto[0])
archivo_texto.close()





#########Agregar una tercera linea

archivo_texto=open("archivo.txt","a")

archivo_texto.write("\n siempre es una buena ocasión para estudiar Python")

archivo_texto.close()


