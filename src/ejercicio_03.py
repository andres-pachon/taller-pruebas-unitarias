def Celsius_a_Fahrenheit(celsius):
    if type(celsius) not in (int, float):
        raise TypeError("la temperatura correcta debe ser un numero")
    if celsius < -273.15:
        raise ValueError("temperatura por debajo del cero absoluto (-273.15 °C)")
    return (celsius * 1.8) + 32
