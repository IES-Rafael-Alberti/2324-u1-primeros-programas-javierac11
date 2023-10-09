#Ejercicio 2.25¶
#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra 
#por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el 
#día o el mes se introduzcan con un solo carácter.

def leeCompruebaFormatoFecha():
    fecha = input("Introduce una fecha con el hormato dd/mm/aaaa: ")
    while len(fecha) != 10 or fecha[2] != "/" or fecha[5] != "/" or not str.isdigit(fecha[0:2]+fecha[3:5]+fecha[6:]):
        fecha = input("Formato incorrecto: ")
    return fecha

def mostrarFecha(fecha):
    fecha_separada = str.split(fecha, "/")
    return fecha_separada

if __name__ == "__main__":
    fecha = leeCompruebaFormatoFecha()
    print(mostrarFecha(fecha))