from re import A
import turtle

class GeometriaAla(object):

    def __init__(self, canvas, flyingWing):

        relacion_elevon = flyingWing.modoVuelo  
        # Iniciar proceso de graficación de ala
        ala = turtle.RawTurtle(canvas)        
        # Declaración de variable
        areatotal = 100000;
        # Define el área de una ala individual a ser la mitad de areatotal, pues esta se refiere al area total de las dos alas
        area_ala = areatotal / 2
        # ancho del fuselaje
        ancho_fuselaje = 80
        # Aquí se declara c1 y c2 refiriéndose a la cuerda1 y cuerda2 del ala respectivamente
        c1 = 200
        c2 = c1 / 2
        # la cuerda2 utiliza una realación de tamaño de 0.5 respecto a la cuerda1
        # angulo_flecha se refiere a el angúlo con el que se proyecta el ala desde la parte superior del fuselaje
        angulo_flecha = 20

       

        for i in range(2):
            ala.forward(ancho_fuselaje)
            ala.left(90)
            ala.forward(c1)
            ala.left(90)

        # Largo del ala
        largo_ala = (4 * area_ala / 3) / c1

        # Posicionan el cursor en la esquina superior del fuselaje para dibujar ala izquierda
        ala.penup()
        ala.goto(0, c1)
        ala.pendown()
        # Dibujando ala izquierda
        ala.left(180 + angulo_flecha)
        while ala.xcor() > 0 - largo_ala:
            ala.forward(10)
        ala.setheading(270)
        ala.forward(c2)
        angulo_elevon = ala.towards(0, 0)
        ala.goto(0, 0)
        # Posicionan el cursor en la esquina superior del fuselaje para dibujar ala derecha
        ala.penup()
        ala.goto(ancho_fuselaje, c1)
        ala.setheading(0)
        ala.pendown()
        # Dibujando ala derecha
        ala.right(angulo_flecha)
        while ala.xcor() < ancho_fuselaje + largo_ala:
            ala.forward(10)
        ala.setheading(270)
        ala.forward(c2)
        borde_de_salida = ala.distance(ancho_fuselaje, 0)
        ala.goto(ancho_fuselaje, 0)
        # Dibujando elevon derecho
        altura_elevon = (areatotal * relacion_elevon) / borde_de_salida 
        ala.goto(ancho_fuselaje, altura_elevon)
        ala.setheading(360 - angulo_elevon)
        ala.forward(borde_de_salida)
        # Posicionando cursor para ala izquierda
        ala.penup()
        ala.goto(0, altura_elevon)
        ala.pendown()
        # Dibujando elevon izquierdo
        ala.setheading(180 + angulo_elevon)
        ala.forward(borde_de_salida)