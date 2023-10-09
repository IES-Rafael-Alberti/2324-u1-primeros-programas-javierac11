#Ejercicio 2.19¶
#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo
#introduzca muestre por pantalla "NOMBRE tiene n letras.", donde NOMBRE es el nombre de usuario en 
#mayúsculas y n es el número de letras que tienen el nombre.

def contadorLetras(nombre):
    nombre_sin_espacios = str.replace(nombre, " ", "")
    total_letra = len(nombre_sin_espacios)
    nombre_mayus = str.upper(nombre)
    return f"{nombre_mayus} tiene {total_letra} letras"

if __name__ == "__main__":
    nombre = input("Introduce tu nombre: ")
    print(contadorLetras(nombre))