#crear matriz de 0's 
# si el quiere transformar la diagonal en 1's que se haga

#m=[[0,0,0],[0,0,0],[0,0,0]]
m=[]
x=int(input("ingrese ancho y alto de la matriz:"))


for f in range(x):
	m.append([])
	for c in range(x):
		m[f].append(0)

for fila in range(len(m)):
	for columna in range(x):
		print(m[fila][columna], end=" ")
	print()
	
print("transformacion de la diagonal a 1:")
#m[0][0]=1    #es una obligacion que sea 1 la primera
cambia=0
for i in range(len(m)):
	for j in range(len(m[i])):
		if cambia <= len(m[i])-1:
			m[i][cambia]=1
			cambia=cambia+1
			break


for k in range(len(m)):
	for l in range(len(m[i])):
		print(m[k][l], end=" ")
	print()

"""
output:
000
000
000

100
010
001
"""
