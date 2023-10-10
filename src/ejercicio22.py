#Ejercicio 2.22¶
#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después
#muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

def leeCompruebaVocal():
    vocal = input("Introduce una vocal: ")
    vocales = "aeiou"
    while len(vocal) != 1 or str.lower(vocal) not in vocales:
        vocal = input("No es una vocal: ")
    return vocal        
    
def vocalMayus(frase: str, vocal: str):
    frase_cambiada = frase.replace(vocal, str.upper(vocal))
    return frase_cambiada

if __name__ == "__main__":
    frase = input("Introduce una frase: ")
    vocal = leeCompruebaVocal()
    print(vocalMayus(frase, vocal))