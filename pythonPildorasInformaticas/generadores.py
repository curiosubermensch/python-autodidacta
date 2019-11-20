#en vez de return usa yield, aunque igual puede usarse en conjunto yield y return
#retorna un objeto iterables

#Son funciones que nos permitirán obtener sus resultados poco a poco, gota a gota, uno a uno. Es decir, cada vez que llamemos a la función nos darán un nuevo resultado

#yield. Esta orden devolverá un valor (igual que hace return) pero, además, congelará la ejecución de la función hasta la próxima vez que le pidamos un valor.
def generaPares(limite):
	num=1
	while num<limite:
		yield num*2
		num=num+1

#retornamos objeto iterable:
devuelvePares=generaPares(10)

#la funcion next va digamos recorriendo el obj iterable desde el principio a fin
print(next(devuelvePares))
print("-----linea de codigo x-----")
print(next(devuelvePares)) #entre llamada y llamada se queda en estado de suspension, lo que ahorra recursos
print("-----otra linea de codigo-----")
print(next(devuelvePares))
print(".......300 lineas de codigo......")
print("...")
print("...")
print(next(devuelvePares))

#el generador solo genero 4 valores (2,4,6,8), si hubiese sido una funcion habria generado 10 numeros en una lista y luego #mostrado los 4 que necesitabamos lo que es menos eficiente
