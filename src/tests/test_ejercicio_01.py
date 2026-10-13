import pytest 
from src.ejercicio_01 import sumar


def test_suma_enteros():
#Arrange
    numero1 = 2
    numero2 = 3
    resultado_esperado = 5

#Act
    resultado_obtenido = sumar(numero1, numero2)  

#Assert
    assert resultado_obtenido == resultado_esperado


def test_suma_negativos():
#Arrange
    numero1 = 10
    numero2 = -4
    resultad_esperado = 6

#Act
    resultado_obtenido = sumar(numero1,numero2)

#Assert
    assert resultado_obtenido == resultad_esperado


def test_tipos_invalidos():
#Arrange
    numerobueno =5 
    numeromalo ="5"

#Act y #Assert
    with pytest.raises(TypeError):
        sumar(numerobueno, numeromalo)

def test_manejo_booleanos():
#Arrange
    num1=4    
    num2=True

#Act  y Assert
    with pytest.raises(TypeError):
        sumar(num1, num2)