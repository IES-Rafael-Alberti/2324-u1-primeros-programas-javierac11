from src.ejercicio16 import panSinVender

def test_ej16():
    assert panSinVender(56) == "Precio Total 3.49 * 56 = 195.44 \nDescuento 2.09 * 56 = 117.04 \nPrecio con descuento 1.4 * 56 = 78.4"
