"""
"Búsqueda de palabras en varias oraciones"
Se necesita crear una aplicación que busque una palabra dentro una serie de líneas de texto,
(ingresadas desde el teclado) y que imprima en la consola sólo las líneas que contienen la palabra (la
palabra debe concordar de forma exacta, con las mismas mayúsculas y minúsculas y el mismo largo
original dentro de la línea). Por ejemplo, si se ingresa la palabra a buscar:
perro
y a continuación se ingresan las siguientes oraciones:
El perro come su hueso.
Hoy hace mucho calor en la ciudad.
José y su perro caminan por la costanera.
Josefina tiene dos perros de peluche en su habitación.
el programa sólo debe imprimir en consola las oraciones "El perro come su hueso." y "José y su
perro caminan por la costanera.", ya que la segunda oración no tiene la palabra perro y la cuarta
incluye la palabra "perros", pero en plural (es decir, no es la palabra buscada de forma exacta).
Para indicar que no hay más oraciones por examinar, se recibe la palabra "FIN" por teclado,
luego de la última oración.

DATOS DE ENTRADA:
a) una palabra, de largo 1 ó mayor, que será buscada dentro de las frases ingresadas por teclado.
b) una o varias frases, de largo 1 ó mayor, donde será buscada la palabra.
c) la palabra "FIN" para indicar que no hay más frases de entrada y que el programa puede
finalizar.

DATOS DE SALIDA:
a) una lista de cero o más renglones, que incluyan todas las frases ingresadas por teclado y que
contengan la palabra a buscar, de forma exacta. Al final de cada oración mostrada, se debe
imprimir un salto de línea, incluyendo al final de la última oración.
"""
def buscaOracion():
	palabra=input()
	bandera=0
	#contadorDiferencias=0
	b=0
	v=[]
	while True:
		f=input()
		bandera=f.find(palabra)
		b=bandera
		if bandera != -1:   #pa descartar frases en las que no esté la palabra y q el for no de error buscandola
			
			#creo no es necesario este for ya que find determina si está exacto la subcadena lo unico si es
			#que si esta junto a otros caracteres sigue arrojando que sí está y nosotros buscamos una PALABRA
			#no una subcadena. Con el if nos aseguramos que sí sea palabra
			
			# for i in range(len(palabra)):
			# 		if palabra[i] == f[bandera]:										
			# 			bandera=bandera+1
			# 		else:
			# 			contadorDiferencias=contadorDiferencias+1
			# 			bandera=bandera+1
			#contadorDiferencias == 0 and
			#f[-1]==palabra[-1] or esta da error ej gato --> gatosssso como termina en o pasa
			if len(f) == len(palabra) or f[b+len(palabra)]== " " or f[b+len(palabra)]== "." or f[b+len(palabra)]=="," or f[b+len(palabra)]==";": #o no tiene cractter final o tiene una coma despues o
				 v.append(f)
		
		elif f == "FIN":
			break
		
	print("------Frases que contienen la palabra exacta------ ")
	for i in range(len(v)):
		print(v[i])



#esta funcion busca el string y dice si está y en donde pero no si es una palabra separada de las demas
def buscarSubcadena():
	#find("subcadena" [, posicion_inicio, posicion_fin])
	cadena=input("ingresa frase: ")
	palabra=input("ingresa subcadena a buscar: ")
	
	bandera=cadena.find(palabra)
	
	if banderaI != -1:
		print("la subcadena esta en la posicion:",bandera)
	else:
		print("no se encuentra la palabra")
	#print("donde termina la palabra o espacio: ",cadena[banderaI+len(palabra)], banderaI+len(palabra))

# for i in range(len(palabra)):
# 			for j in range(len(f)):
# 				if palabra[i]==f[j]:
# 					c=c+1
# 				if f[j]==" ": #si la letra de la frase es igual a espacio
# 					espacio=j

# 		#if c == len(palabra) and  


# #hare un for que evalue desde la bandera hasta el len(palabra) y verifique que el substring sea igualito
			# for bandera in range(len(palabra)): #for que sirve pa recorrer solo la cantidad de elem de palabra
 		# 		for i in range(len(palabra)): #for que sirve para comparar la primera letra de la frase con todas las letras de la palabra
 		# 			if f[bandera] == palabra[i]:  
			# 			#cumple una condicion				
			# 		#if f[bandera]:
			# 			#cumple la condicion 2
			# #if #cumple todas las condiciones:
			# 	#v.append(f)






# if f[len(f)-1]==palabra[len(palabra)-1]: #la ultima palabra de la frase es igual a la ultima de la palabra:
# 			for i in range(len(palabra)):
# 				if palabra[i] == f[bandera]:										
# 					bandera=bandera+1
# 				else:
# 					contadorDiferencias=contadorDiferencias+1
# 					bandera=bandera+1

# 			if contadorDiferencias == 0:
# 				v.append(f)

# 		elif f[bandera+len(palabra)]== " " or f[bandera+len(palabra)]== "." or f[bandera+len(palabra)]==",":			
			
# 			for i in range(len(palabra)):
# 				if palabra[i] == f[bandera]:										
# 					bandera=bandera+1
# 				else:
# 					contadorDiferencias=contadorDiferencias+1
# 					bandera=bandera+1

# 			if contadorDiferencias == 0:
# 				#v.append(f)

#solucion pura sin comentarios
def buscaOracion2():
	palabra=input()
	bandera=0
	v=[]
	while True:
		f=input()
		bandera=f.find(palabra)
		if bandera != -1:   #pa descartar frases en las que no esté la palabra y q el for no de error buscandola
			
			if len(f) == len(palabra) or f[bandera+len(palabra)]== " " or f[bandera+len(palabra)]== "." or f[bandera+len(palabra)]=="," or f[bandera+len(palabra)]==";":
				 v.append(f)
		
		elif f == "FIN":
			break
		
	print("------Frases que contienen la palabra exacta------ ")
	for i in range(len(v)):
		print(v[i])

buscaOracion2()