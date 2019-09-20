"""
99 botellas de cerveza en la pared,
99 botellas de cerveza.
Una se cayó
y quedaron 98 botellas de cerveza en la pared.
...
...
1 botella de cerveza en la pared,
1 botella de cerveza.
Una se cayó
y no hay más botellas de cerveza en la pared.
No hay botellas de cerveza en la pared,
no hay botellas de cerveza.
Hay que ir a la tienda y comprar más,
99 botellas de cerveza en la pared.
"""
b=33
for i in range(33):
	print(b-i, " botellas de cerveza en la pared,")
	print(b-i, " botellas de cerveza")
	print("una se cayó")
	if b-i>1:
		print("y quedaron ",b-i-1," botellas de cerveza en la pared")
	else:
		print("y no hay más botellas de cerveza en la pared.")
		print("No hay botellas de cerveza en la pared,")
		print("no hay botellas de cerveza.")
		print("Hay que ir a la tienda y comprar más,")
		print("33 botellas de cerveza en la pared.")

