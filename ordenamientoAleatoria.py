#ordenar de mayor a menor una lista de 4 elementos:

def masMenos():
	"""
	l=[1,2,3,4]
	print(l)
	"""
	import random
	l=[]
	for i in range(4):
		x=random.randint(1,10)
		l.append(x)

	print(l)
	print("----------")
	print("lista ordenada de mayor a menor: ")

	for i in range(3): #tres vueltas porque son 3 comparaciones
		for j in range(3-i): #cada vuelta de i significa que un elemento estará ordenado por tanto 
		#habrá uno mas que no cumple la condicion y no vale la pena compararlo (ver recuadro final)
			if l[j]<l[j+1]:
				aux=l[j] #para poder hacer el cambio necesitamos ayuda de la memoria para que al setear al primero con el valor de al lado no se pierda su info
				l[j]=l[j+1] 
				l[j+1]=aux

	print(l)

masMenos()
"""
i=0:
	j=0: [1,2,3,4]--¿1<2? sí-->[(2,1),3,4]
	j=1: [2,(3,1),4]
	j=2: [2,3,(4,1)]

i=1: #segunda vuelta seran 3-1 = 2 vueltas del for anidado
	j=0: [2,3,4,1] --->[(3,2),4,1]
	j=1: [3,4,2,1]
	j=2: #no cumple se sale del for

i=2 #3ra vuelta seran 3-2=1 sola vuelta del for anidado:
	j=0:[3,4,2,1] ---->[4,3,2,1]
	j=2: #no cumple, fin
"""






