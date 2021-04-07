#Condicionales

#if

nota_alumno=input("Introduce la nota: ")

def evaluacion(nota):
    valoracion="aprobado"
    if nota < 5:
        valoracion = "suspenso"
    return valoracion    
print(evaluacion(4))
print(evaluacion(6))
print(evaluacion(int(nota_alumno)))

#if, else

edad_usuario=int(input("Introduce tu edad, por favor: "))

if edad_usuario < 18:
    print("No puedes pasar")
elif edad_usuario > 100:
    print("Edad incorrecta")
else:
    print("Puedes pasar")

######################      

nota_alumnos=int(input("Introduce la nota, por favor: "))

if nota_alumnos < 5:
    print("Insuficiente")
elif nota_alumnos < 6:
    print("Suficiente")
elif nota_alumnos < 7:
    print("Bien")
elif nota_alumnos < 9:
    print("Notable")
else:
    print("Sobresaliente") 

####################

x = 50

if x > 60:
    print("x es mayor que 60")
else:
    print("x es menor que 60")

 ##################   

color = "azul"

if color == "rojo":
    print("El color es rojo")
else:
    print("Otro color")

color = "rojo"

if color == "rojo":
    print("El color es rojo")
else:
    print("Otro color")

#elif

color = "azul"

if color == "rojo":
    print("El color es rojo")
elif color == "azul":
    print("El color es azul")
else:
    print("Otro color")

########################    

color = "verde"

if color == "rojo":
    print("El color es rojo")
elif color == "azul":
    print("El color es azul")
else:
    print("Otro color")

#Varios if, else, elif

nombre = "Carlos"
apellido = "Perez"

if nombre == "Pablo":
    if apellido == "Pedace":
        print("Yo soy Pablo Pedace")
    else:
        print("Yo no soy Pablo Pedace")
else:
    print("Yo no soy Pablo")

##################################

salario_presidente=int(input("Introduce salario del presidente: "))
print("Salario presidente: " + str(salario_presidente))

salario_director=int(input("Introduce salario del director: "))
print("Salario del director: " + str(salario_director))

salario_jefe_area=int(input("Introduce salario del Jefe de Área: "))
print("Salario del Jefe de Área: " + str(salario_jefe_area))

salario_administrativo=int(input("Introduce salario del Administrativo: "))
print("Salario del Administrativo: " + str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("Todo funciona correctamente")
else:
    print("Algo falla en esta empresa")    


##and, or, not

x = 5
y = 7

if x > 2 and x <= 10:
    print("x es mayor a 2 y x es menor o igual a 10")
if x > 2 or x <= 20:
    print("x es mayor a 2 o x es menor o igual a 20")
if (not(x == y)):
    print("x no es igual a y")

############################and, or, not

distancia_escuela=int(input("Introduce la distancia a la escuela en km: "))
print(distancia_escuela)

numero_hermanos=int(input("Introduce el n° de hermanos en el centro: "))
print(numero_hermanos)

salario_familiar=int(input("Introduce el salario anual bruto: "))
print(salario_familiar)

if distancia_escuela > 40 and numero_hermanos > 2 or salario_familiar <= 20000:
    print("Tienes derecho a la beca")
else:
    print("No tienes derecho a la beca")       

##################### in

print("Informatica grafica - Prueba de software - Usabilidad y accesibilidad")
asignatura=input("Escribe la asignatura escogida: ")

#opcion=input("Escribe la asignatura escogida: ")
#asignatura=opcion.lower()

if asignatura in ("Informatica grafica", "Prueba de software", "Usabilidad y accesibilidad"):
    
    print("Asignatura elegida: " + asignatura)

else:

    print("La asignatura escogida no esta contemplada")

#lower() -> Transforma todo en minuscula
#upper() -> Transforma todo en mayuscula




    

