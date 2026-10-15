def numeroPar(numero):
    if type(numero) is not int:
        raise TypeError(("el numero debe ser entero"))
    return numero % 2 == 0
