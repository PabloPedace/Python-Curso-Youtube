#Funcion Lambda: es una funcion anonima.
#Se utiliza para abreviar
#Nunca podra tener bucles o condicionales, solo son para operaciones sencillas

def area_triangulo(base, altura):

    return (base*altura)/2

print(area_triangulo(5,7))

triangulo1=area_triangulo(5,7)
triangulo2=area_triangulo(5,7)

print(triangulo1)
print(triangulo2)

#Funcion Lambda

area_triangulo=lambda base,altura:(base*altura)/2

triangulo3=area_triangulo(8,4)
triangulo4=area_triangulo(10,5)

print(triangulo3)
print(triangulo4)

#Otro ejemplo con funcion lambda

al_cubo=lambda numero:pow(numero, 3)

#Otra opcion

al_cubo=lambda numero:numero**3

print(al_cubo(13))

#Otro ejemplo con funcion lambda

destacar_valor=lambda comision:"¡{}! $".format(comision)

comision_Ana=15585

print(destacar_valor(comision_Ana))


























