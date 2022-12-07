import tkinter as tk
from tkinter import ttk
from Model.FlyingWing import FlyingWing
from Controller.FlyingWingController import FlyingWingController
from Controller.MotorController import MotorController
from Controller.BateriaController import BateriaController
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

tk.Label(frame,text='Modo de Vuelo').place(x=30, y=30)
tk.Label(frame,text='Motor').place(x=30, y=60)
tk.Label(frame,text='Bateria').place(x=30, y=90)
tk.Label(frame,text='Velocidad').place(x=30, y=135)

def setLabelVelocidad(f):    
    var = int(escalaVelocidad.get())
    tk.Label(frame,text=(var, 'km/h')).place(x=140, y=115)

listaModosVuelo = ttk.Combobox(frame, width=10)
listaModosVuelo.place(x=120, y=30)
listaMotores = ttk.Combobox(frame, width=10)
listaMotores.place(x=120, y=60)
listaBaterias = ttk.Combobox(frame, width=10)
listaBaterias.place(x=120, y=90)
escalaVelocidad = ttk.Scale(frame, from_=50, to=150, orient='horizontal', command=setLabelVelocidad)
escalaVelocidad.place(x=120, y=135)

labelModoVuelo = []
for modoVuelo in FlyingWingController.GetModosVuelo():
    labelModoVuelo.append(modoVuelo)
listaModosVuelo['values'] = labelModoVuelo

labelMotores = []
for motor in MotorController.GetAll():
    labelMotores.append(motor.referencia)
listaMotores['values'] = labelMotores

labelBaterias = []
for bateria in BateriaController.GetAll():
    labelBaterias.append(bateria.id)
listaBaterias['values'] = labelBaterias

def ModosVuelo():     
    flyingWing.modoVuelo = FlyingWingController.GetModoVueloName(listaModosVuelo.get())
    tk.Label(frame,text='OK', fg="green").place(x=10, y=30)

def AddMotor():     
    flyingWing.motor = MotorController.GetReferencia(listaMotores.get())
    tk.Label(frame,text='OK', fg="green").place(x=10, y=60)

def AddBateria():     
    flyingWing.bateria = BateriaController.GetId(int(listaBaterias.get()))
    tk.Label(frame,text='OK', fg="green").place(x=10, y=90)

def setVelocidad():
    flyingWing.velocidadCrucero = int(escalaVelocidad.get())
    tk.Label(frame,text='OK', fg="green").place(x=10, y=135)

def CalcularAla():
    flyingWingResult = FlyingWingController.Calcular(flyingWing)
    canvas.delete('all')
    Pizarra(canvas, flyingWingResult)

tk.Button(frame, text="Seleccionar", command=ModosVuelo).place(x=230, y=30)
tk.Button(frame, text="Seleccionar", command=AddMotor).place(x=230, y=60)
tk.Button(frame, text="Seleccionar", command=AddBateria).place(x=230, y=90)
tk.Button(frame, text="Seleccionar", command=setVelocidad).place(x=230, y=135)
tk.Button(frame, text="Calcular", command=CalcularAla).place(x=800, y=30)

ventana.mainloop()
    
    




