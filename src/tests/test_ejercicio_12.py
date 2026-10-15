import pytest
from src.ejercicio_12 import procesar_usuario


def test_procesar_usuario_exitoso():
    # Arrange
    usuario = {
        "id": 1,
        "nombre": "Carlos Perez",
        "activo": True
    }
    esperado = {
        "id": 1,
        "nombre": "Carlos Perez",
        "activo": True,
        "estado_registro": "VALIDADO"
    }

    # Act
    resultado = procesar_usuario(usuario)

    # Assert
    assert resultado == esperado
    assert "estado_registro" in resultado
    assert resultado["id"] == usuario["id"]
    assert resultado["nombre"] == usuario["nombre"]
    assert resultado["activo"] == usuario["activo"]


def test_procesar_usuario_clave_faltante():
    # Arrange
    usuario_incompleto = {
        "id": 2,
        "nombre": "Maria Gomez"
        # Falta la clave 'activo'
    }

    # Act & Assert
    with pytest.raises(ValueError):
        procesar_usuario(usuario_incompleto)


def test_procesar_usuario_id_invalido():
    # Arrange
    usuario_id_cero = {
        "id": 0,
        "nombre": "Pedro",
        "activo": True
    }
    usuario_id_negativo = {
        "id": -5,
        "nombre": "Pedro",
        "activo": True
    }

    # Act & Assert
    with pytest.raises(ValueError):
        procesar_usuario(usuario_id_cero)

    with pytest.raises(ValueError):
        procesar_usuario(usuario_id_negativo)


def test_procesar_usuario_nombre_vacio():
    # Arrange
    usuario_nombre_espacios = {
        "id": 3,
        "nombre": "   ",
        "activo": True
    }

    # Act & Assert
    with pytest.raises(ValueError):
        procesar_usuario(usuario_nombre_espacios)


def test_procesar_usuario_tipo_no_diccionario():
    # Arrange
    datos_invalidos = ["id", 1, "nombre", "Ana"]

    # Act & Assert
    with pytest.raises(TypeError):
        procesar_usuario(datos_invalidos)