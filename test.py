"""Módulo de tests."""

import os
import tempfile

import pandas as pd
from unittest.mock import patch


from leer_arduino import leer_y_guardar_periodicamente


class SerialMock:
    """Simula la clase Serial de pyserial con datos controlados para tests."""

    def __init__(self, *args, **kwargs):
        self.is_open = True
        self.data = [
            "150",
            "350",
            "450",
            "700",
            "850",  # valores válidos
            "abc",  # valor no numérico
            "",
            "900",
            "400.5",
            "1000",
        ]
        self.read_index = 0
        self.in_waiting = len(self.data)

    def readline(self):
        if self.read_index >= len(self.data):
            self.in_waiting = 0
            return b""
        val = self.data[self.read_index]
        self.read_index += 1
        self.in_waiting = len(self.data) - self.read_index
        return (val + "\n").encode("utf-8")

    def close(self):
        self.is_open = False


def test_guardado_excel_real():
    ruta = "archivo_test.xlsx"  # Archivo visible en tu proyecto

    try:
        with patch("leer_arduino.Serial", new=SerialMock):
            leer_y_guardar_periodicamente(
                "COM12",
                ruta,
                "Hoja1",
                intervalo_guardado=3,
                timeout_sin_datos=2,
            )

        assert os.path.exists(ruta)

        df = pd.read_excel(ruta, sheet_name="Hoja1")
        assert not df.empty
        assert "valor" in df.columns
        assert "interpretacion" in df.columns

    finally:
        # Descomenta si deseas limpiar después de ver el archivo
        # if os.path.exists(ruta):
        #     os.remove(ruta)
        pass

