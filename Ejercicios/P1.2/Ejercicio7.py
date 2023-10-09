#Ejercicio 2.7¶
#Escribe un programa que solicite tres números al usuario y calcule e imprima por pantalla su suma.

def calc3Numbers():
    num1 = int(input("Introduce un numero: "))
    num2 = int(input("Introduce otro numero: "))
    num3 = int(input("Introduce otro numero: "))
    suma = num1+num2+num3
    mensaje = "El resultado es: " + str(suma)

    return mensaje

print(calc3Numbers())