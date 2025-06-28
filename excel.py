"""
excel.py

Módulo para la escritura de datos en archivos Excel utilizando pandas.

Requiere:
    pip install pandas openpyxl
"""

import os
import pandas as pd


def guardar_datos_en_excel(df_nuevo: pd.DataFrame, archivo: str, hoja: str):
    """
    Guarda un DataFrame en un archivo Excel. Si el archivo ya existe, agrega los datos
    sin perder la información previa en la hoja especificada.

    Parámetros:
        df_nuevo (pd.DataFrame): Datos nuevos a guardar.
        archivo (str): Ruta al archivo Excel.
        hoja (str): Nombre de la hoja.

    Comportamiento:
        - Si el archivo o la hoja existen, concatena datos nuevos con datos existentes.
        - Si no, crea el archivo con los datos nuevos.
    """
    try:
        if os.path.exists(archivo):
            # Leer datos previos de la hoja, si existe
            try:
                df_existente = pd.read_excel(archivo, sheet_name=hoja)
            except ValueError:
                # La hoja no existe aún
                df_existente = pd.DataFrame()
            # Concatenar verticalmente datos existentes con nuevos
            df_concat = pd.concat([df_existente, df_nuevo], ignore_index=True)
        else:
            # No existe archivo, usar sólo nuevos datos
            df_concat = df_nuevo

        # Guardar todo en la hoja (sobrescribir hoja)
        with pd.ExcelWriter(archivo, engine="openpyxl", mode="w") as writer:
            df_concat.to_excel(writer, sheet_name=hoja, index=False)

        print(f"Datos guardados correctamente en '{archivo}' hoja '{hoja}'.")
    except Exception as e:
        print(f"Error guardando Excel: {e}")
