import mat

def raiz(n):
	if n<0:
		#creamos nuestra propia excepcion
		raise ValueError("Numero invalido, debe ser positivo")
	else:
		return math.sqrt(n)

o=int(input("ingresa un numero: "))

try:
	print(raiz(o))
except ValueError as e:
	print(e) #imprimimos de manera elegante la excepcion creada

print("programa finalizado")