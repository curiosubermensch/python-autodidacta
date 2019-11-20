import sys

def divide():
	try:
		x=float(input("ing numero: "))
		y=float(input("ing divisor: "))
		d=x/y
		print("la division es: ",d)
	except ZeroDivisionError:
		print("no se puede dividir por cero")
	except ValueError:
		print("solo puede ingresar numeros")
	finally: #codigo que siempre queremos ejecutar 
		print("codigo importante ejecutado")
		print("aqui podria cerrar un cnx (bd)")

#divide()
def evaluaEdad(edad):
	if edad<0:
		#la sgte excepcion se mostrará al final despues de la pila de error de python
		#visualmente es asqueroso y detiene el flujo de ejecucion
		raise TypeError("Excepcion creada ---> No se puede ing negativos")
	if edad<18:
		print("eres menor de edad")
	elif edad<=25:
		print("eres joven aun")
	elif edad<=30:
		print("ciudadanos aun tenemos patria")
	elif edad<=45:
		print("uy ya estamos en la quema")
	elif edad<=60:
		print("tamos viejos")
	print("linea fundamental")

#evaluaEdad(-6)

def divide2():
	try:
		x=float(input("ing numero: "))
		y=float(input("ing divisor: "))
		d=x/y
		print("la division es: ",d)
	except:
		print("Error inesperado: ",sys.exc_info()[0],": ", sys.exc_info()[1]) 
		#print(sys.exc_info()[0]) para ver el tipo de error
		#detalle/explicacion del error: 
	    #raise
	print("codigo importante ejecutado", end=", ")
	print("[aqui podria cerrar un cnx a bd por ej]")


divide2()
