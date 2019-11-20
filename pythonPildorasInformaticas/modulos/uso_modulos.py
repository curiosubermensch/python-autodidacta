#modulos: archivos .py o .pyc (python compilados) que posee su propio espacio de nombres y que puede 
#contener variables, funciones, clases e incluso otros modulos
#son utiles para reutilizar codigo, modularizar

import funciones_matematicas #para usar un modulo o clase hay que importar el archivo contenedor

a=int(input("ing un numero: "))
b=int(input("ing otro numero: "))
funciones_matematicas.sumar(a,b) #para usar las funciones del modulo/archivo se puede usar la nomenclatura del punto, aunque puede ser engorrosa si son muchas funciones...
funciones_matematicas.restar(a,b) #nombre_archivo.nombre_funcion()
funciones_matematicas.multiplicar(a,b)