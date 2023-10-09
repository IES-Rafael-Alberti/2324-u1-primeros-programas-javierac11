#Ejercicio 2.2¶
#Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio.

horas = float(input("Horas de trabajo: "))
dinero = float(input("Coste por hora: "))
def salario(horas: float, dinero: float):
    total = horas * dinero
    total = str(total)
    return "Importe total: " + total

print(salario(horas, dinero))

#Horas de trabajo: 6
#Coste por hora: 10
#Importe total: 60
