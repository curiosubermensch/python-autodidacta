"""
Definir una lista que almacene 5 enteros. 
Sumar todos sus elementos y mostrar dicha suma.
"""
def ejlista1():
    li=[1,5,9,2,3]
    sum=0 #acumulador
    for i in range(0,len(li)):
        sum=sum+li[i] #ANKI
    print(li)
    print("suma elementos lista: ",sum)



#--------------------------------------------------

"""
Definir una lista por asignación que almacene los nombres de los primeros cuatro
meses de año. 
Mostrar el primer y último elemento de la lista solamente.
"""
def ej2():
    mes=["enero","febrero","marzo","abril"]
    print(mes)
    print("primer y ultimo mes de la lista: ",mes[0],mes[3])

def ej3():
    #Definir una lista por asignación que almacene en la primer componente
    #  el nombre de un alumno y en las dos siguientes sus notas.
    #  Imprimir luego el nombre y el promedio de las dos notas.
    inacap=["cristian",7,6]
    print(inacap[0], " promedio: ",(inacap[1]+inacap[2])//2)
    #el operador // se utiliza para dividir dos valores y retornar solo la parte entera.


def ejpro1():
    """
    Definir por asignación una lista con 8 elementos enteros. 
    Contar cuantos de dichos valores almacenan un valor superior a 100
    """
    l=[]
    c=0
    for i in range(0,8):
        x=int(input("ingrese un numero: "))
        l.append(x)

    for i in range(0,8):
        if l[i]>100:
            c=c+1

    print(l)
    print("de los valores ing ",c, " son mayores q 100")        

def ejpro2():
    #Definir una lista por asignación con 5 enteros. 
    # Mostrar por pantalla solo los elementos con valor iguales o superiores a 7.
    # *Si no se quiere que Python añada un salto de línea al final de un print(),
    #  se debe añadir al final el argumento end="":
    l=[]
    for i in range(0,5):
       x=int(input("ing numero: "))
       l.append(x)

    print("valores ing mayores que 7: ")
    for j in range(0,5):
        if l[j]>7:
            print(l[j],end=" ") ## *Si no se quiere que Python añada un
            #salto de línea al final de un print(),
            #se debe añadir al final el argumento end="":

#ANKIAR EL END, CONTADOR, ACUMULADOR, random=================================
#vaciar mazo de flashcards, agregar palabras en ingles de progra a ingles tecnico

def salto():
    print("a",end=" ")
    print("b")



def ejpro3():
    #Definir una lista que almacene por asignación los nombres de 5 personas.
    #  Contar cuantos de esos nombres tienen 5 o más caracteres.
    l=[]
    c=0
    
    for j in range(0,5):
        n=input("ingresa nombre: ")
        l.append(n)
    
    for i in range(0,5):
        if len(l[i])>=5:
            c=c+1

    print("de los nombres ing, ",c," tiene 5 o mas caracteres")

def ej1():
    #Realizar la carga de valores enteros por teclado, almacenarlos en una lista. 
    #Finalizar la carga de enteros al ingresar el cero.
    #  Mostrar finalmente el tamaño de la lista.
    l=[]
    x=True
    c=1
    while x==True:
        print("[",c,"]",end="")
        n=int(input("ingresa numero: "))
        l.append(n)
        if n == 0:
            x=False
        c=c+1
    print("tamaño de la lista: ",len(l))

#agregar el distinto que != a ANKI=============================================



"""
Almacenar en una lista los sueldos (valores float) de 5 operarios. 
Imprimir la lista y el promedio de sueldos.
"""
def prop1():
    l=[]
    c=1
    for i in range(0,5):
        print("[",c,"]",end="")
        s=float(input("ingresa sueldo: "))
        l.append(s)
        c=c+1
    sum=0
    for j in range(0,len(l)):
        sum=sum+l[j]
    
    pro=sum/5
    print(l)
    print("promedio sueldos: ", pro)


        
"""
Cargar por teclado y almacenar en una lista las alturas de 5 personas 
(valores float)
Obtener el promedio de las mismas. Contar cuántas personas son más
 altas que el promedio y cuántas más bajas.
"""
def funy():
    l=[]
    sum=0
    al=0
    b=0
    for i in range(0,5):
        print("[",i+1,"]",end="")
        a=float(input("ing altura: ")) #cuidado con la rep de variables
        l.append(a)
        sum=sum+a
    
    pro=sum/5
    for i in range(0,5):
        if l[i]>pro:
            al=al+1
        elif l[i]<pro: #INVESTIGAR DIFERENCIA CON ELSE Y ANKIAR===============
            b=b+1
    print(l)
    print("promedio: ",pro)
    print("personas mas altas que el promedio: ",al)
    print("personas mas bajas que el promedio: ", b)

"""
Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados 
(4 por la mañana y 4 por la tarde) Confeccionar un programa que permita 
almacenar los sueldos de los empleados agrupados en dos listas.
Imprimir las dos listas de sueldos.
"""
def turnios():
    ma=[]
    ta=[]
    for i in range(0,8):
        print("[",i+1,"]",end="")
        h=input("el trabajador es de la mañana o de la tarde? (m/t)")
        if h=="m": 
            s=float(input("ingresa suerdo: "))
            ma.append(s)
        elif h=="t":
            ss=float(input("ingresa suerdo: "))
            ta.append(ss)
        else:
            print("ingresaste una weá na que ver!")

    print("sueldos mañanaros: ",ma)
    print("sueldos pajeros de la tarde: ",ta)

#termnamos con el ingreso de valores a listas

#---------------------------

def mayor():
    #Crear y cargar una lista con 5 enteros. 
    # Implementar un algoritmo que identifique el mayor valor de la lista.
    l=[]
    for i in range(0,4):
        x=int(input("ing numero: "))
        l.append(x)
    mayor=l[0]
    for i in range(1,4): #el primer elemento l[0] 
        #no tiene sentido compararlo si ya lo elegimos como mayor para empezar
        if l[i]>mayor: #hay que comparar los elementos con el mayor, no entre ellos
            mayor=l[i] 
            #se ira verificando elemento por elemento si uno de ellos es mayor,
            #si lo es se setea el valor "mayor" con el valor de la lista que
            # lo superó (si está al revez l[i]=mayor estás seteando el elemento l[i])
    print(l)
    print("el valor mayor de la lista es", mayor)


def menorydonde():
    #Crear y cargar una lista con 5 enteros por teclado. Implementar un algoritmo
    # que identifique el menor valor de la lista y la posición donde se encuentra.
    l=[]
    for i in range(0,4):
        x=int(input("ing numero: "))
        l.append(x)
    
    menor=l[0]
    p=0
    for i in range(0,4):
        if l[i]<menor:
            menor=l[i]
            p=i
    print(l)
    print("el menor es: ",menor," ubicado en la posicion: ",p)
        

#--------------random y los logicos:
def log():
    a=2
    b=3
    print("numeros: ",a,b)
    if a != b:
        print("son distintos")
    
      

def igu():
    a=7
    b=7
    print("numeros: ",a,b)
    if a == b:
        print("son iguales")

#Ingresar por teclado los nombres de 5 personas y almacenarlos 
# en una lista.
#  Mostrar el nombre de persona menor en orden alfabético.
def menorNom():
    n=[]
    for i in range(0,5):
        p=input("ing nombre: ")
        n.append(p)
    menor=n[0]
    for i in range(0,len(n)):
        if n[i]<menor:
            menor=n[i]
    print(n)
    print("menor elemento alfabeticamente: ",menor)

#Cargar una lista con 5 elementos enteros. Imprimir el mayor y
#  un mensaje si se repite dentro de la lista 
# (es decir si dicho valor se encuentra en 2 o más posiciones en la lista)

def mayol():
    l=[]
    for i in range(0,5):
        x=int(input("ing numero: "))
        l.append(x)
    
    mayor=l[0]
    c=0
    for i in range(1,5):
        if l[i]>mayor:
            mayor=l[i]

    for i in range(0,5):
        if l[i]==mayor:
            c=c+1

    print(l)
    print("el mayor es: ",mayor, end=" ")
    if c>1:
        print(" y se encuentra repetido ",c," veces")

#Desarrollar un programa que permita cargar 5 nombres de personas y sus edades
#  respectivas. Luego de realizar la carga por teclado de todos los datos 
# imprimir los nombres de las personas mayores de edad
#  (mayores o iguales a 18 años)

def listparalela1():
    n=[]
    e=[]
    for i in range(0,5):
        x=input("ing nombre: ")
        n.append(x)
        y=int(input("ing edad: "))
        e.append(y)
    
    print("personas mayores de edad: ")
    for i in range(5):
        if e[i]>=18:
            print(n[i], end=", ")


#Crear y cargar dos listas con los nombres de 5 productos en una y
#  sus respectivos precios en otra. Definir dos listas paralelas. 
# Mostrar cuantos productos tienen un precio mayor al primer producto ingresado.

def ep1lp():

    prec=[]
    prod=[]
    c=0
    for i in range(5):
        x=input("ingresa nombre producto: ")
        y=int(input("ing precio: "))
        prod.append(x)
        prec.append(y)
    
    for i in range(1,5):
        if prec[i]>prec[0]:
            c=c+1

    print(prec)
    print(prod)
    print("==================")
    print(c, " productos son mayores al primer producto")    

#En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben 
# procesar de acuerdo a lo siguiente:
#a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
#b) Realizar un listado que muestre los nombres, notas y condición del alumno. 
# En la condición, colocar "Muy Bueno" si la nota es mayor o igual a 8, 
# "Bueno" si la nota está entre 4 y 7, y colocar "Insuficiente" si la nota es inferior
#  a 4.
#c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”.

def ep2lp():
    a=[]
    n=[]
    c=[]
    co=0
    for i in range(0,5):
        x=input("ing nombre: ")
        a.append(x)
        y=float(input("ing nota: "))
        n.append(y)
        if y>=8:
            c.append("muy bueno")
            co=co+1
        elif y>=4:
            c.append("bueno")
        else:
            c.append("insuficiente")

    for i in range(5):
        print(a[i] ,"-->",n[i],"-->",c[i])
    print("------------")
    print("alumnos con condicion 'muy buena'",co)

#Realizar un programa que pida la carga de dos listas numéricas enteras de 4 
# elementos cada una. Generar una tercer lista que surja de la suma de 
# los elementos de la misma posición de cada lista. Mostrar esta tercer lista.

def ejp3lp():
    l1=[]
    l2=[]
    l3=[]

    for i in range(4):
        x=int(input("ing numero: "))
        y=int(input("ing otro numero: "))
        l1.append(x)
        l2.append(y)
    
    for i in range(4):
        z=l1[i]+l2[3-i]
        l3.append(z)
    
    print(l1)
    print(l2)
    print("-----suma cruzada------")
    print(l3)








































































































































