#palindromo se lee igual de izquierda a derecha

# Crear un programa que determine si una palabra ingresada por teclado es palíndroma o no. Las
# palabras no llevan tilde. Además, las letras mayúsculas y minúsculas se consideran como diferentes
# carácteres.
# DATOS DE ENTRADA:
# a) una palabra, de largo 1 o mayor, sin espacios. Es posible que el ingreso tenga 0 ó más
# espacios al inicio o al final de la palabra. Dichos espacios no se consideran dentro del análisis.
# DATOS DE SALIDA:
# a) mostrar por consola la salida "ES PALINDROMO", si la palabra ingresada es un palíndromo,
# o "NO ES PALINDROMO", si no lo es. La frase de salida se escribe en sólo mayúsculas y sin
# tildes, y va finalizada por un salto de línea
def palindromo():
	p=input("ingresa una palabra: ")

	x=p.lower()
	palabra=""
	alvere=""
	c=0

	for i in range(len(x)):
		if x[i] != " ":
			palabra=palabra+x[i]
			
	for i in range(len(palabra)): #está ankiable
		if palabra[i] != palabra[(len(palabra)-1)-i]:
			 c=c+1

	if c>=1:
		print("No es palindromo")
	else:
		print("¡Sí es palindroma!") 

palindromo()

#print(x[i]) #uno por uno cada elemento del string

#cuenta regresiva parte del 10:
# for num in range(10,0,-1): (inicio, fin, descuento)
#     print(num)

def canti():
	#PALINDROMO (SE LEE IGUAL DE DERECHA A IZQ QUE NORMAL)
	p=input("ingresa una palabra (sin esp ni acento): ")
	x=p.lower()
	c=0
			
	for i in range(len(x)): 
		#en caso de no haber coincidencia:
		#considerar espacio para el comparador
		if x[i] != x[(len(x)-1)-i]:
			c=c+1
	if c>=1:
		print("No es palindromo")
	else:
		print("¡Sí es palindromo!")  

def canti2():
	l=[]
	for i in range(4):
		p=input("ingrese una palabra fetiche: ")
		l.append(p)

	print(l)
	sufijo="filico"
	for i in l:
		print(l[i]+sufijo)

	# sufijo = "filico"

	# for letra in prefijos:
	#     print letra + sufijo










