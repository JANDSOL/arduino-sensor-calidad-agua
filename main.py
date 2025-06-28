"""
main.py

Script principal para la ejecución del sistema de adquisición de datos desde Arduino
y almacenamiento en archivo Excel. Orquesta la lectura del puerto serial y el guardado
periódico de datos.

Este script importa:
    - leer_y_guardar_periodicamente desde leer_arduino.py
    - guardar_datos_en_excel desde excel.py

Uso:
    Ejecutar este script como programa principal.
    Requiere que Arduino esté conectado y enviando datos por el puerto especificado.
"""

from leer_arduino import leer_y_guardar_periodicamente

if __name__ == "__main__":
    PUERTO = "COM12"
    BAUDIOS = 9600
    ARCHIVO_EXCEL = "datos_sensor.xlsx"
    HOJA = "SensorData"

    leer_y_guardar_periodicamente(
        PUERTO,
        ARCHIVO_EXCEL,
        HOJA,
        BAUDIOS,
        intervalo_guardado=10,
        timeout_sin_datos=10,
    )
