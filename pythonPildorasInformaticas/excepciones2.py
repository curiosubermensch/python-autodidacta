def divide(x,y):
	try:
		return x/y
	except ZeroDivisionError:
		print("no se puede dividir por cero") #en este orden o no funka	
		return "Error"

#ciclo infinito para que se ingresen dos valores numericos si o si
while True:			
	try:
		n=int(input("ingresa un numero: "))
		m=int(input("ingresa divisor: "))
		break #si los 2 values son correctos se sale del try 
	except ValueError:
		#si hay error en el cuerpo del try se salta el break y viene directo 
		#al except
		print("Debe ingresar solo numeros, vuelva a ingresar porfa: ") 
			
print(divide(n,m))

#lo que importa es que el codigo de abajo se ejecute aun si hay excepciones
print("100 lineas de codigo extremadamente importantes")
print("...")