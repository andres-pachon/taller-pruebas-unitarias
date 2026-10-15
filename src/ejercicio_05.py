def es_mayor_de_edad(edad):
    if type(edad) is not int:
        raise TypeError("la edad debe ser un numero entero")
    if edad < 0 or edad > 125:
        raise ValueError("la edad ingresada esta fuera del rango biologico admisibles (0 - 125)")
    return edad >= 18