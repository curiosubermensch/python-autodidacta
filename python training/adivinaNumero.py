"""
 “Adivina el Número”. La computadora pensará un número
aleatorio entre 1 y 20, y te pedirá que intentes adivinarlo. La computadora te dirá si cada intento
es muy alto o muy bajo. Tú ganas si adivinas el número en seis intentos o menos
"""

import random #importamos esta cuestion pa poder usar el metodo

intentosRealizados = 0 
resultado = 0

nombre = input("hola, dime tu nombre: ")
print(nombre," el numero esta entre 1 y 20, adivinalo")
numero=random.randint(1,20)

while intentosRealizados < 6:
    x=int(input(nombre+" ingresa el numero que crees que es: "))

    if x != numero:
        intentosRealizados=intentosRealizados+1
        print("equivocado, te quedan ",6-intentosRealizados," intentos")
        
    if x == numero:
        intentosRealizados=intentosRealizados+1
        resultado=1
        break  

if resultado == 1:
    print("Exacto era el ",numero, " diste con él al ",intentosRealizados," intento, felicidades") 
else:
    print("game over, el numero era ",numero)

