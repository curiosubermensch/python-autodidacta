import turtle
import time
import random

#configuracion de la ventana:
win=turtle.Screen() #creamos elemento ventana
win.title("Juego Piton")
win.bgcolor("blue")
win.setup(width=600, height=600) #redimensionar ventana
#win.tracer(0) #animaciones mejoradas

#contador comida:
contador=0

#lista q contendra el cuerpo de la piton:
body=[]

#tablero:
tb=turtle.Turtle()
tb.speed(0)
tb.color("green")
tb.penup()
tb.hideturtle()
tb.goto(0,260)
tb.write("Puntuacion = 0",align="center",font=("Courier",24,"normal"))

#cabeza de la piton:
head=turtle.Turtle() #creamos elemento turtle
head.speed(0)
head.shape("square")
head.color("yellow")
head.penup() #para que no deje "rastro" cuando se mueva, osea no dibuja al moverse
head.goto(0,0) #ubicamos en el centro la piton
head.direction="stop"

#comida de la piton:
eat=turtle.Turtle() #creamos elemento turtle
eat.speed(0)
eat.shape("circle")
eat.color("green")
eat.penup()
cx=random.randint(-280,280) #300-20 porque hay que descontar el tamaño de la comida, si se crea en el borde 300 ya no se veria
cy=random.randint(-280,280)
eat.goto(cx,cy) #ubicamos en el centro la piton

# for i in range(0,40):
# 	head.forward(100) #flecha de 100px
# 	head.left(90) #giro hacia la derecha en angulo recto

#funciones controladoras para llamar los movimientos:
def arriba():
	head.direction="up"
def abajo():
	head.direction="down"
def izquierda():
	head.direction="left"
def derecha():
	head.direction="right"
#funciones que haran el movimiento:
def mov():
	if head.direction=="up":
		y=head.ycor() #almacenamos en "y" el valor de la coordenada y
		head.sety(y+20) #aumentamos en 20px la coordenada y, q es lo mismo que suba 20px

	if head.direction=="down":
		y=head.ycor()
		head.sety(y-20)

	if head.direction=="left":
		x=head.xcor()
		head.setx(x-20)

	if head.direction=="right":
		x=head.xcor()
		head.setx(x+20)


#dejamos el teclado en escucha:
win.listen()
win.onkeypress(arriba,"Up")
win.onkeypress(abajo,"Down")
win.onkeypress(izquierda,"Left")
win.onkeypress(derecha,"Right")

while True:
	win.update()

	#colision con los bordes:
	if head.ycor()==280 or head.ycor()==-280 or head.xcor()==280 or head.xcor()==-280:
		time.sleep(0.3)
		head.goto(0,0)
		head.direction="stop"
		#esconder los segmentos, los mandamos bien lejos
		for k in body: #usar un tipo foreach
			k.goto(2000,2000)
		body.clear() #limpiamos la lista (osea los segmentos que conforman el cuerpo)

	if head.distance(eat)<20: #la cabeza y la comida miden 20px, si la distancia entre ellas es menor a 20 es q se han tocado
		contador+=1
		tb.clear() #limpiamos el tablero antes de reescribirlo
		tb.write("Puntuacion = {}",format(contador),align="center",font=("Courier",24,"normal"))
		h=random.randint(-280,280)
		v=random.randint(-280,280)
		eat.goto(h,v)

		#por cada colision comida-piton creamos un nuevo segmento:
		segmento=turtle.Turtle() 
		segmento.speed(0)
		segmento.shape("square")
		segmento.color("yellow")
		segmento.penup()  
		#segmento.direction="stop"
		body.append(segmento)

	totalSeg=len(body)
	#movimiento del cuerpo de la piton:
	for i in range(totalSeg-1, 0, -1): #inicio, fin], decremento
		#tomar las coordenadas del elemento penultimo, para q el ultimo lo pueda seguir:
		ex=body[i-1].xcor()
		ye=body[i-1].ycor()
		body[i].goto(ex,ye)

	#si hay cuerpo (osea si ha comido):
	if totalSeg>0:
		x=head.xcor()
		y=head.ycor()
		body[0].goto(x,y)


	#============intento de colision cabeza-cuerpo===========
	# for k in range(len(body)):
	# 	if head.distance(body[k])<=0:
	# 		body=[]
	# 		head.goto(0,0)
	# 		#head.distance(eat)<20:			

	#================intento de otro metodo para el movimiento del cuerpo==================
	# if totalSeg>0:
	# 	x=head.xcor()
	# 	y=head.ycor()
	# 	body[0].goto(x,y)
	
	# for i in range(1,totalSeg):
	# #tomar coordenadas de la cabeza y darselas al siguiente:
	# 	ecs=body[i-1].xcor()
	# 	lle=body[i-1].ycor()
	# 	body[i].goto(ecs,lle) #al elemento i=1 le damos la direccion de i=0
	mov()
	time.sleep(0.1) #posponer por 0.1 de segundo