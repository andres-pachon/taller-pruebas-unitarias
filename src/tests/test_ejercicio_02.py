import pytest
from src.ejercicio_02 import numeroPar

def test_par_positivo():
# Arrange
    numero = 8

#Act
    resultado = numeroPar(numero)

#Assert
    assert resultado is True

def test_impar_positivo():
#Arrage
    numero = 7

#Act
    resultado = numeroPar(numero)
#Assert
    assert resultado is False


def test_valor_neutro():
#Arrage
    numero = 0
#Act
    resultado = numeroPar(numero)
#Assert
    assert resultado is True


def test_negativos_par():
#Arrage
    numero = -4
#Act
    resultado = numeroPar(numero)
#Assert
    assert resultado is True

def test_negativo_impar():
    numero = -9
#Act
    resultado = numeroPar(numero)
#Assert
    assert resultado is False

def test_error_decimal():
#Arrage
    numero = 4.0
#Act y Assert
    with pytest.raises(TypeError):
        numeroPar(numero)