#Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos}

x=int(input("ingresa un numero: "))
y=int(input("ingresa un numero: "))
z=int(input("ingresa un numero: "))

if x>y and x>z:
    print("el mayor es: ",x)
else: #sabemos a ciencia cierta que "x" no es el mayor
    if y>z:
        print("el mayor es: ",y)
    else: #sabemos a ciencia cierta que z no es menor que y
        print("el mayor es: ",z)

    