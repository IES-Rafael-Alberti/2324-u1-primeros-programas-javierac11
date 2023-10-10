#Ejercicio 2.23¶
#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por 
#pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio
#ceu.es.

def leeCompruebaCorreo():
    correo = input("Introduce tu correo: ")
    while str.count(correo, "@") != 1:
        correo = input("Correo invalido: ")
    return correo

def correo(correo):
    correo_separado = str.split(correo, "@")
    correo_cambiado = correo_separado[0] + "@ceu.com"
    return correo_cambiado

if __name__ == "__main__":
    correo_e = leeCompruebaCorreo()
    print(correo(correo_e))