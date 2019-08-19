
#while es un ciclo indefinido
def whily():

	n=int(input("ing numero positivo:"))
	while n<0:
		print("error de ingreso")
		n=int(input("ing numero positivo:"))
	print("el numero positivo ing es: ",n)


def whilyBreak():
	n=int(input("ing numero positivo:"))
	
	
	if n<0:
		break

	print()