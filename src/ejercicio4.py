#Ejercicio 2.4¶
#Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e
#imprima por pantalla la temperatura convertida.

def temperatura(grados_c: float):
    grados_f = (grados_c*9/5)+32
    return grados_f

if __name__ == "__main__":
    grados_c = float(input("Introduce los grados: "))
    print("La temperatura en Fahrenheit es de " + str(temperatura(grados_c)))