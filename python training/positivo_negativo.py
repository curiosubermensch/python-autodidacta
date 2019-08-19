#Se ingresa por teclado un valor entero, mostrar una leyenda que indique
#  si el número es positivo, negativo o nulo (es decir cero) sin usar op logicos

x=int(input("ingrese un n: "))

if x>0:
    print("el numero es positivo")
else: #sabemos que no es mayor que 0
    if x==0: #
        print("es igual a cero")
    else:
        print("es negativo")
