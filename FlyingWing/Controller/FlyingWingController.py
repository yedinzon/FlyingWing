from Controller.Miscelanea.SuperficieControl import SuperficieControl
from Controller.Miscelanea.AnguloBordeAtaque import AnguloBordeAtaque

class FlyingWingController(object):

	def GetModosVuelo():
		return SuperficieControl.modosVuelo

	def GetModoVueloName(char):
		listaModosVuelo = FlyingWingController.GetModosVuelo()
		for elemento in listaModosVuelo:
			if elemento == char:
				return listaModosVuelo[char]

	def getAnguloAtaque(velocidadCrucero):
		return AnguloBordeAtaque.Calcular(velocidadCrucero)				
			
	def Calcular(flyingWing):
		flyingWing.anguloAtaque = FlyingWingController.getAnguloAtaque(flyingWing.velocidadCrucero)
		return flyingWing

	

		
	