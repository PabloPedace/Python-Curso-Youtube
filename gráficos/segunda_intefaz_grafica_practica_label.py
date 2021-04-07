#¿Qué son los Label?
#Widgets utilizadospara mostrar texto o imagenes.
#Tienencomo unica finalidad mostrar texto, no se puede 
#interactuar con él (borrar, arrastrar, etc)
#Label: Sintaxis:
#variableLabel = Label(contenedor,opciones)

from tkinter import *

root=Tk() #Creamos raiz que la vamos a llamar root

miFrame=Frame(root, width=500, height=400)

miFrame.pack()

miImagen=PhotoImage(file="Ferrari.png")

Label(miFrame, image=miImagen, text="Hola alumnos de Python", fg="red", font=("Times New Roman", 12)).place(x=100, y=200)

root.mainloop()
































