#Ejercicio 2.4¶
#Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e
#imprima por pantalla la temperatura convertida.

grados_c = float(input("Introduce los grados: "))
def temperatura(grados: float):
    grados_f = (grados_c*9/5)+32
    return str(grados_f)

print(temperatura(grados_c))