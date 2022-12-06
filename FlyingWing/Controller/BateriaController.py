from Data.Componentes import Baterias
from Model.BateriaModel import BateriaModel

class BateriaController(object):
    def GetAll():
        listaBaterias = []
        for elemento in Baterias.baterias:
            listaBaterias.append(BateriaModel(elemento))
        return listaBaterias

    def GetId(id):        
        for elemento in Baterias.baterias:
            if elemento[0] == id:
                return BateriaModel(elemento)
            




