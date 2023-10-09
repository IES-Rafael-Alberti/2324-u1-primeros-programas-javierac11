from src.ejercicio6 import calcIva

def test_ej6():
    assert calcIva(45) == "El precio sin iva es: 40.5\nEl iva es: 4.5"
    