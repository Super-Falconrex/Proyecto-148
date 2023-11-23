# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 20:26:33 2023

@author: anyta
"""

from tkinter import*
import random

root = Tk()
root.geometry("500x500")
root.title("Picnic")

label1 = Label(root)
label2 = Label(root)

picnic = ["sandwich", "agua", "manzanas", "pastel", "jugo", "hamburguesa", "pizza", "fresas"]
label1["text"] = str(picnic)

def gran_picnic():
    lista = random.randint(0,7)
    elemento_olvidado = picnic[lista]
    label2["text"] = "Chicos, no se olviden de llevar..." + str(elemento_olvidado)

btn= Button(root, text= "Que se me olvida?", command= gran_picnic)

btn.place(relx= 0.5, rely= 0.5, anchor= CENTER)
label1.place(relx= 0.5, rely= 0.4, anchor= CENTER)
label2.place(relx= 0.5, rely= 0.6, anchor= CENTER)

root.mainloop()