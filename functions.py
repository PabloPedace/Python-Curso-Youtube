#¿Qué son?
#Conjunto de líneas de código agrupadas(bloque de código) que funcionan como una unidad realizando una tarea específica.
#Las funciones en Python pueden devolver valores.
#Las funciones en Python pueden tener parámetros/argumentos
#A las funciones también se las denomina "métodos" cuando se encuntran definidas dentro de una clase

#Sintaxis
# def nombre_funcion():
#     . Inst(prucciones de la función
#     . return (opcional)

# def nombre_función(parámetros)
#     . Instrucciones de la función
#     . resturn (opcional)

#Ejecución

#nombre-función()
#Nombre_función(parámetros)

def hello():
    print("Hello world!")

hello()

def hello(name):
    print("Hello " + name + "!")

hello("Pablo")

#Parametro por defecto

def hello(name="Person"):
    print("Hello " + name + "!")

hello("Pablo")
hello()

def add(numero1, numero2):
    return numero1 + numero2

print(add(10, 10))

add = lambda numberOne, numberTwo: numberOne + numberTwo
print(add(10, 20))


print(len("hello")) #Me dice la cantidad de caracteres

def mensaje():

    print("Estamos aprendiendo python")

mensaje()

def suma():
    num1=5
    num2=7
    print(num1+num2)

suma()

def suma(num1, num2):
    
    print(num1+num2)

suma(5, 7)

def suma(num1, num2):
    
    resultado=num1+num2

    return resultado

print(suma(5, 7))

def suma(num1, num2):
    
    resultado=num1+num2

    return resultado

almacena_resultado=suma(5, 7)

print(almacena_resultado)


















