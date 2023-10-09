#Ejercicio 2.16¶
#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%.
#Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después 
#el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una 
#constante), el descuento que se le hace por no ser fresca y el coste final total de todas las barras 
#no frescas.

def leeCompruebaEntero():
    numero = input("Introduce el numero de barras sin vender: ")
    while not str.isdigit(numero):
        numero = input("No es un entero: ")
    numero = int(numero)
    return numero

def panSinVender(barras):
    precio = 3.49
    descuento = round((precio * 0.6), 2)
    precio_descontado = round((precio * 0.4), 2)
    total = round((precio * barras),2)
    total_descuento = round((descuento * barras), 2)
    total_precio_descontado = round((precio_descontado * barras),2)
    
    mensaje = f"Precio Total {precio} * {barras} = {total} \nDescuento {descuento} * {barras} = {total_descuento} \nPrecio con descuento {precio_descontado} * {barras} = {total_precio_descontado}"
    return mensaje

if __name__ == "__main__":
    pan_sin_vender = leeCompruebaEntero()
    print(panSinVender(pan_sin_vender))