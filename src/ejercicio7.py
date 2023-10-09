#Ejercicio 2.7¶
#Escribe un programa que solicite tres números al usuario y calcule e imprima por pantalla su suma.

def leeCompruebaEntero():
    numero = input("Introduce un entero: ")
    while not str.isdigit(numero):
        numero = input("No es un entero: ")
    numero = int(numero)
    return numero
    
def calc3Numbers(num1, num2, num3):
    suma = num1+num2+num3
    return suma

if __name__ == "__main__":
    num1 = leeCompruebaEntero()
    num2 = leeCompruebaEntero()
    num3 = leeCompruebaEntero()   
    print("EL total de la suma de tos 3 numeros es de: " + calc3Numbers(num1, num2, num3))