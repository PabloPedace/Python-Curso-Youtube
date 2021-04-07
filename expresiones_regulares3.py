#Expresiones regulares
#Rangos

import re

lista_nombres=['Ana',
                'Pedro',
                'Maria',
                'Rosa',
                'Sandra',
                'Celia',
                'Ma1',
                'Se1',
                'Ma2',
                'Ba1',
                'Ma3',
                'Va.1',
                'Va:2',
                'Ma4',
                'MaA',
                'Ma5',
                'MaB',
                'MaC']

for elemento in lista_nombres:
    if re.findall('[o-t]', elemento):

        print(elemento)

for elemento in lista_nombres:
    if re.findall('^[O-T]', elemento):

        print(elemento)

for elemento in lista_nombres:
    if re.findall('[o-t]$', elemento):

        print(elemento)

for elemento in lista_nombres:
    if re.findall('Ma[0-3]', elemento):

        print(elemento)

for elemento in lista_nombres:
    if re.findall('Ma^[0-3]', elemento):

        print(elemento)

for elemento in lista_nombres:
    if re.findall('Ma[0-3A-B]', elemento):

        print(elemento)

for elemento in lista_nombres:
    if re.findall('Va[.:]', elemento):

        print(elemento)








