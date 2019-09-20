"""
Para resolver este problema se solicita generar todos los números pares positivos que se
encuentran entre dos números enteros positivos diferentes dados como entrada por teclado, ambos
números incluidos si corresponde. Para ello, se reciben dos números enteros positivos por teclado y se
imprimen en pantalla los numeros pares, de izquierda a derecha, todos en un mismo renglón. Los
números se deben separar por un único espacio simple y luego del último número impreso sólo debe
mostrarse un salto de línea.
"""

x=int(input("ingrese un numero: "))
y=int(input("ingresa otro numero: "))

#1 validar que el segundo sea mayor que el primero- ok
#que se imprima el rango correctamente cuando se ingresa impar

if y>x:
	if x % 2 != 0: #si el principio del rango es impar lo transformamos altiro en par y empieza la faena 
		x=x+1
	#el siguiente for se limita a imprimir los numeros pares de un rango que parte con un par
	for x in range(x,y+1): 
		if x % 2 == 0:
			print(x,end=" ")
			x=x+2

elif x>y: 
	#aqui se hace lo mismo solo que con distintos extremos del rango 
	if y % 2 != 0: 
		y=y+1
	for y in range(y,x+1):
		if y % 2 == 0:
			print(y,end=" ")
			y=y+2
			

else:
	print("los numeros son iguales!")


