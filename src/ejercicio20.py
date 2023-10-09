#Ejercicio 2.20¶
#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el
#código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
#Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla 
#el número de teléfono sin el prefijo y la extensión.

def leerComprobarFormato():
    numero = input("Introduce un numero con el formato +34-XXXXXXXXX-XX: ")
    while len(numero) != 16 or numero[0:3] != "+34" or numero[3] != "-" or numero[13] != "-" or not str.isdigit(numero[4:13]) or not str.isdigit(numero[14:16]):
        numero = input(" no valido: ")
    return numero

def quitarFormato(numero: str):
    numero_sin_formato = numero[4:13]
    return numero_sin_formato    

if __name__ == "__main__":
    numero = leerComprobarFormato()
    print(quitarFormato(numero))