#Ejercicio 2.3¶
#Suponiendo que se han ejecutado las siguientes sentencias de asignación:
#Para cada una de las expresiones siguientes, intenta adivinar el valor de la expresión y su tipo sin ejecutarlas en el intérprete:
#1. ancho / 2
#2. ancho // 2
#3. alto / 3
#4. 1 + 2 * 5
#Cuando termines comprueba con el intérprete si has acertado.

def alto_y_ancho():
    ancho = 17
    alto = 12.0

    uno = ancho/2
    dos = ancho // 2
    tres = alto / 3
    cuatro = 1 + 2 * 5

    return "Uno = " + str(uno) + "\nDos = " + str(dos) + "\nTres = " + str(tres) + "\nCuatro = " + str(cuatro)

if __name__ == "__main__":
    
    print(alto_y_ancho())