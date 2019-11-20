# class Clase():
# 	def __init__(self,nombre):
# 		self.nombre=nombre
# 		self.a="atributo"
# 	def metodo(self):
# 		print(self.a)
# 		print(self.nombre)
#serializar 2 objetos:
#pasarlos a una lista
# import pickle
# a=Clase("x")
# b=Clase("y")
# lista=[a,b]
# file=open("serialitems","wb") #creamos el archivo binario
# pickle.dump(lista,file) #volcado: dump(<coleccion>,<archivo_binario>)
# file.close()
# del (file)

#deserializar "serialitems"
#contiene una lista de obj
# import pickle
# file=open("serialitems","rb")
# objetos=pickle.load(file)
# file.close()
# #imprimimos los objetos:
# for o in objetos:
# 	print("Objeto: ",o)

class Q():
    __a="hola"

    def __m(self):
        return self.__a
    	

q=Q()
print(q.__m())

