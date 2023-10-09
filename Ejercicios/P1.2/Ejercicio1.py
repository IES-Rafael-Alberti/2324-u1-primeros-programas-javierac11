#Ejercicio 2.1
#Escribe un programa que pida el nombre del usuario para luego darle la bienvenida.

nombre = input("Escribe tu nombre: ")
def hola(nombre: str):

    return "Hola, " + nombre

print(hola(nombre))