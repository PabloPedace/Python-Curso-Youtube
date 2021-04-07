#Expresiones regulares. Metacaracteres (caracteres comodin)
#Anclas y clases de caracteres

import re 

lista_nombres=['http://pildorasinformaticas.es',
                'ftp://pildorasinformaticas.es',
                'http://pildorasinformaticas.com',
                'ftp://pildorasinformaticas.com',
                'http://informaticaespaña.es',
                'hombres',
                'mujeres',
                'mascotas',
                'niños',
                'niñas',
                'camión',
                'camion',
                'Ana Gomes',
                'Maria Martin',
                'Sandra Lopez',
                'Santiago Martin',
                'Sandra Fernandez'
                ]

for elemento in lista_nombres:
    if re.findall('^Sandra', elemento):

        print(elemento)

for elemento in lista_nombres:
    if re.findall('Martin$', elemento):

        print(elemento)

for elemento in lista_nombres:
    if re.findall('es$', elemento):

        print(elemento)

for elemento in lista_nombres:
    if re.findall('^ftp$', elemento):

        print(elemento)

for elemento in lista_nombres:
    if re.findall('[ñ]', elemento):

        print(elemento)

for elemento in lista_nombres:
    if re.findall('niñ[oa]s', elemento):

        print(elemento)

for elemento in lista_nombres:
    if re.findall('cami[óo]n', elemento):

        print(elemento)





























