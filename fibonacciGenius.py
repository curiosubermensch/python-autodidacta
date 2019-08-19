"""
Se solicita crear un programa que imprima en la consola N términos pares de la serie de
Fibonacci. La serie Fibonacci es así: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,
2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, etc.
Recuerde que la serie de Fibonacci tiene la siguiente fórmula:
Fib(x)=¿
Recuerde también que el número cero es un número par.
DATOS DE ENTRADA:
a) N es un número entero desde teclado, que indica la cantidad de números pares de la serie
Fibonacci a imprimir.
DATOS DE SALIDA:
a) los términos pares solicitados de la serie de Fibonacci, separados por un espacio entre ellos,
en un único renglón de texto. No debe haber ningún carácter ni salto de línea luego del último
término a mostrar.
"""

n=int(input("ing la cant de numeros pares de la fibonacci: "))

a=0
b=1
x=0
for i in range(True):
	if a % 2 == 0:
		print(a) #0 #1 #1
	 	x=x+1
	if x>=n:
		break
	else:
		c=a+b #1 #2
		a=b #(0),1 = (1),1 # (1),1 # 
		b=c #1,(1) = 1,(1) # 1,(2)  