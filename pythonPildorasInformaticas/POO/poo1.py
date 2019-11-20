class Coche():
	#atributos de la clase coche
	largoChasis=250 #cm
	anchoChasis=120
	ruedas=4
	enMarcha=False

	#metodos de la clase coche, son funciones propias de ésta clase	
	#funcion seteadora del atributo enMarcha:
	def arrancar(self): #self equivale al this, indica objeto perteneciente a la clase 
		 self.enMarcha=True #con self indicamos que setearemos el atributo enMarcha

	#funcion mostradora, con retorno:
	def estado(self):
		if self.enMarcha:
			return "en marcha"
		else:
			return "detenido"

miCoche=Coche() #instanciamos la clase, creamos un objeto
print("Largo del coche: ",miCoche.largoChasis) #mostramos un atributo de la clase
print("el coche esta: ",miCoche.estado()) #ejecutamos funcion mostradora
print("*encendiendo*")
miCoche.arrancar() #ejecutamos funcion seteadora
print("el coche está: ",miCoche.estado())
