def ordenMenor():
	#ordenar los elementos de una lista de menor a mayor:
	import random
	#l=[5,4,3,2,1]
	l=[]
	for i in range(5):
		x=random.randint(1,20)
		l.append(x)
	
	print(l)
	print("-----ordenamiento------")

	#si la lista tiene N componentes hay que hacer N-1 comparaciones 
	for j in range(4): #el primer for solo se encarga de repetir el proceso (ya que el otro solo ordena 1 no todos), no se usa "j" mas que para iterar
		##el segundo for se encarga de ir cambiando posicion por posicion UN y solo UN numero que sea mayor 
		#(el caso más extenso es que esté al principio) pa que quede al final (ordenado en ese orden)
		for i in range(4): # 

			if l[i]>l[i+1]: #si el primero es mayor que el segundo
				
				#para poder hacer el cambio necesitamos ayuda de la memoria para que al setear al primero 
				#con el valor de al lado no se pierda su info
				aux=l[i] 
				l[i]=l[i+1] #intercambiamos el primero por el segundo
				l[i+1]=aux #el segundo queda como primero, se han intercambiado en orden de menor a mayor
			


	print(l)


ordenMenor()
"""
j=0:
	i=1: [(5,4),3,2,1],[4,(5,3),2,1],[4,3,(5,2),1],[4,3,2,(5,1)],[4,3,2,1,5] #se ha ordenado 1
	i=2: [(4,3),2,1,5],[3,(4,2),1,5],[3,2,(4,1),5],[3,2,1,4,5],[4 no cumple, fin for]
	i=3: [(3,2),1,4,5],[],[],[]
    i=4:

"""
