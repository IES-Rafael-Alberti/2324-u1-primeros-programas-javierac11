#Ejercicio 2.5¶
#Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por
#pantalla el precio final del artículo.

def addIva(precio: float, iva: float):
    total = precio * (iva / 100) + precio
    return total

if __name__ == "__main__":
    price = float(input("Introduce el precio: "))
    iva = float(input("Introduce el iva: "))
    print("El precio con iva es de: " + addIva(price, iva))