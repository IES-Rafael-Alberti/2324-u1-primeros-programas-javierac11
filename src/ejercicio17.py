#Ejercicio 2.17¶
#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e 
#imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

def leeCompruebaNumero():
    numero = input("Introduce un entero: ")
    while not str.isdigit(numero):
        numero = input("No es un entero: ")
    numero = int(numero)
    return numero

def repiteNombre(nombre, numero):
    nombre_espaciado = nombre + "\n"
    return nombre_espaciado * numero 

if __name__ == "__main__":
    nombre = input()
    repeticiones = leeCompruebaNumero()
    print(repiteNombre(nombre, repeticiones))