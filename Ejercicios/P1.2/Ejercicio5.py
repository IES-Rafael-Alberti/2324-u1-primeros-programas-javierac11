#Ejercicio 2.5¶
#Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por
#pantalla el precio final del artículo.

def addIva():
    price = float(input("Introduce el precio: "))
    iva = float(input("Introduce el iva: "))

    total = price * (iva / 100) + price
    return "Total: " + str(total)

print(addIva())