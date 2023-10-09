#Ejercicio 2.26¶
#Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados 
#por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

def saltoLineaLista(lista_compra):
    lista_saltos = ""
    lista_separada = str.split(lista_compra, ",")
    for producto in lista_separada:
        lista_saltos += producto + "\n"
    return lista_saltos

if __name__ == "__main__":
    lista = input("Escribe una lista de la compra separada por comas: ")
    print(saltoLineaLista(lista))