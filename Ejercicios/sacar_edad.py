# DD/MM/AAAA
nacimiento = input("Oe cuando naciste: ")
hoy = input("Que dia es hoy: ")

total = 0
diaNacimiento, mesNacimiento, añoNacimiento = nacimiento.split("/")
diaHoy, mesHoy, añoHoy = hoy.split("/")

total = int(añoHoy) - int(añoNacimiento)

if int(mesHoy) < int(mesNacimiento):
    total = total - 1
elif int(mesNacimiento) == int(mesHoy):
    if not int(diaHoy) < int(diaNacimiento):
        total = total - 1

print(f"Tienes {total} años")


