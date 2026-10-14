import pytest
from src.ejercicio_10 import clasificar_nota


def test_clasificar_nota_limite_superior_maximo():
    # Arrange
    nota = 5.0
    esperado = "Excelente"

    # Act
    resultado = clasificar_nota(nota)

    # Assert
    assert resultado == esperado


def test_clasificar_nota_borde_inferior_excelente():
    # Arrange
    nota = 4.5
    esperado = "Excelente"

    # Act
    resultado = clasificar_nota(nota)

    # Assert
    assert resultado == esperado


def test_clasificar_nota_borde_superior_bueno():
    # Arrange
    nota = 4.4
    esperado = "Bueno"

    # Act
    resultado = clasificar_nota(nota)

    # Assert
    assert resultado == esperado


def test_clasificar_nota_borde_inferior_aprobacion_minima():
    # Arrange
    nota = 3.0
    esperado = "Aceptable"

    # Act
    resultado = clasificar_nota(nota)

    # Assert
    assert resultado == esperado


def test_clasificar_nota_borde_inmediatamente_reprobatorio():
    # Arrange
    nota = 2.9
    esperado = "Deficiente"

    # Act
    resultado = clasificar_nota(nota)

    # Assert
    assert resultado == esperado


def test_clasificar_nota_limite_inferior_absoluto():
    # Arrange
    nota = 0.0
    esperado = "Deficiente"

    # Act
    resultado = clasificar_nota(nota)

    # Assert
    assert resultado == esperado


def test_clasificar_nota_fuera_de_escala_inferior():
    # Arrange
    nota = -0.1

    # Act & Assert
    with pytest.raises(ValueError):
        clasificar_nota(nota)


def test_clasificar_nota_fuera_de_escala_superior():
    # Arrange
    nota = 5.1

    # Act & Assert
    with pytest.raises(ValueError):
        clasificar_nota(nota)