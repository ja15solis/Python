print("programa de evaluacion de notas de estudiantes")
nota_alumno=input("Indique la nota: ")
def evaluacion(nota):
	valoracion="aprobado"
	if nota < 5:
		valoracion="suspenso"
	return valoracion

print(evaluacion(int(nota_alumno)))#se debe poner el int porque siempre que el usuario pone algo dentro de un input es un str#
