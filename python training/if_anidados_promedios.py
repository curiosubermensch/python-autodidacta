""" Confeccionar un programa que pida por teclado tres notas de un alumno, calcule el promedio e imprima alguno 
de estos mensajes:
Si el promedio es >=7 mostrar "Promocionado".
Si el promedio es >=4 y <7 mostrar "Regular".
Si el promedio es <4 mostrar "Reprobado"."""


n1=int(input("ingrese nota 1: "))
n2=int(input("ingrese nota 2: "))
n3=int(input("ingrese nota 3: "))

pro=(n1+n2+n3)/3
print("el promedio del wacho es: ")
print(pro)

if pro >= 7:
	print("Promocionado")
else: #pro < 7
	if pro >=4:
		print("reguleque")
	else: # 4<
		print("reproba3 8==========D")


	