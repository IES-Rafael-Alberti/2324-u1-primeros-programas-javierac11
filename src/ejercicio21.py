#Ejercicio 2.21¶
#Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla
#la frase invertida.

def invertirFrase(frase):
    frase_invertida = ""
    frase_separada = str.split(frase, " ")
    frase_separada_invertida = frase_separada[::-1]
    for palabra in frase_separada_invertida:
        frase_invertida += palabra + " "
    return frase_invertida

if __name__ == "__main__":
    frase = input("Introduce una frase: ")
    print(invertirFrase(frase))