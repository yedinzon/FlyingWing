from Data.Componentes import Motores
from Model.MotorModel import MotorModel

class MotorController(object):
    def GetAll():
        listaMotores = []
        for elemento in Motores.motores:
            listaMotores.append(MotorModel(elemento))
        return listaMotores
            




