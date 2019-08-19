"""Confeccionar un programa que permita cargar un número entero positivo de 
hasta tres cifras y muestre un mensaje indicando si tiene 1, 2, o 3 cifras.
 Mostrar un mensaje de error si el número de cifras es mayor """


n=int(input("ingrese un numero entero positivo de hasta 3 cifras: "))

if n>=1000:
     print("ERROR!!!")
else: #sabemos que tiene 3 cifras o menos
    if n>=100: 
        print("el numero tiene 3 cifras")
    else: #sabemos que tiene 2 cifras o menos
        if n>=10:
            print("tiene dos cifras")
        else: #sabemos que tiene una cifra
            print("tiene una cifra")



    