import pytest
from src.ejercicio_11 import division_segura


def test_division_segura_exacta():
    # Arrange
    dividendo = 10
    divisor = 2
    esperado = 5.0

    # Act
    resultado = division_segura(dividendo, divisor)

    # Assert
    assert resultado == esperado


def test_division_segura_periodica():
    # Arrange
    dividendo = 10
    divisor = 3
    esperado = pytest.approx(3.3333333333333335)

    # Act
    resultado = division_segura(dividendo, divisor)

    # Assert
    assert resultado == esperado


def test_division_segura_cero_en_dividendo():
    # Arrange
    dividendo = 0
    divisor = 5
    esperado = 0.0

    # Act
    resultado = division_segura(dividendo, divisor)

    # Assert
    assert resultado == esperado


def test_division_segura_divisor_cero_lanza_error():
    # Arrange
    dividendo = 8
    divisor = 0

    # Act & Assert
    with pytest.raises(ZeroDivisionError):
        division_segura(dividendo, divisor)