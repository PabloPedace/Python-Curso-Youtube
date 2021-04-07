#Intefaz gráfica (GUI)
#Son ventanas con las qu nosotros como usuarios interactuamos con los programas
#Son intermediarios entre el programa y el usuario.
#Formadas por un conjunto de gráficos como ventanas, botones, menus, casillas de verificacion, etc.
#Librerias con las que trabajar para crear GUI:
#Tkinter, WxPython, PyQT, PyGTK
#Tkinter es un "puente" entre Python y la librería TCL/TK
#
#Estructura de vetana con Tkinter:
#
#Primero hay que contruir la Raiz(ventana).
#Adentro de la ventana, es habitual que se construya un Frame como aglutinador de elementos
#Adentro del Frame hay Widgets(botones, menus, desplegables, etc)

from tkinter import *

raiz=Tk()

raiz.title("Ventana de pruebas")

#raiz.resizable(0,0) #Agranda la pantalla. El primero es el ancho(width) y el segundo el alto(heigth)
#raiz.resizable(True,False) #Agranda la pantalla. El primero es el ancho(width) y el segundo el alto(heigth)

#Cambiar icono de la pluma con la extension.ico, ir a google: conversor .ico
#raiz.iconbitmap("sasasa.ico")

#raiz.geometry("650x350") #El tamaño que le damos a la raiz

raiz.config(bg="blue")

raiz.config(bd=45)

raiz.config(relief="groove")

raiz.config(cursor="hand2")

miFrame=Frame() #Construccion del Frame

miFrame.pack() #Empaquetado side="left", anchor="n" ; fill="both", expand="True"

miFrame.config(bg="red")

miFrame.config(width="650", height="350")

miFrame.config(bd=35)

miFrame.config(relief="sunken") #groove

miFrame.config(cursor="pirate") #hand2

raiz.mainloop() #El mainloop siempre tiene que estar al final















































