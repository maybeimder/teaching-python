""" 
    🍓 [ DEFINICION ]
    Una variable es un espacio en memoria donde se puede almacenar distintos tipos de datos
"""

# =================================================================================================================

'''
    ==== [ VARIABLES BASICAS ] ======================================================================
    Variables que representan solo un valor
    =================================================================================================
'''

# la sintaxis de una variable basica es:
nombre = "valor"

# * Reglas para nombrar variables
#       ! Debe ser unico
#       ! Solo puede usar letras, numeros y guiones bajos
#       ! No puede empezar con un numero

# * El valor puede cambiar en el transcurso del código
edad = 20
edad = 22 # La variable edad ahora es igual a 22 ( anteriormente 20 )

# * Si se desea que una variable NO cambie, poner su nombre es mayuscula
CONSTANTE_PI = 3.141529


# Tipos de variables basicas:
cadena   = "Soy una cadena de caracteres" # Tipo string (str)
entero   = 10                             # Tipo entero (int)
real     = 3.141529                       # Tipo decimal (float)
booleano = True                           # Tipo booleano (bool)

# También podemos especificar el tipo de dato (pero Python lo infiere automáticamente):
cadena   : str
entero   : int
real     : float
booleano : bool

# =================================================================================================================

'''
    ==== [ VARIABLES COMPUESTAS ] ===================================================================
    Variables que pueden almacenar múltiples valores en un solo lugar.
    =================================================================================================
'''

#* Listas (list) → Colección ordenada y modificable.
lista : list = [1, 2, 3, 4, 5]

# ? Acceder a un elemento
lista[0] # Extrae el elemento en la posicion 0   

# ? Modificar un valor
lista[0] = 100 # Establece el elemento en la posicion 0 como 100 

# ? Agregar un elemento
lista.append(6) # Agrega el 6 a la lista


#* Tuplas (tuple) → Colección ordenada, pero INMODIFICABLE.
tupla : tuple = (10, 20, 30)
# tupla[0] = 100  ❌ ERROR: Las tuplas no se pueden modificar.
print(tupla)     # ▶️ (10, 20, 30)

# 🔵 Conjuntos (set) → Colección NO ordenada, SIN elementos duplicados.
conjunto : set = {1, 2, 3, 3, 4, 4}
print(conjunto)  # ▶️ {1, 2, 3, 4} (Python elimina los duplicados)
conjunto.add(5)  # Agregar un nuevo elemento
print(conjunto)  # ▶️ {1, 2, 3, 4, 5}
