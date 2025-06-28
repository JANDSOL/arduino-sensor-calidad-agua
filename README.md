# Monitor de Calidad de Agua con Arduino y Python

Este proyecto te permite **leer datos desde un sensor conectado a un Arduino**, interpretarlos automáticamente (ej. "Buena", "Contaminada", etc.) y **guardarlos en un archivo Excel**, todo usando Python.

No necesitas saber mucho de programación para comenzar 🚀.

---

## 🧰 Requisitos Previos

- Tener Python instalado. Recomendado: **Python 3.11 o superior**
- Tener acceso a un **sensor Arduino** que envíe datos por el puerto serial (como valores de calidad del agua)
- Si no tienes el Arduino conectado, igual puedes ejecutar los tests (ver más abajo)

---

## 🧱 Paso 1: Crear un entorno virtual (opcional pero recomendado)

Esto te ayuda a mantener los paquetes organizados solo para este proyecto:

```bash
python -m venv .venv
```

### ▶️ Activar el entorno virtual

#### En Windows:
```bash
.venv\Scripts\activate
```

#### En Linux o macOS:
```bash
source .venv/bin/activate
```

---

## 📦 Paso 2: Instalar dependencias necesarias

Ejecuta el siguiente comando:

```bash
pip install -r requirements.txt
```


---

## 🚀 Paso 3: Ejecutar el programa principal

El archivo principal es `main.py` o puedes ejecutar directamente la función `leer_y_guardar_periodicamente` del archivo `leer_arduino.py`.

### 🟢 Ejecutar la app:

```bash
python main.py
```

Cuando tu sensor comience a enviar datos, verás algo como esto:

```
Conectado. Presiona Ctrl+C para detener.
2025-06-28 13:22:05 > Valor: 450.0, Interpretación: Aceptable
```

Los datos se guardan automáticamente en un archivo Excel.

### 🛑 ¿Cómo salir del programa?
Presiona `Ctrl + C` cuando quieras detener la lectura.

---

## 🧪 Ejecutar los tests (sin necesidad de sensor)

Este proyecto viene con un test automático que **simula los datos del sensor** y te permite verificar que los datos **sí se están guardando en un archivo Excel real**.

### 🧪 Ejecutar test:

```bash
pytest -v test.py
```

✅ Este test crea un archivo temporal y guarda datos simulados en él. Si deseas verificar manualmente, puedes modificar el test para guardar en un archivo visible como `archivo_test.xlsx`.

---

## 📝 Archivos principales

| Archivo              | Función                                                                 |
|----------------------|-------------------------------------------------------------------------|
| `main.py`            | Punto de entrada de la app                                              |
| `leer_arduino.py`    | Se conecta al Arduino, interpreta los datos y los guarda en Excel       |
| `calidad_agua.py`    | Contiene la lógica para clasificar la calidad del agua                  |
| `excel.py`           | Maneja la lectura y escritura del archivo Excel                         |
| `test.py`            | Simula datos desde Arduino y prueba que los datos se guarden correctamente |

---

## ❓¿Problemas comunes?

- Asegúrate de **activar el entorno virtual** antes de correr cualquier comando.
- Si el test falla porque no encuentra `openpyxl`, instala así:
  ```bash
  pip install openpyxl
  ```
- El programa solo guarda cuando llega cierto número de datos. Puedes cambiar el parámetro `intervalo_guardado` en `main.py`.

---
