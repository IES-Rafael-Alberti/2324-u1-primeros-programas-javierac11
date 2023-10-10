#Ejercicio 2.18¶
#Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por
#pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas
#las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El
#usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

def minMayus(nombre):
    nombre_min_mayus = ""
    nombre_min = str.lower(nombre)
    nombre_mayus = str.upper(nombre)
    min_mayus = str.split(nombre, " ")
    for i in min_mayus:
        nombre_min_mayus += str.upper(i[0]) + str.lower(i[1:]) + " "
        
    return nombre_min, nombre_mayus, nombre_min_mayus

if __name__ == "__main__":
    nombre = input("Escribe tu nombre: ")
    print(minMayus(nombre))