#yield from: util para simplificar el codigo de los generadores en el caso de usar bucles anidados (for dentro de otro for)
def devuelveCiudades(*nombres): # * significa numero indeterminado de elementos in this case, recibe elem en forma de tupla, osea recibe una tupla
	for item in nombres: #asi seria sin yield from 
		for subItem in item:
			yield subItem 

#con yield from no hay necesidad de otro for anidado para acceder al subelemento
def dos(*nombres):
	for item in nombres:
		#for subItem in item:
		yield from item #retorna desde item sus elementos

retorno=dos("juan","pepe","luis")

for x in retorno:
	print(x,end=" ")
#output:
#j u a n p e p e l u i s 



