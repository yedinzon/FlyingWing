class AnguloBordeAtaque:
    def Calcular(velocidadCrucero):
        anguloMin = 15
        anguloMax = 30
        velocidadMin = 50
        velocidadMax = 150
        anguloAtaque = (anguloMax - anguloMin) * (velocidadCrucero - velocidadMin) / (velocidadMax - velocidadMin) + anguloMin
        return anguloAtaque






