import random
def matrizTraspuesta2():
	m=[]
	x=int(input("filas: ")) #2
	y=int(input("columnas: ")) #3

	for f in range(x):
		m.append([]) #le agrego una filita	
		for c in range(y):
			aux=random.randint(1,9)
			m[f].append(aux)

	#imprimo la matriz generada
	for a in range(x):
		for b in range(y):
			print(m[a][b], end=" ")
		print()

	#recrear matriz
	t=[]
	for i in range(y):
		t.append([])
		for j in range(x):
			t[i].append(m[j][i]) #invierto ctm y le paso a la fila corresp
	
	print("matriz traspuesta: ")
	for z in range(y):
		for w in range(x):
			print(t[z][w],end=" ")
		print()

		
matrizTraspuesta2()