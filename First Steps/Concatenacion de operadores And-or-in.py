salario_presidente=int(input("introduce salario presidente: "))
print("salario presidente: " + str(salario_presidente))

salario_director=int(input("introduce salario director: "))
print("salario director: " + str(salario_director))

salario_jefe_area=int(input("introduce salario Jefe Area: "))
print("salario jefe area: " + str(salario_jefe_area))

salario_administrativo=int(input("introduce salario salario_administrativo: "))
print("salario administrativo: " + str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
	print("todo correcto")
else:
	print("algo falla en esta empresa")