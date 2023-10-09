#Ejercicio 2.11¶
#Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de
#todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:

def calculadoraDe1AN():
    numero = int(input("Introduce un numero: "))
    suma = numero * (numero+1) / 2
    return int(suma)
print(calculadoraDe1AN())
