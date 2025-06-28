"""
leer_arduino.py

Módulo para la lectura continua de datos enviados desde un dispositivo Arduino
a través del puerto serial. Los datos se pueden acumular en memoria o procesar
en tiempo real para su análisis o almacenamiento.

Requiere la biblioteca pyserial:
    pip install pyserial
"""

import time

import pandas as pd
from serial import Serial, SerialException  # pylint: disable=no-name-in-module

from excel import guardar_datos_en_excel
from calidad_agua import interpretar_calidad_agua


def leer_y_guardar_periodicamente(
    puerto: str,
    archivo_excel: str,
    hoja: str,
    baudios=9600,
    intervalo_guardado=10,
    timeout_sin_datos=10,
):
    """
    Lee datos desde el puerto serial y los guarda en Excel periódicamente.

    Parámetros:
        puerto (str): Nombre del puerto serial (ej. 'COM12' o '/dev/ttyUSB0').
        archivo_excel (str): Ruta al archivo Excel donde se guardarán los datos.
        hoja (str): Nombre de la hoja de Excel.
        baudios (int): Velocidad de comunicación serial. Por defecto 9600.
        intervalo_guardado (int): Número de líneas a acumular antes de guardar.
        timeout_sin_datos (int): Segundos máximos sin recibir datos antes de cerrar.

    Comportamiento:
        - Se conecta al dispositivo Arduino.
        - Lee datos continuamente.
        - Guarda cada 'intervalo_guardado' líneas en el archivo Excel.
        - Si no recibe datos en 'timeout_sin_datos' segundos, termina la lectura.
        - Al presionar Ctrl+C, se guarda lo que quede en buffer y se cierra el puerto.
    """
    arduino = None
    buffer_datos = []
    ultimo_tiempo_dato = time.time()

    try:
        arduino = Serial(port=puerto, baudrate=baudios, timeout=1)
        time.sleep(2)
        print("Conectado. Presiona Ctrl+C para detener.")

        while True:
            if arduino.in_waiting > 0:
                linea = arduino.readline().decode("utf-8").strip()
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

                try:
                    valor = float(linea)
                    interpretacion = interpretar_calidad_agua(valor)
                except ValueError:
                    valor = None
                    interpretacion = "Valor inválido"

                buffer_datos.append({
                    "timestamp": timestamp,
                    "valor": valor,
                    "interpretacion": interpretacion
                })

                print(f"{timestamp} > Valor: {valor}, Interpretación: {interpretacion}")

                ultimo_tiempo_dato = time.time()

                if len(buffer_datos) >= intervalo_guardado:
                    df_temp = pd.DataFrame(buffer_datos)
                    guardar_datos_en_excel(df_temp, archivo_excel, hoja)
                    buffer_datos.clear()
            else:
                # No hay datos, verificar timeout
                if time.time() - ultimo_tiempo_dato > timeout_sin_datos:
                    print(f"No se recibieron datos en {timeout_sin_datos} segundos. Cerrando lectura.")
                    break
                time.sleep(0.1)  # Evita uso excesivo CPU

    except KeyboardInterrupt:
        print("\nLectura detenida por usuario.")

    except SerialException as e:
        print(f"Error de conexión serial: {e}")

    except Exception as e:  # pylint: disable=broad-exception-caught
        print(f"Error inesperado: {e}")

    finally:
        if arduino and arduino.is_open:
            arduino.close()
        # Guardar datos restantes
        if buffer_datos:
            df_temp = pd.DataFrame(buffer_datos)
            guardar_datos_en_excel(df_temp, archivo_excel, hoja)
