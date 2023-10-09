#Ejercicio 2.6¶
#Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado y
#el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%).

def calcIva(precio):
    iva = precio * 0.10
    price_sin_iva = precio - iva
    mensaje = "El precio sin iva es: " + str(price_sin_iva) + "\nEl iva es: " + str(iva)
    return mensaje

if __name__ == "__main__":
    price = float(input("Introduce el precio: "))
    print(calcIva(price))