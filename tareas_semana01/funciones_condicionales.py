import random 

print('Tarea cuadrado o rectangulo')

def tipo_de_valor(num1, num2):
	if num1 == num2:
	    return 'Es un cuadrado'
	else: 
	    return 'Es un rectangulo'     

incrementador = 0
for numero in range(1, 11):
	incrementador = incrementador + 1
	numeroRandom = random.randint(0, 10) 

	print(tipo_de_valor(incrementador, numeroRandom))


