#Documentacion
#Incluir comentarios en clases, metodos, modulos, etc.
#Sirve para ayudar en el trabajo en equipo. Especialmente util en aplicaciones complejas

from modulos import modulos_funciones_matematicas

class Areas:

    """Esta clase calcula las areas de diferentes figuras geometricas"""

    def areaCuadrado(lado):

        """Calcula el area de un cuadrado
    elevando al cuadrado el lado pasado por parametro"""

        return "El area del cuadrado es: " + str(lado*lado)

    def areaTriangulo(base, altura):

        """Calcula el area de un triangulo utilizando los parametros base y altura"""

        return "El area del trianguloo es: " + str((base*altura)/2)

help(Areas)
help(modulos_funciones_matematicas)





























