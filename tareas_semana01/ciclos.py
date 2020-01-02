
print('Tarea range()')

for numero in range(5, 9):
	print(numero)



print('Tarea WORLD!')

texto = 'Hello World!'
posicion = 0
world = texto[6:12]

for letra in world:
	posicion = posicion + 1
	letraMayuscula = letra.upper()
	print(letraMayuscula)


print('Tarea indice_letra_par()')

def indice_letra_par():
	cadena = 'supercalifragilisticoespiralidoso'
	posicion = 0

	for posicionLetra in range(0, len(cadena)):
		if posicion % 2 == 0:
			posicion = posicion + 1
			print(cadena[posicionLetra])
		else:
			posicion = posicion + 1


print(indice_letra_par())
