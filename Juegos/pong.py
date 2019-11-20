import turtle  

wn=turtle.Screen() #obj ventana
wn.title("Pong 2019")
wn.bgcolor("black") 
wn.setup(width=800, height=600) #ancho de la ventana
wn.tracer(0)

#jugador 1 (paleta 1):
jugador1=turtle.Turtle()
jugador1.speed(0) #que se vea de inmediato el jugador
jugador1.shape("square") #forma de la pelota
jugador1.color("white")
jugador1.penup() #para q no aparezca la linea por defecto q queda al mover el objeto
jugador1.goto(-350,0) #al final de la ventana lo ubicamos
jugador1.shapesize(stretch_wid=5,stretch_len=1) #ancho y alto de la paleta

#jugador 2 (paleta 2):
jugador2=turtle.Turtle()
jugador2.speed(0) 
jugador2.shape("square") 
jugador2.color("blue")
jugador2.penup() 
jugador2.goto(350,0)
jugador2.shapesize(stretch_wid=5,stretch_len=1) 

#pelota: tiene 20 pixeles
pelota=turtle.Turtle()
pelota.speed(0) 
pelota.shape("circle") 
pelota.color("orange")
pelota.penup() 
pelota.goto(0,0)
pelota.shapesize(5) #agrandamiento de pelota 
#la pelota se movera cada 1 pixel hace el lado y hacia arriba:
pelota.dx=1 
pelota.dy=1 

#linea divisoria:
division=turtle.Turtle()
division.color("white")
division.goto(0,400) #la linea va en el eje y, esta es la que va hacia arriba
division.goto(0,-400)

#tablero:
tb=turtle.Turtle()
tb.speed(0)
tb.color("red")
tb.penup()
tb.hideturtle()
tb.goto(0,260)
tb.write("Player A: 0       Player B: 0",align="center",font=("Courier",24,"normal"))

#contadores:
contador1=0
contador2=0

#FUNCIONES:
def p1up():
	y=jugador1.ycor()
	y += 20
	jugador1.sety(y)

def p1down():
	y=jugador1.ycor()
	y -= 20
	jugador1.sety(y)

def p2up():
	y=jugador2.ycor()
	y += 20
	jugador2.sety(y)

def p2down():
	y=jugador2.ycor()
	y -= 20
	jugador2.sety(y)

#dejar el teclado en escucha:
wn.listen()
wn.onkeypress(p1up,"w") #([funcion/accion_sin_parentesis], <tecla_asociada>)
wn.onkeypress(p1down,"s")
wn.onkeypress(p2up,"Up") 
wn.onkeypress(p2down,"Down")
#motor del juego, ejecucion:
while True:
	wn.update()
	pelota.setx(pelota.xcor()+pelota.dx) #aumentamos los 4 px
	pelota.sety(pelota.ycor()+pelota.dy)

	#bordes verticales
	#600-20=580/2=290--->tope del borde con la pelota (de 20px)
	#(0,-290)(0,290)
	if pelota.ycor()>290: #cuando la pelota llegue al borde en el eje y:
		pelota.dy *= -1 #multiplicamos por -1, osea invertimos el valor que traiga de positivo a negativo
	if pelota.ycor()<-290: 
		pelota.dy *= -1	

	#bordes horizontales:
	#800-20=780/2=390------->(-390,0),(+390,0)
	if pelota.xcor()>390:
		pelota.goto(0,0) #retornarla al centro
		pelota.dx *=-1 #revertimos la posicion multiplicando por -1
		contador1+=1 #si se sale fuera del eje x es punto para el contrario
		tb.clear()
		tb.write("Player A: {}       Player B: {}".format(contador1,contador2),align="center",font=("Courier",24,"normal"))
	if pelota.xcor()<-390:
		pelota.goto(0,0)
		pelota.dx *=-1
		contador2+=1
		tb.clear() #limpiar el marcador
		tb.write("Player A: {}       Player B: {}".format(contador1,contador2),align="center",font=("Courier",24,"normal"))
	#colision paleta2:
	if((pelota.xcor()>=340 and pelota.xcor()<=350) 
		and (pelota.ycor()<jugador2.ycor()+50
		and pelota.ycor()>jugador2.ycor()-50)):
		pelota.dx *= -1
	#colision paleta2:
	if((pelota.xcor()<=-340 and pelota.xcor()>=-350) 
		and (pelota.ycor()<jugador1.ycor()+50
		and pelota.ycor()>jugador1.ycor()-50)):
		pelota.dx *= -1

