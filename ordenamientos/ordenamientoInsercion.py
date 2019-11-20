
#1. partir evaluando POSICION hacia adelante siempre
#2. si a la izquierda el numero es mayor hay que ordenarlo

def miOrdInsercion():
	#este lo hice yo
	lista=[6,4,2,1,3,5]
	print(lista)
	for i in range(1,len(lista)):
		for j in range(len(lista[0:i])):
			if lista[j]>lista[i]:
				aux=lista[i]
				lista[i]=lista[j]
				lista[j]=aux
			print(lista)

def insercionSimple():
	#del video de makigas:
	#es ineficiente
	lista=[6,4,2,1,3,5]
	for i in range(1,len(lista)):
		pos=i #posicion del evaluando
		#el while ira moviendo tantas veces sea necesario el evaluando
		while pos>=1 and lista[pos]<lista[pos-1]: #que sea el segundo elemento (o mas) y si el de la izquierda es mayor que el evaluando entonces hacer el cambiazo
			aux=lista[pos-1] 
			lista[pos-1]=lista[pos] #estos intercambios son los ineficientes
			lista[pos]=aux
			pos=pos-1 #debe moverlo a la posicion anterior por eso se decrementa la posicion del evaluando
			print(lista)

def insercionEficiente():
	pass

#insercionSimple()
def insercion2():
	#el de cesar ramos:
	lista=[6,4,2,1,3,5]
	for i in range(1,len(lista)):
		aux=lista[i] #el elemento actual
		j=i-1#variable q ira decrementando a la izq, comparar el elemento actual con el de la izq
		while j>=0 and aux<lista[j]:
			lista[j+1]=lista[j]
			lista[j]=aux
			j-=1
			print(lista)

#insercion2()

