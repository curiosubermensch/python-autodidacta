"""
¡Bienvenido al concurso! Su primer problema a resolver esta noche consiste en imprimir en
pantalla el mensaje :
BIENVENIDO AL CONCURSO DE PROGRAMACION 2013
pero en sentido diagonal, de izquierda a derecha, sin tildes y en mayúsculas. La impresión en diagonal
se logra espaciando las letras con respecto al margen izquierdo de la consola, de forma progresiva,
utilizando cero espacios para la primera letra, un espacio para la segunda, dos para la tercera, y así
sucesivamente para las demás.
Nótese que los espacios de la frase también deben imprimirse, siguiendo el espaciamiento antes
indicado. Por ejemplo, si el carácter en la posición 10 de la frase es un espacio, se imprime luego de
anteponerle 10 espacios a la izquierda (en total, en el renglón se deberán imprimir 11 espacios más el
salto de línea).
La última línea se imprime sin un salto de línea final.

DATOS DE SALIDA:
a) el mensaje indicado anteriormente, en diagonal, de tal forma que en cada renglón exista sólo
una letra del mensaje. Los espacios que separan las palabras de la frase también deben
imprimirse en la consola.

"""

s="BIENVENIDO AL CONCURSO DE PROGRAMACION 2013"
e=" "
for i in range(len(s)):
	print(i*e,s[i])





