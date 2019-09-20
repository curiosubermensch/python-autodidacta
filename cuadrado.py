# "Cuadrado con asteriscos"
# Crear un programa que imprima en consola el borde de un cuadrado, dibujando sus lados con
# asteriscos. El ancho del cuadrado es ingresado por teclado como un único número entero, finalizado
# con un salto de línea.
# Recuerde que el ancho y el alto del cuadrado tienen la misma cantidad de caracteres.
# DATOS DE ENTRADA:
# a) el número de columnas que tiene el cuadrado a dibujar.
# DATOS DE SALIDA:
# a) el cuadrado dibujado sólo con asteriscos, sin espacios entre ellos. Cada fila de asteríscos se
# dibuja en un renglón de la consola, finalizándolos con un salto de línea, cada uno de ellos.

l=int(input("ingrese ancho del cuadrado: "))

#imprimir techo
#imprimir columna 1 (posicion final+ espacio+)
#imprimir columna 2 (posicion inicial)
#imprimir piso


print("*"*l)
for i in range(l-2):
	print("*"+" "*(l-2)+"*")
print("*"*l)

