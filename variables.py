name = "Pablo"
name = None #Consola= poner: type(None y me devolvera class 'NoneType'
print(100 + 1)
print(name)

x = 100 #Variable x

print(x)

#Case sensitive: aunque las dos variables tengan el mismo nombre,
#son diferentes porque una empieza con minuscula y la otra en mayusucla. 

ópera = "Lohengrin"
Ópera = "La valquiria"

print(ópera)
print(Ópera)

#Una variable nunca puede empezar con un numero
#Ejemplo: 2books = .....
#Puede empezar con un guion bajo
#Ejemplo: _2books = .....

ópera, añoestreno = "Tristán e Isolda", 1865

print(ópera)
print(añoestreno)
print(ópera, añoestreno)

#Conventions

#compositor_nombre = "Ludwig van Beethoven" #snake_case
compositorNombre = "Richard Wagner" #camelCase
CompositorNombre = "Gustav Mahler" #PascalCase

#print(compositor_nombre) 
print(compositorNombre) 
print(CompositorNombre)

#Cambiar de valor: en la practica las variables pueden ser reasignadas,
#por eso, Python es un lenguaje de tipado dinamico

compositor_nombre = "Ludwig van Beethoven"
compositor_nombre = "Ludwig van Beethoven - Fidelio"
print(compositor_nombre)








