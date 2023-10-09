#Ejercicio 2.8¶
#Escribir el programa del ejercicio 1.7 usando solamente dos variables diferentes.

def calc3Numbers2():
    num1 = int(input("Introduce un numero: "))
    num2 = int(input("Introduce otro numero: "))
    suma = num1+num2
    num2 = int(input("Introduce otro numero: "))
    suma += num2
    mensaje = "El resultado es: " + str(suma)

    return mensaje

print(calc3Numbers2())