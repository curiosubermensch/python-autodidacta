#crear clase "Clase"
# class Clase():
# 	#crear atributo de name "atributo"
# 	atributo=False
# 	#crear metodo "metodo"
# 	#debe cambiar a True el valor
# 	#del atributo
# 	def metodo(self):
# 		self.atributo=True
# o=Clase() #crear objeto "o" 
# o.metodo() #aplicar metodo
# #mostrar el valor seteado
# print("Atributo: ",o.atributo)
# #output: Atributo:  True

# class C():
# 	a=False
# 	#crear metodo "get" q indique
# 	#textualmente si el valor de "a"
# 	#es "f" o "v"
# 	def get(self):
# 		if self.a: #sintaxis corta 
# 			return "v"
# 		else:
# 			return "f"
# o=C()
# print(o.get())
# #output: f

# class r():
# 	a="publico"
# 	#crear el mismo atributo
# 	#pero privado
# 	__a="privado"
 
# 	#metodo para accesar la variable 
# 	#privada desde afuera
# 	def m(self):
# 		return self.__a

# r=r()
# print(r.a) #print el valor de a
# print(r.m()) #print el valor de a encapsulado
#output:
#publico
#privado
#si se intentara accesar al atributo, imprimirlo
#directo, daria el siguiente error por ser priv: 
#print(r.__a)
#AttributeError: 'r' object has no attribute '__a'


#el sgte metodo es accedible desde afuera? (si/no+xq)
# class Q():
# 	__a="hola"

# 	def __m(self):
# 		return self.__a

# #no xq es privado:
# q=Q()
# print(q.m())
#output:
#AttributeError: 'Q' object has no attribute 'm'


# class C():
# 	#crear constructor
# 	#se le deben pasar 2 param
# 	#"uno" y "dos":
# 	def __init__(self,uno,dos):
# 		self.a=uno
# 		self.b=dos

# c=C("gato","perro")
# print(c.a, c.b)
#output: gato perro

#es metodo o funcion:

#metodos estan metidos en la clase
#funciones son independientes

#¿ES METODO O FUNCION? ¿XQ?
# class C():
# 	def funcion(self):
# 		return "hola mundo"
# c=C()
# print(c.funcion())  
#hola mundo

#funcion porque depende de la clase C()
#esta dentro de ella

#¿ES METODO O FUNCION? ¿XQ?
# def funcion():
# 	return "hola mundo"
# print(funcion())
#output: hola mundo

#funcion porque es independiente

# class q():
# 	def __init__(self,h,e,i):
# 		self.hetero=h
# 		self.estado=e
# 		self.iglu=i

# 	def metodo(self):
# 		print("hola")
# class s(q):
# 	def __init__(self,p,e):
# 		self.peso=p
# 		self.estatura=e
# 	def metodo(self):
# 		print(self.peso)
# 		print(self.estatura)
# class t(s,q):
# 	pass
# #pasarle los mismos values
# #del constructor pero entre " "
# s=s("p","e") 
# s.metodo()

#cuando conviene usar la herencia multiple?
#super: para reutilizacion de metodos y agregarle mas cosas
#isinstance: para saber si un obj pertenece a determinada clase

# class c():
# 	def __init__(self,anio):
# 		self.anio=anio
# 	def metodo(self):
# 		print(self.anio)
# class b(c):
# 	#usar herencia de manera elegante:
# 	#(sin redundancia de codigo)
# 	#agregar la edad al constructor
# 	def __init__(self,anio,edad):
# 		super().__init__(anio) 
# 		self.edad=edad 
# 	#debe imprimir todos los datos del
# 	#constructor mejorado:
# 	def metodo(self):
# 		super().metodo()
# 		print(self.edad)		
# class a(b):
# 	pass
# #pasarle tus datos al constructor
# a=a("1992","27")
# a.metodo()

#output
#1992
#27

#=====================================
#isinstance(obj,clase): Informa si un objeto es instancia de una clase determinada
# class x():
# 	pass
# class y(x):
# 	pass
# class z(y):
# 	pass
# class w():
# 	pass
# class a():
# 	pass
# class r(z):
# 	pass
# class i(w):
# 	pass
# i=i()
# print(isinstance(i,z))
#output: False
##=====================================
#imprimir matriz de 3fx4c
#rellena de 1's
# matriz=[]
# for f in range(3):
# 	matriz.append([])
# 	for c in range(4):
# 		matriz[f].append(1)
# #impresion rapida:
# for i in range(3):
# 	print(matriz[i])
#output:
#[1, 1, 1, 1]
#[1, 1, 1, 1]
#[1, 1, 1, 1]

#======================================
#imprimir matriz de 4fx3c
#rellena de 1's
# matriz=[]
# for f in range(4):
# 	matriz.append([])
# 	for c in range(3):
# 		matriz[f].append(1)
# #impresion rapida:
# for i in range(4):
# 	print(matriz[i])
#output:
# [1, 1, 1]
# [1, 1, 1]
# [1, 1, 1]
# [1, 1, 1]
#========================================

class z():
	def metodo(self):
		print("zeta")
class w():
	def metodo(self):
		print("doble v")
class x():
	def metodo(self):
		print("equis")
#crear funcion polimorfica
#que llame el metodo q corresponda al obj
#debe llamarse "metodoPoli"
def metodoPoli(objeto):
	objeto.metodo()
objw=w()
objx=x()
metodoPoli(objw) #usar el metodo
metodoPoli(objx) #polimorfico
#output:
#doble v
#equis





















