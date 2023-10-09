#Ejercicio 2.14¶
#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por 
#correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso 
#de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada 
#muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último 
#pedido y calcule el peso total del paquete que será enviado.

def leeCompruebaNumero(texto_input):
    numero = input(texto_input)
    while not str.isdigit(numero):
        numero = input("No es un entero: ")
    numero = int(numero)
    return numero

def calcularPeso(payasos, munecas):
    peso_payaso = 112
    peso_muneca = 75
    peso_total = (peso_payaso*payasos)+(peso_muneca*munecas)
    return peso_total

if __name__ == "__main__":
    payasos = leeCompruebaNumero("Cuantos payasos hay en el pedido: ")
    munecas = leeCompruebaNumero("Cuantas muñecas hay en el pedido: ")
    print("El peso es de: " + str(calcularPeso(payasos, munecas)) + " gramos")