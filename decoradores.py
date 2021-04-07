#Decoradores
#Son funciones que a su vez añaden funcionalidaes a otra funciones
#Decoran a otras funcionees, les añaden funcinalidades
#Estructura de un decorador:
#3 funciones (A, B y C) donde A recibe como parametro a B para devolver C.
#Un decorador vuelve a una funcion
#
#              def funcion_decorador(funcion):
#                 def funcion_integral():
#                     #codigo de la funcion interna
#                  return funcion_interna

def funcion_decoradora(funcion_parametro):

    def funcion_interior(*args, **kwargs):

        #Acciones adicionales que decoran, que agregan

        print("Vamos a realizar un calculo: ")

        funcion_parametro(*args, **kwargs)

        #Acciones adicionales que decoran

        print("Hemos terminado el calculo")

    return funcion_interior

@funcion_decoradora
def suma(num1, num2, num3):

    print(num1+num2+num3)

@funcion_decoradora
def resta(num1, num2):

    print(num1-num2)

@funcion_decoradora
def potencia(base, exponente):

    print(pow(base, exponente))

suma(7, 5, 8)

resta(12, 10)

potencia(base=5, exponente=3)

































