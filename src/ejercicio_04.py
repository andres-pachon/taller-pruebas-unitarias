def aplicar_descuento(precio, porcentaje_descuento):
    if not (isinstance(precio,(int, float)) and isinstance (porcentaje_descuento, (int, float))):
        raise TypeError("los valores deben ser numericos")
    if isinstance(precio, bool)or isinstance (porcentaje_descuento, bool):
        raise TypeError("Los valores no pueden ser booleanos")
    if precio < 0:
        raise ValueError("el precio no puede ser negativo")
    if porcentaje_descuento < 0 or porcentaje_descuento > 100:
        raise ValueError("el descuento debe estrar entre 0 a 100")

    descuento = precio * (porcentaje_descuento / 100)
    return precio - descuento
