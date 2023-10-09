#Ejercicio 2.10¶
#Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética

def operacion():
    resultado = ((3+2)/(2*5))**2
    return resultado

if __name__ == "__main__":
    print("El resultado es: " + operacion())
