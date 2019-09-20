
def cantLetras(nom):
    c=0
    for i in range(0,len(nom)): 1#
        c=c+1
    print("tu nombre tiene " , c , " letras") #los numeros con string se 
    #concatenan con coma!!!

nom=input("ingresa tu nombre: ")
print("tu nombre empieza con la letra: "+nom[0])
print("*************************************")

cantLetras(nom)

#1. Si queremos conocer la longitud de un string en Python disponemos de
#  una función llamada len que retorna la cantidad de caracteres que contiene:

