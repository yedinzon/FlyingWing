import tkinter as tk
from View.Pizarra.Pizarra import Pizarra
from Controller.MotorController import MotorController

class VentanaPrincipal(object):
    
    ventana = tk.Tk()
    ventana.title('Class')    
    canvas = tk.Canvas(ventana, width=400, height=400)
    canvas.grid(row=0, columnspan=6, pady=20)    

    menuBar = tk.Menu(ventana)
    ventana.config(menu=menuBar)

    motorMenu = tk.Menu(menuBar, tearoff=0)    
     
    for motor in MotorController.GetAll():
        motorMenu.add_command(label = motor.nombre)
    menuBar.add_cascade(label = "Motor", menu = motorMenu)


    Pizarra(canvas)
    
    




