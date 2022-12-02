import tkinter as tk
from tkinter import ttk
from Model.FlyingWing import FlyingWing
from Controller.MotorController import MotorController
from Controller.FlyingWingController import FlyingWingController
from Controller.Miscelanea.SuperficieControl import SuperficieControl
from View.Pizarra.Pizarra import Pizarra

global flyingWing
flyingWing = FlyingWing()
 
#Configuraci�n inicial de la ventana principal
ventana = tk.Tk()
ventana.title('Geometria Ala Volante')    
    
#Creaci�n de ventana interior para dibjar el ala
canvas = tk.Canvas(ventana, width=1000, height=400)
canvas.grid(row=0, columnspan=6, pady=20)

#Creaci�n de frame para colocar las listas y botones
frame = tk.Frame(ventana, width=1000, height=200)
    
#Se empaqueta todo en la ventana principal
canvas.pack(fill="both", expand=1)
frame.pack()  

####################### Configuracion de Labels, Combobox y Botones ###############################

tk.Label(frame,text='Motores').place(x=30, y=30)
tk.Label(frame,text='Modo de Vuelo').place(x=30, y=60)

listaMotores = ttk.Combobox(frame, width=10)
listaMotores.place(x=120, y=30)
listaModosVuelo = ttk.Combobox(frame, width=10)
listaModosVuelo.place(x=120, y=60)

labelMotores = []
for motor in MotorController.GetAll():
    labelMotores.append(motor.id)
listaMotores['values'] = labelMotores

labelModoVuelo = []
for modoVuelo in FlyingWingController.GetModosVuelo():
    labelModoVuelo.append(modoVuelo)
listaModosVuelo['values'] = labelModoVuelo

def AddMotor():     
    flyingWing.motor = MotorController.GetId(int(listaMotores.get()))
    tk.Label(frame,text='OK', fg="green").place(x=10, y=30)

def ModosVuelo():     
    flyingWing.modoVuelo = FlyingWingController.GetModoVueloName(listaModosVuelo.get())
    tk.Label(frame,text='OK', fg="green").place(x=10, y=60)

def CalcularAla():
    flyingWingResult = FlyingWingController.Calcular(flyingWing)
    canvas.delete('all')
    Pizarra(canvas, flyingWing)

tk.Button(frame, text="Seleccionar", command=AddMotor).place(x=220, y=30)
tk.Button(frame, text="Seleccionar", command=ModosVuelo).place(x=220, y=60)
tk.Button(frame, text="Calcular", command=CalcularAla).place(x=800, y=30)

ventana.mainloop()
    
    




