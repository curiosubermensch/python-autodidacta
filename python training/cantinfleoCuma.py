#Solicitar la carga del nombre de una persona en minúsculas. 
# Mostrar un mensaje si comienza con vocal dicho nombre.

def vocal():
    n=input("ingresa tu nombre: ")

    if n[0]=="a" or n[0]=="e" or n[0]=="i" or n[0]=="o" or n[0]=="u":
        print("tu nombre comienza por una vocal")


def dos():
    a="zapatos"
    print(len(a))

#Ingresar un mail por teclado. 
# Verificar si el string ingresado contiene solo un caracter "@".

def mail():
    c=0
    m=input("ingresa un mail: ")
    for i in range(0,len(m)):
        if(m[i]=="@"):
            c=c+1
    if c>1:
        print("error, tiene mas de un @ su cagá de mail")
    else:
        if c==0:
            print("no le pusiste arroba tonto weon")
        else:
            print("muy bien, su email es correcto")

def metodosString():
    n=input("ingresa un nombre a la loca: ")
    op=int(input("1. transformar a mayusculas; 2. transformar a minusculas; 3.may solo la primera "))
    if op==1:
        print(n.upper())
    if op==2:
        print(n.lower())
    if op==3:
        print(n.capitalize())
    

#Inicializar un string con la cadena "mAriA" luego llamar a sus métodos
#  upper(), lower() y capitalize(),
#  guardar los datos retornados en otros string y mostrarlos por pantalla.
def metodosString2():
    s="mAriA"
    
    u=s.upper()
    l=s.lower()
    c=s.capitalize()
    print(u,l,c)

#uso de random



def randoms():
    #generar 20 enteros aleatorios 
    #e imprimirlos:
    for i in range(0,20):
        print(random.randint(1,20),end=" ")



def choisep():
    import random
    l=["a","b","c","d","e","f","g","h"]
    print(l)
    print("el premiado es: ")
    print(random.choice(l))

choisep()






















