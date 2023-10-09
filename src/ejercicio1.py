#Ejercicio 2.1
#Escribe un programa que pida el nombre del usuario para luego darle la bienvenida.


def hola(nombre: str):

    return "Hola, " + nombre

if __name__ == "__main__":
    nombre = input("Escribe tu nombre: ")
    print(hola(nombre))