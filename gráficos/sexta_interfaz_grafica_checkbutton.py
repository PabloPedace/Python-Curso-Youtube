#Checkbutton
#Botones de seleccion para preguntas de respuesta multiple

from tkinter import *

root=Tk()

root.title("Ejemplo")

playa=IntVar()
montaña=IntVar()
turismoRural=IntVar()

def opcionesViaje():

    opcionEscogida=""

    if(playa.get()==1):
        opcionEscogida+="playa"

    if(montaña.get()==1):
        opcionEscogida+="montaña"

    if(turismoRural.get()==1):
        opcionEscogida+="turismo rural"   
    
    textoFinal.config(text=opcionEscogida)

foto=PhotoImage(file="Ferrari.png")
Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()

Checkbutton(root, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(root, text="Montaña", variable=montaña, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(root, text="Turismo rural",variable=turismoRural, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()


root.mainloop()





















