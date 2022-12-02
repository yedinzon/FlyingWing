from Controller.Miscelanea.SuperficieControl import SuperficieControl

class FlyingWingController(object):

	def GetModosVuelo():
		return SuperficieControl.modosVuelo

	def GetModoVueloName(char):
		listaModosVuelo = FlyingWingController.GetModosVuelo()
		for elemento in listaModosVuelo:
			if elemento == char:
				return listaModosVuelo[char]
			
	def Calcular(flyingWing):
		print("Funciona")
		
	