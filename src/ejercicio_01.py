def sumar(a, b):
    if type(a) not in (int, float) or type(b) not in (int, float):
        raise TypeError("ambos argumentos deben ser estrictamente numericos (int o flotantes )")
     
    return a+b

