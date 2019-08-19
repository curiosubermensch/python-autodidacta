"""
fibonacci clasico, la idea era hacerlo como el de lgnd
"""

n=int(input("ctos numeros queris que imprima de la Fibonacci"))
f=[0,1]
sum=0
while True:
	
	#sumatorio:
	for i in range(len(f)):
		x=f[(len(f))-2]+f[len(f)-1]
	 	#0+1,0+1+1,0+1+1+2,
	f.append(x)
	if len(f)>20:
		break

print(f,end=" ")
	
#generar el fibonacci




# for(2):
# 	i=0
# 		sum=0
# 	i=1
# 		sum=0+1
# se agrega un 1
# for(3):
# 	i=0
# 		sum=0
# 	i=1
# 		sum=0+1
# 	i=2
# 		sum=0+1+1


"""
este algoritmo no es fibonacci pero esta bien,osea pensaba que fibonacci era como este algoritmo pero es distinto
f=[0,1]
sum=0
while True:
	
	#sumatorio:
	for i in range(len(f)):
		sum=sum+f[i]
	 	#0+1,0+1+1,0+1+1+2,
	f.append(sum)
	if len(f)>20:
		break

print(f,end=" ")
"""












