print("verificacion de acceso")

notaestudiante=int(input("Introduce tu nota por favor: "))

if notaestudiante<5:
	print("insuficiente")
elif notaestudiante<6:
	print("suficiente")
elif notaestudiante<7:
	print("bien")
elif notaestudiante<9:
	print("notable")
else:
	print("sobresaliente")	
