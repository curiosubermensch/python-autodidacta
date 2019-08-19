def infin():
	x=input("ingresa una letra de la A a la D: ")

	if x.lower() in ("a","b","c","d"):
		print("ha ingresado la letra: ",x)
	else:
		print("error de ingreso, gil")

def ifinCorreo():
	correo=input("ingresa correo: ")
	c=0
	for i in correo:
		if i =="@":
			c=c+1
		if i ==".":
			c=c+1
	if c==2:
		print("correo valido")
	elif c>2:
		print("su correo tiene algo de más")
	else:	
		print("correo invalido")



def iftrue():

	verdad=input("sera verda lo que vas a escribir?: ")

	if verdad:
		print("asumo que sí"+"'"+verdad+"'")

iftrue()




