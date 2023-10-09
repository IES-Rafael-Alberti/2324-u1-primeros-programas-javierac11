#Ejercicio 2.11¶
#Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de
#todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:

def leeCompruebaEntero():
    numero = input("Introduce un entero: ")
    while not str.isdigit(numero):
        numero = input("No es un entero: ")
    numero = int(numero)
    return numero

def calculadoraDe1AN(numero):
    suma = numero * (numero+1) / 2
    return int(suma)

if __name__ == "__main__":
    numero = leeCompruebaEntero()
    print(f"La suma desde el 1 al {numero} es {calculadoraDe1AN(numero)}")
