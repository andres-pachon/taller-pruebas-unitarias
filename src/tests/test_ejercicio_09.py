import pytest
from src.ejercicio_09 import es_palindromo


def test_palindromo_palabra_simple():
    # Arrange
    texto = "radar"
    esperado = True

    # Act
    resultado = es_palindromo(texto)

    # Assert
    assert resultado is esperado


def test_palindromo_frase_con_espacios_y_mayusculas():
    # Arrange
    texto = "Anita lava la tina"
    esperado = True

    # Act
    resultado = es_palindromo(texto)

    # Assert
    assert resultado is esperado


def test_palindromo_palabra_no_palindroma():
    # Arrange
    texto = "software"
    esperado = False

    # Act
    resultado = es_palindromo(texto)

    # Assert
    assert resultado is esperado


def test_palindromo_cadena_vacia_o_solo_espacios():
    # Arrange
    texto = "   "
    esperado = False

    # Act
    resultado = es_palindromo(texto)

    # Assert
    assert resultado is esperado


def test_palindromo_tipo_numerico_lanza_type_error():
    # Arrange
    valor_invalido = 1001

    # Act & Assert
    with pytest.raises(TypeError):
        es_palindromo(valor_invalido)