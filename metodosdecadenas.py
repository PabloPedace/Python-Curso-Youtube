#Metodos de cadenas
#Uso de metodos de cadenas: string

myStr = "hello world"

print("HELLO WORLD AND " + myStr) #Concatenacion
print(f"HELLO WORLD AND {myStr}") #Concatenacion con f
print("HELLO WORLD AND {0}".format(myStr)) #Concatenacion


#print(dir(myStr))

# print(myStr.upper()) #Convierte todo en mayuscula
# print(myStr.lower()) #Convierte todo en minuscula
# print(myStr.swapcase()) #Cambia de mayusucla a minuscula y viceversa
# print(myStr.capitalize()) #Convierte la primera letra del texto en mayuscula
# print(myStr.replace("hello", "bye")) #Remplaza la palabras o letras que queres
# print(myStr.replace("hello", "bye").upper())
# print(myStr.count("l")) #Muestra cuntas veces se repite la letra
# print(myStr.startswith("hola")) #Muestra si la palabra que empieza el texto es verdadera o falsa
# print(myStr.startswith("hello")) #Muestra si la palabra que empieza el texto es verdadera o falsa
# print(myStr.startswith("he")) #Muestra si la palabra que empieza el texto es verdadera o falsa
# print(myStr.endswith("world")) #Muestra si la palabra que termina el texto es verdadera o falsa
# print(myStr.split()) #Separa los caracteres "Separa las palabras utilizando espacios"
# print(myStr.strip()) #Borra los espacios sobrantes al principio y al final
# print(myStr.split("o")) #Separa los caracteres "Separa las palabras utilizando espacios"
# print(myStr.find("o")) #Busca en que posicion estan los caracteres
# print(myStr.rfind()) #Representa el indice de un caracter, pero lo hace contando desde atras
# print(len(myStr)) #Muestra la longitud
# print(myStr.find("e"))
# print(myStr.index("e"))
# print(myStr.isdigit()) #Devuelve un booleano
# print(myStr.isnumeric()) #Muestra si es numerico
# print(myStr.isalpha()) #Muestra si es numerico
# print(myStr.isalum()) #Comprueba si son alphanumericos

print(myStr[4]) #Muestra en que posicion esta la letra
print(myStr[-5]) #Muestra en que posicion esta la letra inversamente

nombreUsuario=input("Introduce tu nombre de Usuario: ")

print("El nombre es: ", nombreUsuario.upper())
print("El nombre es: ", nombreUsuario.lower())
print("El nombre es: ", nombreUsuario.capitalize())

edad=input("Introduce la edad: ")

while(edad.isdigit()==False):
    print("Por favor, introduce un valor numerico")
    edad=input("Introduce la edad: ")
    
if (int(edad)<18):
    print("No puede pasar")
else:
    print("Puedes pasar")    