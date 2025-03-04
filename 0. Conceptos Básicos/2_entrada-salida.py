""" 
    🍓 [ DEFINICIÓN ]  
    La mayoría de los programas requieren la interacción con el usuario.  
    Para esto, usamos métodos de ENTRADA y SALIDA.
"""

# SALIDA ======================================================================================
print()
# * Metodo clasico de salida, recibe como argumento cualquier tipo de dato, tambien le puedes enviar variables
#   ? Imprime en consola la representacion como cadena de texto de el elemento especificado
#   ? Se pueden especificar otros argumentos como:
#       - end=, permite que, al finalizar de imprimar, se agregue el caracter especificado al final
#       - sep=, en caso tal enviar un conjunto de datos, agregar un caracter para dividir los elementos dentro del conjunto de datos

print("Hola Mundo")
print("Python", "es", "chevere", sep="-") # Imprimira "Python-es-chevere"
print("Hola", end="\n")

#* Si te preguntas por que "\n" se ve de otro color es porque es un caracter especial llamado:
#! Secuencia de escape
#?      \n → Salto de línea (Nueva línea)
#?      \t → Tabulación (Espacio de tabulación)
#?      \\ → Barra invertida \
#?      \' → Comilla simple '
#?      \" → Comilla doble "
#?      \f → Salto de página
#?      \v → Tabulación vertical

# ==============================================================================================



# ENTRADA ======================================================================================

input() 
# * Recoje la siguiente entrada de un usuario en la consola como un String (texto)
#   ? Se puede asignar su resultado a una variable
#   ? Recibe como argumento una cadena (Pregunta al usuario)
#   ? Se puede convertir la entrada de usuario usando int(), float(), etc... 

respuesta = input("Pregunta aleatoria")             # Respuesta sera una cadena de texto
edad_usuario = int(input("Cual es su edad?: "))     # edad_usuario sera un entero

# ==============================================================================================

