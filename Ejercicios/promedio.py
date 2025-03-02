cantidad = int(input("Cuantas notas hay en el corte: "))

acumulador = 0
for iteracion in range(1, cantidad+1 ):
    nota = float(input(f"Ingrese Nota({iteracion}): "))
    acumulador = acumulador + nota

print( acumulador/cantidad )
