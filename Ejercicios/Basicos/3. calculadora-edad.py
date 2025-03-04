""" 
    🍓 [ CLASES RECOMENDADAS ]: 0, 1, 2, 3
"""


# Dadas la fecha de nacimiento y la fecha de hoy calcular la edad de una persona

diaHoy = int(input("Que dia es hoy: "))
mesHoy = int(input("De que mes: "))
añoHoy = int(input("En que año: "))

diaNac = int(input("Día de nacimiento: "))
mesNac = int(input("Mes de nacimiento: "))
añoNac = int(input("Año de nacimiento: "))

edad = añoHoy - añoNac

if mesHoy < mesNac:
    edad = edad - 1

elif mesHoy == mesNac:
    if diaHoy < diaNac:
        edad = edad - 1

print(f"Tienes {edad} años")


