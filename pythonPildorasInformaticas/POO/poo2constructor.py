class Coche():
	#atributos de la clase coche
	
	#CONSTRUCTOR: metodo especial q le da estado inicial a los objetos de la clase:
	def __init__(self): #siempre tiene el mismo nombre "init"
		self.__largoChasis=250 #cm
		self.__anchoChasis=120
		self.__ruedas=4 #dos guiones bajo precedidos a un atributo lo hacen privado, no accesible
		self.__enMarcha=False	

	#metodos de la clase coche, son funciones propias de ésta clase	
	def arrancar(self, estado): #le pasamos un PARAMETRO a la funcion, no hay necesidad de especificar tipo
		self.__enMarcha=estado #con self indicamos que setearemos el atributo enMarcha
		if self.__enMarcha: #si es true
			chequeo = self.__chequeoInterno()
		if self.__enMarcha and chequeo: #si los dos son true
			return "en marcha"
		elif self.__enMarcha and chequeo==False:
			return "algo anduvo mal, no podimos arrancar"
		else:
			return "detenido"
	
	def atributos(self):
		print("el coche mide ",self.__largoChasis,", su ancho es ",self.__anchoChasis,", tiene ",self.__ruedas,"ruedas")

	#metodo que chequea antes de arrancar y solo antes si todo esta ok para ponerse en marcha
	def __chequeoInterno(self): #esta ENCAPSULADO, no se puede acceder desde afuera de la clase Coche
		print("realizando chequeo interno")
		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="cerradas"

		if self.gasolina == "ok" and self.aceite == "ok" and self.puertas=="cerradas":
			return True
		else:
			return False

#el codigo sgte esta FUERA de la clase:
miCoche=Coche() #instanciamos la clase, creamos un objeto
miCoche.atributos()
print("el coche esta: ",miCoche.arrancar(True)) #ejecutamos funcion mostradora
print("-----------otro coche----------")
miCoche2=Coche()
miCoche2.__ruedas=50 #intentamos setear fuera de la clase un atributo privado, como esta encapsulado no se cambia
miCoche2.atributos()
print("el coche esta: ",miCoche.arrancar(False)) 
#no tiene sentido hacer chequeo si el coche esta apagado, por eso existe la encapsulacion de metodos---v
#print("vamos a chequear de manera directa por molestar: ",miCoche2.__chequeoInterno()) #Error: 'Coche' object has no attribute '__chequeoInterno'



