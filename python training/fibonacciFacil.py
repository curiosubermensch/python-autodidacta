#fibonacci clasico
#0, 1, 1, 2, 3, 5, 8
n=int(input("ing la cant de numeros de la fibonacci: "))

a=0
b=1
print(a,end=" ")
print(b,end=" ")
for i in range(n-2):
	c=a+b #un auxiliar 
	print(c,end=" ")
	a=b #se hace este cambio en memoria para la proxima suma
	b=c #ya que son los ultimos dos los que se suman y van cambiando
