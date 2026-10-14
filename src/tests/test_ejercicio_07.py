import pytest
from src.ejercicio_07 import factorial


def test_factorial_cero():
    # Arrange
    numero = 0
    esperado = 1

    # Act
    resultado = factorial(numero)

    # Assert
    assert resultado == esperado


def test_factorial_uno():
    # Arrange
    numero = 1
    esperado = 1

    # Act
    resultado = factorial(numero)

    # Assert
    assert resultado == esperado


def test_factorial_cinco():
    # Arrange
    numero = 5
    esperado = 120

    # Act
    resultado = factorial(numero)

    # Assert
    assert resultado == esperado


def test_factorial_siete():
    # Arrange
    numero = 7
    esperado = 5040

    # Act
    resultado = factorial(numero)

    # Assert
    assert resultado == esperado


def test_factorial_negativo_lanza_value_error():
    # Arrange
    numero = -3

    # Act & Assert
    with pytest.raises(ValueError):
        factorial(numero)