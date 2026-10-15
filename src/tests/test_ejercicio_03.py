import pytest
from src.ejercicio_03 import Celsius_a_Fahrenheit


def test_punto_congelacion():
#Arrage
    celsius = 0
#Act
    resultado = Celsius_a_Fahrenheit(celsius)
#Assert
    assert resultado == 32.0

def test_punto_ebullicion():
#Arrage
    celsius = 100
#Act
    resultado = Celsius_a_Fahrenheit(celsius)
#Assert
    assert resultado == 212.0

def test_coincidencia_escalas():
#Arrage
    celsius = -40
#Act
    resultado = Celsius_a_Fahrenheit(celsius)
#Assert
    assert resultado == -40.0

def test_decimal_pytest():
#Arrage
    celsius = 37
#Act
    resultado = Celsius_a_Fahrenheit(celsius)
#Assert
    assert resultado == pytest.approx(98.6)

def test_inferior_noPermitido():
#Arrage
    celsius = -273.16
#Act y Assert
    with pytest.raises(ValueError):
        Celsius_a_Fahrenheit(celsius)
