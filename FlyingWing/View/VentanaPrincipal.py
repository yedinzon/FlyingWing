import tkinter as tk
from View.Pizarra.Pizarra import Pizarra
from Controller.MotorController import MotorController
from Controller.Miscelanea.SuperficieControl import SuperficieControl

class VentanaPrincipal(object):
    
    ventana = tk.Tk()
    ventana.title('Class')    
    canvas = tk.Canvas(ventana, width=400, height=400)
    canvas.grid(row=0, columnspan=6, pady=20)   
    
    frame=tk.Frame(ventana,width=1000,height=1000)
    canvas.pack()
    frame.pack()

    S = tk.Entry(frame)
    
    S.grid(row=0,column=2,padx=15,pady=15)
    Slabel = tk.Label(frame,text='Superficie Alar')
    Slabel.grid(row=0,column=0,padx=15,pady=15)
    mvenergico = tk.Button(frame,text='Energico',width=10,height=2,command=SuperficieControl.S_Control(800,0))
    mvenergico.grid(row=1,column=1,padx=15,pady=15)
    mvnormal = tk.Button(frame,text='Normal',width=10,height=2,command=lambda:S_Control(float(S.get()),1))
    mvnormal.grid(row=1,column=2,padx=15,pady=15)
    mvsuave = tk.Button(frame,text='Suave',width=10,height=2,command=lambda:S_Control(float(S.get()),2))
    mvsuave.grid(row=1,column=3,padx=15,pady=15)
    mvlabel = tk.Label(frame,text='Modo de Vuelo')
    mvlabel.grid(row=1,column=0,padx=15,pady=15)

    r = tk.DoubleVar()

    resultadolabel = tk.Label(frame,text='La Superficie de Control es:')
    resultadolabel.grid(row=2,column=1,padx=15,pady=15)
    resultado = tk.Entry(frame,textvariable=r,state='disable')
    resultado.config(justify='center')
    resultado.grid(row=2,column=2,padx=15,pady=15)

    menuBar = tk.Menu(ventana)
    ventana.config(menu=menuBar)

    motorMenu = tk.Menu(menuBar, tearoff=0)    
     
    for motor in MotorController.GetAll():
        motorMenu.add_command(label = motor.nombre)
    menuBar.add_cascade(label = "Motor", menu = motorMenu)


    Pizarra(canvas)
    
    




