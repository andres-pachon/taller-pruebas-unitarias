import pytest
from src.ejercicio_08 import obtener_mayor


def test_obtener_mayor_positivos_desordenados():
    # Arrange
    datos = [4, 12, 8, 3]
    esperado = 12

    # Act
    resultado = obtener_mayor(datos)

    # Assert
    assert resultado == esperado


def test_obtener_mayor_negativos():
    # Arrange
    datos = [-15, -3, -8, -20]
    esperado = -3

    # Act
    resultado = obtener_mayor(datos)

    # Assert
    assert resultado == esperado


def test_obtener_mayor_unico_elemento():
    # Arrange
    datos = [42]
    esperado = 42

    # Act
    resultado = obtener_mayor(datos)

    # Assert
    assert resultado == esperado


def test_obtener_mayor_lista_vacia_lanza_value_error():
    # Arrange
    datos = []

    # Act & Assert
    with pytest.raises(ValueError):
        obtener_mayor(datos)


def test_obtener_mayor_elementos_corruptos_lanza_type_error():
    # Arrange
    datos = [1, 2, "tres"]

    # Act & Assert
    with pytest.raises(TypeError):
        obtener_mayor(datos)