# Evaluación Final — Programación en Python

## Objetivo

Completar los módulos del sistema para que pasen todos los tests.
Cada módulo debe implementarse en el orden indicado.

## Estructura del proyecto

```
evaluacion-final/
├── README.md
├── requirements.txt
├── datos/
│   └── lecturas.csv
├── tests/
│   ├── conftest.py
│   ├── test_procesador.py   (obligatorio)
│   ├── test_sensor.py       (obligatorio)
│   ├── test_estacion.py     (obligatorio)
│   └── bonus/
│       ├── test_gateway.py  (bonus)
│       └── test_api.py      (bonus)
```

## Paso a paso — preparar el entorno

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPO>
cd evaluacion-final
```

### 2. Crear y activar el entorno virtual

**Linux / Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (PowerShell):**
```bash
python -m venv venv
venv\Scripts\activate
```

**Windows (Git Bash / CMD):**
```bash
python -m venv venv
venv\Scripts\activate.bat
```

> Al activar el venv vas a ver `(venv)` al inicio de la línea en la terminal.
> Para desactivarlo después: `deactivate`
> Cada vez que abras una terminal nueva, tenés que volver a activarlo.

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

Esto instala: `pytest`, `flask`, `paho-mqtt`.

### 4. Verificar que todo está listo

```bash
pip list
python --version
```

## Qué tenés que hacer

Crear los siguientes archivos en la raíz del proyecto (donde está este README), en este orden:

| Orden | Archivo | Test suite | Temas | Tipo |
|---|---|---|---|---|
| 1 | `procesador.py` | `test_procesador.py` | CSV, funciones, condicionales, bucles, listas, dicts | Obligatorio |
| 2 | `sensor.py` | `test_sensor.py` | POO, @property, encapsulamiento, raise, excepción propia | Obligatorio |
| 3 | `estacion.py` | `test_estacion.py` | Composición, CSV, try/except, logging | Obligatorio |
| 4 | `gateway.py` | `test_gateway.py` | Herencia, super(), MQTT con mock | Bonus |
| 5 | `app.py` | `test_api.py` | Flask, JSON, test_client | Bonus |

**Los tests son la especificación.** Abrí cada archivo de test para entender qué funciones/clases tenés que implementar y qué comportamiento se espera.

## Cómo ejecutar los tests

### Tests obligatorios (para aprobar)

```bash
python -m pytest tests/test_procesador.py tests/test_sensor.py tests/test_estacion.py -v
```

### Tests bonus (para nota máxima)

```bash
python -m pytest tests/bonus/ -v
```

### Todos los tests juntos

```bash
python -m pytest tests/ -v
```

### Correr un test específico

```bash
python -m pytest tests/test_sensor.py -v
```

### Ver cobertura de código

```bash
python -m pytest tests/ --cov=. -v
```

## Criterios de evaluación

- **Aprobación:** los 30 tests obligatorios pasando (test_procesador + test_sensor + test_estacion)
- **Nota máxima:** 44/44 tests (obligatorios + bonus)
  - `test_procesador.py` = 9 tests
  - `test_sensor.py` = 12 tests
  - `test_estacion.py` = 9 tests
  - `test_gateway.py` = 7 tests (bonus)
  - `test_api.py` = 7 tests (bonus)

## Reglas importantes

- No modificar ningún archivo dentro de `tests/`
- No modificar `datos/lecturas.csv`
- Los archivos los creás VOS en la raíz del proyecto
- Usar Python 3

## Tips

- No intentes escribir todo de una vez. Implementá de a un test por vez.
- Corré `python -m pytest tests/test_procesador.py -v` después de cada cambio para ver cuántos tests pasan.
- Si un test falla, leé el mensaje de error: dice exactamente qué se espera vs qué obtuviste.
- Usá `print()` para debuggear, pytest lo muestra con `-s`:
  ```bash
  python -m pytest tests/test_sensor.py -v -s
  ```
