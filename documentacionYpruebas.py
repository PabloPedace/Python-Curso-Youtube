#Documentacion y pruebas
#Utilizar la documentacion para realizar pruebas
#Modulo doctest

# def areaTriangulo(base, altura):

  #  """
  #  Calcula el area de un triangulo dado

  #  .>>> areaTriangulo(3,6)
   # 'El area del triangulo es: 9.0'

   # .>>> areaTriangulo(4,5)
    #'El area del triangulo es: 10.0' 

    #.>>> areaTriangulo(9,3)
    #'El area del triangulo es: 13.5

    #"""

    #return "El area del triangulo es: " +str((base*altura)/2)

def compruebaMail(mailUsuario):

    """
    La funcion compruebaMail evalua un mail
    recibido en busca de la @. Si tiene una @
    es correcto, si tiene mas de una @ es incorrecto
    si la @ esta en el final es incorrecto

    .>>> compruebaMail('juan@cursos.es')
    True

    .>>> compruebaMail('juancursos.es@')
    False

    .>>> compruebaMail('juancursos.es')
    False

    .>>> compruebaMail('juan@cursos@.es')
    False

    """
    arroba=mailUsuario.count('@')

    if(arroba!=1 or mailUsuario.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')==0):
        return False

    else:
        return True 

import doctest
doctest.testmod()













































