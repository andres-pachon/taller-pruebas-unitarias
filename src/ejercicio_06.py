
def validar_longitud_password(password):
    if not isinstance(password, str):
        raise TypeError("el password debe ser una cadena de caracteres o texto")
    return 8 <= len(password)<=20