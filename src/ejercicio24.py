#Ejercicio 2.24¶
#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y 
#muestre por pantalla el número de euros y el número de céntimos del precio introducido.

def separarEurosCent(precio):
    euros = round(precio)
    centimos = round((precio - euros) * 100)
    return euros, centimos

if __name__ == "__main__":
    precio = float(input("Introduce un precio: "))
    print(separarEurosCent(precio))