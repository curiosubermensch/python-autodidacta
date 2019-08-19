
#el else se asocia al if más cercano que tiene arriba (creo)
#no puede haber un else sin su correspondiente if
def elsa():
    #que imprime?
    e=11
    if e<18:
        print("mal")
    elif e>100:
        print("error")
    #este else se ejecuta cuando nada de lo
    #anterior ha funcionado 
    else:
        print("bien")




def elifeo():
    nota=4.9
    if nota>=6:
        print("excelente")
    if nota<5:
        print("bien")
    
    elif nota>=4: 
        print("suficiente")
    
    else:
        print("reprobado")
    #completar para que imprima "excelente"
    

#si fuese if imprimiría "excelente y suficiente porque la nota cumpliria los dos if"


#concatenar operadores de comparacion

def conca():
    #ingresar numero entre ]21,100[
    #concatenar operadores de comparacion:
    e=2
    if 21<e<100:
        print("ingreso correcta")
    else:
        print("ingreso incorrecto")

#string con un int se concatena con ","

def ifconcatenando():
    x=int(input("ing numero: "))
    y=int(input("ing otro numero: "))
    z=int(input("ing un tercer numero: "))
    w=int(input("ing el 4to: "))

    if w<z<y<x:
        print("el primero es mayor")
    else:
        print("mira como te tengo weta")

ifconcatenando()






















