""" 
    🍓 [ CLASES RECOMENDADAS ]: 0, 1, 2, 3
"""

# Dada el precio de un producto, se aplican descuentos del:
#    20% para compras superiores a 100.000 COP
#    10% para compras superiores a 50.000 COP
#    5% para compras superiores a 20.000 COP

precio = float(input("Precio del producto: "))
descuento : float

if precio >= 100000:
    descuento = 0.20
elif precio >= 50000:
    descuento = 0.10
elif precio >= 20000:
    descuento = 0.05
else:
    descuento = 0

precio_final = precio*(1-descuento)
print(precio_final)

