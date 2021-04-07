#Expresiones regulares
#Match y search

import re

nombre1="Sandra Lopez"

nombre2="Antonio Lopez"

nombre3="Maria Lopez"

nombre4="sandra Lopez"

cadena1="Jara Lopez"

cadena2="5485126235"

cadena2="a548751236"

codigo1="sjdusdusdnsdnsdndnsa71jdusdusadushdus"

codigo2="gygyygyg71dansdsnad jdsjdjs jsids"

codigo3="fjdujsu iiej jfuejfu jdi u idsiaa dda"

if re.match("Sandra", nombre3):

    print("Hemos encontrado el nombre")

else:

    print("No lo hemos encontrado")

if re.match("Sandra", nombre2):

    print("Hemos encontrado el nombre")

else:

    print("No lo hemos encontrado")


if re.match("Sandra", nombre4, re.IGNORECASE):

    print("Hemos encontrado el nombre")

else:

    print("No lo hemos encontrado")

if re.match(".nio", nombre2, re.IGNORECASE):

    print("Hemos encontrado el nombre")

else:

    print("No lo hemos encontrado")

if re.match("\d", cadena1):

    print("Hemos encontrado el numero")

else:

    print("No lo hemos encontrado")

if re.match("\d", cadena2):

    print("Hemos encontrado el numero")

else:

    print("No lo hemos encontrado")

if re.search("Lopez", nombre2):

    print("Hemos encontrado el numero")

else:

    print("No lo hemos encontrado")

if re.search("71", codigo1):

    print("Hemos encontrado el codigo")

else:

    print("No lo hemos encontrado")
























