def divide(x,y):
	try:
		return x/y
	except ZeroDivisionError:
		print("no se puede dividir por cero") #en este orden o no funka	
		return "Error"
			
try:
	n=int(input("ingresa un numero: "))
	m=int(input("ingresa divisor: "))
	print(divide(n,m))
except ValueError:
	print("debe ingresar solo numeros") #captura del error
			


#lo que importa es que el codigo de abajo se ejecute aun si hay excepciones
print("100 lineas de codigo extremadamente importantes")
print("...")