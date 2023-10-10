#Ejercicio 2.27¶
#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y 
# muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6
# dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 
# dígitos enteros y 2 decimales.

def precios(producto, precio: float, unidades):
    coste_total = precio * unidades
    
    return f"Producto : {producto} Precio unitario : {precio:09.2f} Coste total : {coste_total:011.2f}"

if __name__ == "__main__":
    producto = input("Introduce el nombre del producto: ")
    precio_unidad = float(input("Introduce el precio unitario: "))
    unidades = int(input("Introduce las unidades: "))
    print(precios(producto, precio_unidad, unidades))