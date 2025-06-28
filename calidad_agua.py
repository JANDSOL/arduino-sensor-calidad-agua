"""
calidad_agua.py

Módulo para interpretar valores numéricos de calidad del agua provenientes de un sensor.
Proporciona una función para categorizar la calidad del agua según rangos predefinidos.

Funciones:
    interpretar_calidad_agua(valor_calidad_agua: float) -> str
        Devuelve una interpretación textual de la calidad del agua basada en el valor numérico.

Uso:
    Este módulo está pensado para integrarse en sistemas de adquisición de datos
    donde se recibe un valor numérico y se requiere una evaluación rápida y clara
    de la calidad del agua.

Ejemplo:
    >>> interpretar_calidad_agua(150)
    'Excelente'
    >>> interpretar_calidad_agua(450)
    'Aceptable'
"""


def interpretar_calidad_agua(valor_calidad_agua: float) -> str:
    """
    Interpreta un valor numérico de calidad del agua según rangos definidos.

    Parámetros:
        valor_calidad_agua (float): Valor numérico entre 0 y 1000 que representa
                                    la calidad del agua medida por un sensor.

    Retorna:
        str: Cadena con la categoría de calidad del agua:
             - 'Excelente'   si el valor es menor a 200
             - 'Buena'       si está entre 200 y 399.99
             - 'Aceptable'   si está entre 400 y 599.99
             - 'Pobre'       si está entre 600 y 799.99
             - 'Contaminada' si es 800 o más
    """
    if valor_calidad_agua < 200:
        return "Excelente"
    elif 200 <= valor_calidad_agua < 400:
        return "Buena"
    elif 400 <= valor_calidad_agua < 600:
        return "Aceptable"
    elif 600 <= valor_calidad_agua < 800:
        return "Pobre"
    else:
        return "Contaminada"
