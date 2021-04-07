#Funciones filter: programacion funcional
#Verifica que los elementos de una secuencia cumplen una condicion,
#devolviendo un iterador con los elementos que cumplen dicha condicion

def numero_par(num):

    if num % 2==0:

        return True 

numeros=[17, 24, 7, 39, 8, 51, 92]

print(list(filter(numero_par, numeros)))

#Funcion filter con lambda

numeros=[17, 24, 7, 39, 8, 51, 92]

print(list(filter(lambda numero_par:numero_par%2==0, numeros)))

#Funcion filter para filtrar objetos

class Empleado:

    def __init__(self, nombre, cargo, salario):

        self.nombre=nombre

        self.cargo=cargo

        self.salario=salario

    def __str__(self):

        return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre, self.cargo, self.salario)

listaEmpleados=[

    Empleado("Juan", "Director", 750000),

    Empleado("Ana", "Presidente", 850000),

    Empleado("Antonio", "Administrativo", 25000),

    Empleado("Sara", "Secretaria", 27000),

    Empleado("Mario", "Botones", 21000),
]

salarios_altos=filter(lambda empleado:empleado.salario>50000, listaEmpleados)

for empleado_salario in salarios_altos:

    print(empleado_salario)






