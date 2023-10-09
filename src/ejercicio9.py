#Ejercicio 2.9¶
#¿Es posible escribir el programa del ejercicio 1.7 sin usar variables? Inténtalo.

def calc3Numbers3():
    return int(input("Introduce un numero: ")) + int(input("Introduce un numero: ")) + int(input("Introduce un numero: "))

if __name__ == "__main__":
    print("La suma de los numeros es de: " + calc3Numbers3())
    
#He tenido que meter input() dentro de la función