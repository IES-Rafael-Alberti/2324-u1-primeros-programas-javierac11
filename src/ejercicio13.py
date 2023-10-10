#Ejercicio 2.13¶
#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla los siguienteS: 
#"la división de n entre m da un cociente c y un resto r", donde n y m son los números introducidos 
#por el usuario, y c y r son el cociente y el resto de la división entera respectivamente.

def leeCompruebaEntero():
    numero = input("Introduce un entero: ")
    while not str.isdigit(numero):
        numero = input("No es un entero: ")
    numero = int(numero)
    return numero

def division(num1, num2):
    cociente = num1 / num2
    resto = num1 % num2
    return "la división de " + str(num1) + " entre " + str(num2) + " da un cociente " + str(cociente) + " y un resto " + str(resto)
    
if __name__ == "__main__":
    numero1 = leeCompruebaEntero()
    numero2 = leeCompruebaEntero()
    print(division(numero1, numero2))