#coche, moto, camion:
class Coche():
	def desplazamiento(self):
		print("me desplazo en 4 ruedas")
class Moto():
	def desplazamiento(self):
		print("me desplazo en 2 ruedas")
class Camion():
	def desplazamiento(self):
		print("me desplazo en 6 ruedas")

#esta es una funcion (independiente de una clase) por tanto no requiere "self"
def polmorficaDesplazamientoVehiculo(vehiculo): #se le pasa el objeto vehiculo de la clase que sea
	#aqui se aplica la magia del polimorfismo:
	vehiculo.desplazamiento() #la funcion se encargará de llamar al metodo desplazamiento q corresponda a ese objeto

autito=Coche()
polmorficaDesplazamientoVehiculo(autito) #me desplazo en 4 ruedas
x=Camion()
polmorficaDesplazamientoVehiculo(x) #me desplazo en 6 ruedas, LA FUNCION DETERMINA CUAL ES EL METODO CORRESP.

