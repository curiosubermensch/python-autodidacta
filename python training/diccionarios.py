

#c:v mi diccionario es un curriculum vitae! (sarcasmo)
#cuando se cambia el valor de una clave, ese valor sobreescribe al otro
#no pueden haber dos claves iguales

def diccio():
    #declarar diccionario de nombre "d"
    #ciudades: chile, colombia, peru
    #agregar sus respectivas capitales
    d={"chile":"santiago","colombia":"bogota","peru":"lima"}
    print(d)

def dec():
    d={1:"a",2:"b",3:"c"}
    print(d)
    print("se agrega un elemento:")
    d[4]="d"
    print(d)

def pitea():
    d={"a":1, "b":6, "c":12}
    print(d)
    print("eliminamos el valor 6: ")
    del d["b"]
    print(d)

def diccioloco():
    d={1:"a",2:"b",3:{"c":["x","y","z"]}}
    print(d[3])

def dex():
    tupla=(1,2,3)
    diccio={tupla[0]:"x",tupla[1]:"y",tupla[2]:"z"}
    print(diccio)

def ddd():

    diccionario={"a":1,"b":2,"c":3}
    #imprimir el valor de la clave b:
    print(diccionario["b"]) #salida: 2

ddd()







