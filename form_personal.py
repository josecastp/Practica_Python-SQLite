# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
import bdatos as bd

def veure_seleccio(evt):
    value=str(lbox.get(lbox.curselection()))
    mensaje.set(value)
    

    
def esborra_caixes():

    try:
        dni.set("")
        nom.set("")
        cognom1.set("")
        cognom2.set("")
        correu.set("")
        telf.set("")
        codipostal.set("")
        direccion.set("")
        poblacion.set("")
    except ValueError:
        pass   
    
def enviar() :
    try:

        # Creamos una lista con tupla usuarios (dni, nom, cognom1,congom2, correu, telf, codipostal, direccion, poblacion)
        persona = (dni.get(), nom.get(), cognom1.get(), cognom2.get(), correu.get(), telf.get(), codipostal.get(), direccion.get(), poblacion.get())
        bd.crea_personal([persona])
        print ("Enviat ", cognom1.get(), cognom2.get(), correu.get())
        esborra_caixes()
        Label(root ,text = "Enviat").pack()        
    except ValueError:
        pass     

def cancelar() :

    try:
        esborra_caixes()
        root.destroy()
    except ValueError:
        pass   

def donothing_out():
    button = ttk.Button(root, text="Do nothing button")
    button.pack()

def cmdconsultar():
    frame.pack_forget()
    frcons.pack()
    carrega_dades()
    
def carrega_dades() :
    global lbox

    lbox.delete('0','end')
    lista = bd.consulta_personal()

    for item in lista:
        lbox.insert(END,item[1:3])

    
def cmdcrear():
    mensaje.set("")
    frame.pack()
    frcons.pack_forget()


# =============================================================================
# if __name__ == '__main__':
# =============================================================================
root = Tk()
root.geometry('800x500')
 

#------------------------------------------- Zona menu
frmenu = ttk.Frame(root)  
frmenu.pack()


ttk.Button(frmenu ,text="Consulta", command=cmdconsultar).grid(row=0,column=0)
ttk.Button(frmenu ,text="Alta",  command=cmdcrear).grid(row=0,column=1)

#------------------------------------------- Zona consulta

mensaje =StringVar()
frcons = ttk.Frame(root)  
frcons.pack_forget()
Label(frcons ,textvariable=mensaje).grid(row = 0,column = 0)
lbox=Listbox(frcons,width=200, font=('Arial',11))
lbox.grid(row = 1,column = 0,  columnspan=3)
lbox.bind('<<ListboxSelect>>',veure_seleccio)
#------------------------------------------- Zona formulario

frame = ttk.Frame(root)  
frame.pack_forget()      
frame.config(width=250,height=320, relief="sunken") 
    
dni =StringVar()
nom =StringVar()
cognom1 =StringVar()
cognom2 =StringVar()
correu =StringVar()
telf =StringVar()
codipostal =StringVar()
direccion=StringVar()
poblacion=StringVar()

Label(frame ,text = "Dni     ").grid(row = 0,column = 0)
Label(frame ,text = "Nom     ").grid(row = 1,column = 0)
Label(frame ,text = "Cognom 1").grid(row = 2,column = 0)
Label(frame ,text = "Cognom 2").grid(row = 3,column = 0)
Label(frame ,text = "Correu  ").grid(row = 4,column = 0)
Label(frame ,text = "Telèfon ").grid(row = 5,column = 0)
Label(frame ,text = "cPostal ").grid(row = 6,column = 0)
Label(frame ,text = "direccion ").grid(row = 7,column = 0)
Label(frame ,text = "poblacion ").grid(row = 8,column = 0)

Entry(frame, textvariable=dni).grid(row = 0,column = 1)
Entry(frame, textvariable=nom).grid(row = 1,column = 1)
Entry(frame, textvariable=cognom1).grid(row = 2,column = 1)
Entry(frame, textvariable=cognom2).grid(row = 3,column = 1)
Entry(frame, textvariable=correu).grid(row = 4,column = 1)
Entry(frame, textvariable=telf).grid(row = 5,column = 1)
Entry(frame, textvariable=codipostal).grid(row = 6,column = 1)
Entry(frame, textvariable=direccion).grid(row = 7,column = 1)
Entry(frame, textvariable=poblacion).grid(row = 8,column = 1)

ttk.Button(frame ,text="Cancelar", command=cancelar).grid(row=9,column=0)
ttk.Button(frame ,text="Enviar", command=enviar).grid(row=9,column=1)

root.mainloop()