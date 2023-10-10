#Ejercicio 2.8¶
#Escribir el programa del ejercicio 1.7 usando solamente dos variables diferentes.

def leeCompruebaEntero():
    numero = input("Introduce un entero: ")
    while not str.isdigit(numero):
        numero = input("No es un entero: ")
    numero = int(numero)
    return numero

def calc3Numbers2(num1, num2):
    suma = num1+num2
    num2 = leeCompruebaEntero()
    suma += num2
    mensaje = "El resultado es: " + str(suma)

    return mensaje

if __name__ == "__main__":
    numero1 = leeCompruebaEntero()
    numero2 = leeCompruebaEntero()
    print("EL total de la suma de tos 3 numeros es de: " + calc3Numbers2(numero1, numero2))

#He tenido que meter un input() dentro de la función