import pytest
from src.ejercicio_05 import es_mayor_de_edad

def test_inferior_mayor_Edad():
#Arrage
    edad = 17
#Act
    resultado = es_mayor_de_edad(edad)
#Assert
    assert resultado ==False

def test_mayor_edad():
#Arrage
    edad = 18
#act
    resultado = es_mayor_de_edad(edad)
#Assert
    assert resultado == True


def test_superior_mayor_edad():
#Arrage
    edad = 19
#act
    resultado = es_mayor_de_edad(edad)
#Assert
    assert resultado == True


def test_inferior_biologico():
#Arrage
    edad = -1
#act y assert
    with pytest.raises(ValueError):
        es_mayor_de_edad(edad)

def test_mayor_biologico():
#Arrage
    edad= 126
#act y assert
    with pytest.raises(ValueError):
        es_mayor_de_edad(edad)