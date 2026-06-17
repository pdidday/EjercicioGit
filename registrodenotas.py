print("Registro de nota")
nombre = input("Ingrese nombre del estudiante: ")
nota = float(input("Ingrese nota final: "))
print("Estudiante:", nombre)
print("Nota final:", nota)

if nota >= 4.0:
    print('Aprobado')
else:
    print('reprobado')