
#las tuplas no se pueden modificar luego de creadas
#si extraes una porcion se transforma en otra tupla
#no se puede hacer busquedas en ellas
#si permite verificar si hay un elemento en ella
#se pueden transformar a lista
#son mas eficientes computacionalmente

def tupl():
    tuplaA=("hola", 2, 3, "chao")
    print(tuplaA)
    
    print("transformacion de la tupla a lista: ")
    listaA=list(tuplaA)
    print(listaA)
    print("------fin metodo-----")



def listaa():
    listaB=[7,False,"perro"]
    print(listaB)
    #crear una tupla de nombre "tuplaB" y...
    print("transformacion de la lista en tupla")
    tuplaB=tuple(listaB)
    print(tuplaB)

#tupl()
#listaa()

#falta ankiar desde aqui!!!!!!!!!!!!!!
def cont():
    tup=(1,2,1,2,3,1,1)
    print(tup)
    print("el '1' se repite: ")
    print(tup.count(1), " veces") 
    #linea 5: 
    #cuantas veces está un elemento en la tupla



def empaquet():
    tup="a","z",2 #declarar tupla sin parentesis se llama empaquetado de tupla
    print(tup)



def desempaquetar():
    tu="ana",24,10,1994
    print(tu)
    #desempaquetar tupla:
    #y que coincida con la salida:
    nombre,dia,mes,anio=tu
    print(nombre, anio, mes, dia) 



def declara():
    tupla=("a","b","c")
    print(tupla)


 















