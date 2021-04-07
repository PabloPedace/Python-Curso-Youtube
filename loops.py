#Bucles

#Sintaxis:

#for variable in elemento a recorrer:
#     Cuerpo del bucle

#Bucle for

for i in [1, 2, 3]:
    print("Hola")

for i in ["verano", "otoño", "invierno", "primavera"]:
    print("Hello")

for i in ["verano", "otoño", "invierno", "primavera"]:
    print(i)           

for i in [100, 200, 300]:
    print("Adios", end="  ") #Lo imprime todo el linea, gracias al end=""
#Adios  Adios  Adios

#Condicional dentro de un bucle for

email=False
miEmail=input("Introduce tu direccion de email: ")

for i in "pablopedace94@gmail.com":

    if(i=="@"):

        email=True

if email==True:
    print("Email es correcto")
else:
    print("El email no es correcto")

#Condicional y contador dentro de un bucle for

contador=0
miEmail=input("Introduce tu direccion de email: ")

for i in miEmail:

    if(i=="@" or i=="."):

        contador=contador+1

if contador==2:
    print("Email es correcto")
else:
    print("El email no es correcto")                

#Bucle for con el range

for i in range(5):
    print("Hola")

for i in range(5):
    print(i)    

for i in range(5, 10):
    print(f"Valor de la variable {i}") #Comienza del 5 hasta el 9

for i in range(5, 50, 3):
    print(f"Valor de la variable {i}") #Comienza del 5 
                                       #Termina en el 49
                                       #Va de 3 en 3

################

valido=False
email=input("Introduce tu email: ")

for i in range(len(email)):

    if email[i]=="@":

        valido=True

if valido:
    print("Email correcto")
else:
    print("Email no correcto")                

#Bucle while

#Sintaxis:

#while condicion:
#      cuerpo del bucle

i=1

while i <= 10:
    print("Ejecución " + str(i))
    i=i+1
print("Terminó la ejecución")

##################

edad=int(input("Introduce tu edad por favor: "))

while edad < 5 or edad > 100:
    print("Has introducido una edad incorrecta. Vuelve a intentarlo")
    edad=int(input("Introduce tu edad por favor: "))

print("Gracias por colaborar. Puede pasar")
print("Edad del aspirante " + str(edad))

##############

import math

print ("Programa de calculo de raiz cuadrada")
numero=int(input("Introduce un numero por favor: "))

intentos=0

while numero < 0:
    print("No se puede hallar la raiz de un numero negativo")

    if intentos == 2:
        print("Has consumido demasiados intentos. El programa ha finalizado")
        break;

    numero=int(input("Introduce un numero por favor: "))
    if numero < 0:
        intentos=intentos+1

if intentos < 2:
    solucion=math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero) + " es " + str(solucion))

#Continue, pass y else

#Continue

for letra in "Python":

    if letra == "h":
        continue
    print("Viendo la letra: " + letra) 


nombre="Pildoras Informaticas"

print(len(nombre)) #Cuenta los caracteres

#Continue

nombre="Pildoras Informaticas"

contador=0

for i in nombre:
    if i==" ":
        continue
    contador+=1

print(contador)

#Pass

while True:
    pass

class MiClase:
    pass # Para implementar más tarde

email=input("Introduce tu email, por favor: ")

for i in email:

    if i == "@":

        arroba = True

        break;

else:

    arroba=False

print(arroba)




























