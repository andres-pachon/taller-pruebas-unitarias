import pytest
from src.ejercicio_06 import validar_longitud_password

def test_borde_invalido_inferior():
#Arrage
    texto = "abcdefg"
#Act
    resultado = validar_longitud_password(texto)
#Assert
    assert resultado == False


def test_validar_longitud_inferior():
#Arrage
    texto = "abc12345"
#Act
    resultado = validar_longitud_password(texto)
#Assert
    assert resultado == True


def test_valido_longitud_superior():
#Arrage
    texto = "12345678911234567891"
#Act
    resultado= validar_longitud_password(texto)
#Assert
    assert  resultado == True


def test_invalido_longitud_superior():
#Arrage
    texto = "123456789112345678911"
#Act
    resultado= validar_longitud_password(texto)
#Assert
    assert  resultado == False


def test_valor_nulo():
#Arrage
    texto = None
#Act
    with pytest.raises(TypeError):
        validar_longitud_password(texto)