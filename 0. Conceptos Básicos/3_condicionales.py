""" 
    🍓 [ DEFINICIÓN ]  
    Las expresiones condicionales son usadas para evaluar una condicion especifica
    y dar la respuesta adecuada segun se indique.
"""

# =========================================================================================
# La sintaxis es:

#*  if ( condicion ):
#      print()

# En este caso, se leeria como: Si condicion, entonces imprime algo en consola
#!  Recuerda darle al Tab para definir el bloque de codigo: Python se basa en identacion

# =========================================================================================


#? Ejemplo:

edad = 18
if edad >= 18:
    print("Puede tomar")

# En este caso, se leeria como: 
#* Si la edad es mayor o igual que 18:
#       Entonces "puede tomar"


# =========================================================================================


# Podemos complementar cada if con un else, para que un bloque de codigo se ejecute en caso tal la condicion inicial no se cumpla

#? Ejemplo:
edad = 5
if edad <= 10:
    print("Paga el precio de infante")
else:
    print("Paga el precio de adulto")

# En este caso, se leeria como: 
#* Si la edad es menor o igual que 10:
#       Entonces pagara el precio de infante
#* De lo contrario:
#       Se le cobrara el de adulto


# =========================================================================================


# Se pueden stackear condiciones dentro de otras

#? Ejemplo:
precio_cover = 0.0
genero = "Femenino"
edad = 21

if edad >= 18:
    if genero == "Femenino":
        precio_cover = 10000
    else:
        precio_cover = 30000
else:
    print("No puedes pasar, eres menor")

# En este caso, se leeria como: 
#* Si la edad es mayor o igual que 18:
#       Entonces puede pasar
#?      Si es mujer:
#           Tiene descuento en el cover
#?      De lo contrario:
#           Paga lo mismo
#* De lo contrario:
#       Le llamamos a los papas porque no puede pasar


# Vease que el else se aplica bajo el if de su mismo nivel, azul-azul, verde-verde


# =========================================================================================


# Existe un tercer condicional llamado elif, corresponde a un "sino si"

#? Ejemplo:
color_ojos = "Azul"
altura = 1.85
calificacion = 0

if color_ojos == "Azul" or color_ojos == "Verde":
    calificacion = 10
elif color_ojos == "Avellana":
    calificacion = 9
else:
    calificacion = 7

if altura < 1.75:
    calificacion = calificacion - 3 

# En este caso, se leeria como: 
#* Si tiene ojos azules o verdes:
#       Entonces es un 10
#* Sino, si tiene ojos avellana:
#       Entonces es un 9
#* Sino:
#       Entonces es un 7

#* Si mide menos de 1.75:
#       Le restamos -3 porque uno no sale con pitufos


# =========================================================================================

