#Ejercicio 2.15¶
#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
#Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance 
#final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero 
#depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y 
#mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada 
#cantidad a dos decimales.
#Calcula el interés: capital * (1 + interes)

def leeCompruebaEntero():
    numero = input("Introduce un entero: ")
    while not str.isdigit(numero):
        numero = input("No es un entero: ")
    numero = int(numero)
    return numero

def ahorros(capital):
    interes = 0.04
    anio1 = round(capital * (1+interes), 2)
    anio2 = round(anio1 * (1+interes), 2)
    anio3 = round(anio2 * (1+interes), 2)
    return anio1, anio2, anio3

if __name__ == "__main__":
    dinero = leeCompruebaEntero()
    print(ahorros(dinero))