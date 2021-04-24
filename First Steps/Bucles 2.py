email=False 
miEmail=input("introduce tu email: ")

for i in miEmail:
	if (i == "@" or i =="."):
		email=True

if email:
	print (miEmail)
else:
	print ("el email es incorrecto")
	print ("hola",end=" ") #El end y las comillas es para dejar tantos espacios como se indican entre las comillas
#si solamente se deja un string, la accion se realiza la cantidad de caracteres que haya en el string
#Si se realiza una lista, entonces la cantidad de elementos en la lista.
#False o True va con la primera letra en mayuscula
#Dos iguales "==" comparan variables, y un igual "="asigna un valor a una variable.
# el tipo -> range(5) crea una lista que comienza en 0 y termina en 4.