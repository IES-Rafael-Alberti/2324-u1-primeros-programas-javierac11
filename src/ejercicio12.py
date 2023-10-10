#Ejercicio 2.12¶
#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice
#de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa 
#corporal es donde es el índice de masa corporal calculado redondeado con dos decimales.

def IMC(kg, m):
    icm = kg / (m)**2
    return icm

if __name__ == "__main__":
    kilos = float(input("Introduce un peso en kilogramos: "))
    metros = float(input("Introcude tu altura en metros: "))
    print("Tu índice de masa corporal es donde es " + str(IMC(kilos, metros)))