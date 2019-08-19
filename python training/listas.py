#las listas son similares a los vectores pero:
#estructura de datos que permite almacenar muchos valores 
#(incluso de distinto tipo ej string junto con int)
#se expanden dinamicamente (agregar mas elementos)
import random


def pruebas():
    lista=["n","r","perro","i","ñafle", "tres","ballena"]
    print(lista[0:3]) #el 3 no lo toma
    print(lista[3:5]) #porcion muestra lista[3] hasta lista[4] el 5 no lo toma
    print(lista[-4])  #con negativos muestra al revez partiendo eso si desde -1
    print(lista[2:]) #imprime desde lista[1] hacia adelante

 #hacer 2, uno con cloze del codigo y otro con resultados


#append, insert, extend

def agregar():
    lista=["q","w", "e", "r"]
    print(lista)
    
    print(lista.index("r")) #con esta linea se obtiene la posicion de r
    
    
    #print(lista)

    #lista.append("x") #agregar elemento al final
    
    #lista.insert(1,"uno") #agregar elemento en una posicion determinada
    
    #lista.extend(["p", "q", "r","z"]) #agregar varios elementos de golpe


#DESDE ACA FALTA ANKIAR
def tanota():
    listax=["hola", "mi", "amor", "zapato", "elva"]
    print(listax)
    
    print("mi" in listax) #print(objeto in nombreLista) 
    #in devuelve un valor booleano (true o false)
    print("----------------------")
    print("mama" in listax)


#La función randint(a, b) genera un número entero entre a y b, ambos incluidos. a debe ser inferior o igual a b.
#para usar randint hay que import la clase random pa aplicarle los metodos
def verif():
    vector=[]
    repetidos=[]
    for i in range(0, 30):
        x=random.randint(0,30)
        vector.append(x)

    print(vector[0:10])
    print(vector[10:20])
    print(vector[20:30])  


    for i in range(0,30):
        for z in range(0,30):
            if vector[i]==vector[z]:
                repetidos.append(vector[i])

    a=int(input("ing el numero que quiere saber si esta repetido entre 1 y 30"))
    
    for i in range(0,len(repetidos)):
        if a==repetidos[i]:
            print("si está repetido compruebalo: ")
        
    print("no esta repetido comprueba")

      




def repete():
    vector=[]

    for i in range(0, 40):
        x=random.randint(0,100)
        vector.append(x)

    a=int(input("ing el numero que quieres saber si está o no"))

    print(a in vector)

    print("--------------------------")
    print(vector[0:10]) 
    print(vector[10:20])
    print(vector[20:30])
    print(vector[30:40])
    
    
def vamos():
    li=["k", 1, 3.14, False, "8"]
    print(li)
    print("se eliminará el 8")
    print("-----------------")
    #eliminamos el ultimo elemento de li:
    li.remove("8") 
    print(li)

vamos()


def piteau():
    li=["k", 1, 3.14, False, "pepe","miau",666]
    print(li)
    print("se ejecuta codigo loco")
    #el sgte metodo elimina el ultimo elem de li,
    #sin pedir nada
    li.pop() 
    print("------------")
    print(li)

def multili():
    
    a=[1,3,5]
    #imprimir 3 veces los elementos de la lista:
    print(a*3) 



def agrega3():
    uno=[1,2,3]
    dos=[4,5,6]
    print(uno)
    print(dos)
    print("------")
    print(uno+dos)













