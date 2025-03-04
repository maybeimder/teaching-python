""" 
    🍓 [ CLASES RECOMENDADAS ]: 0, 1, 2, 3
"""



# Dada una calificacion del 1-5, convertirlo a la notacion anglosajona
#    4.5 - 5.0: "A"
#    4.0 - 4.5: "B"
#    3.5 - 4.0: "C"
#    3.0 - 3.5: "D"
#    Menos de 3: "F"

calificacion = float(input("Calificacion a conocer: "))
salida : str

if calificacion <= 5 and calificacion >= 4.5:
    salida = "A"
elif calificacion < 4.5 and calificacion >= 4.0:
    salida = "B"
elif calificacion < 4.0 and calificacion >= 3.5:
    salida = "C"
elif calificacion < 3.5 and calificacion >= 3.0:
    salida = "D"
else:
    salida = "F"

print(salida)

