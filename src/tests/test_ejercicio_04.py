import pytest
from src.ejercicio_04 import aplicar_descuento


def test_precio_100000():
#Arrage
    precio = 100000
    porcentaje = 20
#Act
    resultado= aplicar_descuento(precio,porcentaje)
#Assert
    assert resultado == 80000.0


def test_limite_descuento():
#Arrage
    precio = 50000
    descuento = 0
#Act
    resultado= aplicar_descuento(precio, descuento)
#Assert
    assert resultado == 50000.0

def test_100_descuento():
#Arrage
    precio = 75000
    descuento = 100
#Act
    resultado = aplicar_descuento(precio, descuento)
#Assert
    assert resultado == 0

def test_descuento_menor_0 ():
#Arrage
    precio = 50000
    descuento= -1
#Act y Asser
    with pytest.raises(ValueError):
        aplicar_descuento(precio, descuento)


def test_descuento_mayor_100 ():
#Arrage
    precio = 50000
    descuento= 101
#Act y Asser
    with pytest.raises(ValueError):
        aplicar_descuento(precio, descuento)