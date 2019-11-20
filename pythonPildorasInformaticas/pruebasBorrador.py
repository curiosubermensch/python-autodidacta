
def generador(*tupla):
	for i in tupla:
		for j in i:
			yield j

objGen=generador(["a","e","i"],[2,4,6],[1,3,5])

#reescribir el generador
#sin for anidados y q coincida con 
#el ouput
def generador2(*x):
	for z in x:
		yield from z

obj2=generador2(["a","e","i"],[2,4,6],[1,3,5])

for k in objGen:
	print(k,end=" ")
print() #salto de linea
for l in obj2:
	print(l,end=" ")
#output:
#a e i 2 4 6 1 3 5 #generador 
#a e i 2 4 6 1 3 5 #generador2

