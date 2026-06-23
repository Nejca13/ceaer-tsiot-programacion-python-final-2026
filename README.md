# Evaluacion Final — Programacion en Python

## Objetivo

Completar 3 modulos para que todos los tests pasen.
Cada modulo suma dificultad de a poco:

1. `procesar.py` — escribis codigo con `for`, `if`, `print`
2. `analisis.py` — escribis funciones con `def` y `return`
3. `procesador.py` — escribis una clase con `__init__` y `self`

No se evalua memoria, se evalua practica. Podes consultar apuntes,
documentacion y hasta una IA, pero siempre mostrando primero tu intento.

---

## Requisitos

- Python 3 instalado
- Una terminal (simbolo del sistema, PowerShell, o la terminal de VSCode)

---

## Paso 1: Preparar el entorno

### 1a. Clonar el repositorio

Abre una terminal y ejecuta:

```bash
git clone <URL_DEL_REPO>
cd evaluacion-final
```

### 1b. Crear el entorno virtual

Un entorno virtual aisla las dependencias de este proyecto del resto
del sistema. Es obligatorio para que funcione.

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

> Cuando el venv esta activo, ves `(venv)` al inicio de la linea.
>
> Si cerras la terminal y la volves a abrir, tenes que activarlo otra vez
> con el mismo comando de arriba (`source` en Linux, `activate` en Windows).

### 1c. Instalar las dependencias

```bash
pip install -r requirements.txt
```

Esto instala `pytest` (el programa que corre los tests).

### 1d. Verificar que todo esta listo

```bash
python --version
pip list
```

Deberias ver Python 3 y `pytest` en la lista.

---

## Paso 2: Entender la estructura

```
evaluacion-final/
├── README.md                  este archivo
├── requirements.txt           dependencias (no tocar)
├── corregir.py                corrector automatico (no tocar)
├── datos/
│   └── lecturas.csv           10 lecturas de sensores (no tocar)
├── tests/
│   ├── conftest.py            configuracion de pytest (no tocar)
│   ├── test_procesar.py       tests del modulo 1
│   ├── test_analisis.py       tests del modulo 2
│   └── test_procesador.py     tests del modulo 3
```

Los archivos que **VOS** tenes que crear estan en la raiz:

| Archivo         | Modulo | Temas                                                          |
| --------------- | ------ | -------------------------------------------------------------- |
| `procesar.py`   | 1      | `for`, `if`, `>`, `print()`, `float()`, `len()`, indices `[0]` |
| `analisis.py`   | 2      | `def`, `return`, parametros, `sum()`, `dict`, formulas         |
| `procesador.py` | 3      | `class`, `__init__`, `self`, `csv.DictReader`, metodos         |

Los archivos de `tests/` NO se tocan. Ahi estan las especificaciones
de lo que tiene que hacer tu codigo.

---

## Paso 3: Como trabajar

### El ciclo de trabajo

Para cada modulo, segui estos pasos:

1. **Crea el archivo** (ej: `procesar.py`) con el esqueleto que ya te dimos
2. **Corre los tests** del modulo para ver cuales fallan
3. **Lee el primer error**: el mensaje dice exactamente que se espera
4. **Implementa esa funcion** en tu archivo
5. **Volve a correr los tests** para ver si pasaste
6. **Repeti** hasta que todos los tests del modulo esten en verde

### Comandos utiles

**Correr tests de un modulo:**

```bash
python -m pytest tests/test_procesar.py -v
```

**Correr un solo test (para no esperar a todos):**

```bash
python -m pytest tests/test_procesar.py::Test_LeerCSV::test_devuelve_lista_con_10_filas -v
```

**Correr todos los tests:**

```bash
python -m pytest tests/ -v
```

**Ver los prints de tu codigo mientras corre:**

```bash
python -m pytest tests/test_procesar.py -v -s
```

El `-s` hace que los `print()` se muestren en pantalla. Sirve para debuggear.

### Auto-correccion con nota

Cuando termines, corre esto para ver tu nota final:

```bash
python corregir.py
```

Muestra por cada modulo cuantos tests pasaron, una barra de progreso,
y una nota con estrellas.

---

## Paso 4: Los modulos en detalle

### Modulo 1 — `procesar.py`

Que aprendiste hasta ahora: `print()`, `for`, `if`, `>`, `<`, `==`,
`float()`, `int()`, `len()`, listas, indices `[0]`, `[1]`, `[2]`.

**Que tenes que hacer:**

| Funcion                                  | Que hace                                                                         |
| ---------------------------------------- | -------------------------------------------------------------------------------- |
| `leer_csv(ruta)`                         | Abre el archivo CSV, imprime cada fila con `print()`, devuelve la lista de filas |
| `mostrar_resumen(datos)`                 | Imprime cuantas filas se leyeron                                                 |
| `contar_superan(datos, columna, limite)` | Cuenta filas donde el valor > limite                                             |
| `filtrar_por(datos, columna, limite)`    | Devuelve las filas que superan el limite                                         |

**Pistas:**

- Usa `import csv` y `csv.reader()` para leer el archivo
- Salta el encabezado con `next(reader)`
- Para comparar, converti los strings a numeros con `float()`
- Las columnas son: `[0]` = temperatura, `[1]` = humedad, `[2]` = luz
- El archivo de datos tiene 10 filas (mas el encabezado)

**Para empezar:** abri `tests/test_procesar.py` y lee los tests
`Test_LeerCSV` para entender exactamente que tiene que devolver
`leer_csv()` y como tiene que imprimir.

### Modulo 2 — `analisis.py`

Que aprendiste hasta ahora: `def`, `return`, parametros de funcion,
`sum()`, `len()`, `max()`, `min()`, `dict`, formulas matematicas.

**Que tenes que hacer:**

| Funcion                                | Que hace                                               |
| -------------------------------------- | ------------------------------------------------------ |
| `calcular_promedio(valores)`           | Devuelve el promedio de una lista                      |
| `calcular_maximo(valores)`             | Devuelve el valor maximo                               |
| `calcular_minimo(valores)`             | Devuelve el valor minimo                               |
| `convertir_temperatura(valor, origen)` | Convierte entre Celsius y Fahrenheit                   |
| `analizar_columna(datos, columna)`     | Devuelve `{promedio, max, min}` de una columna del CSV |

**Pistas:**

- Si la lista esta vacia, devolve `0.0` (ni `None`, ni `0` entero)
- Formulas: `F = C * 9/5 + 32`, `C = (F - 32) * 5/9`
- `analizar_columna()` recibe datos como los de `leer_csv()`: lista de listas de strings
- `analizar_columna()` deberia llamar a las otras funciones que ya escribiste

**Para empezar:** abri `tests/test_analisis.py` y lee los primeros tests.

### Modulo 3 — `procesador.py`

Que aprendiste hasta ahora: `class`, `__init__`, `self`, metodos,
`csv.DictReader`, atributos privados `_datos`.

**Que tenes que hacer:**

| Metodo                              | Que hace                                                                    |
| ----------------------------------- | --------------------------------------------------------------------------- |
| `__init__(self, ruta_csv)`          | Guarda la ruta y crea `_datos = []`                                         |
| `cargar_datos(self)`                | Lee el CSV con `DictReader`, convierte tipos, guarda en `_datos` y devuelve |
| `calcular_estadisticas(self)`       | Devuelve `{columna: {promedio, max, min}}` para cada columna                |
| `detectar_alertas(self, limite=35)` | Devuelve filas donde temperatura > limite                                   |
| `contar_alertas(self, limite=35)`   | Devuelve cuantas alertas hay (usa `detectar_alertas`)                       |

**Pistas:**

- `DictReader` salta el encabezado solo y te da diccionarios: `fila["temperatura"]`
- Los valores vienen como strings, tenes que convertirlos con `float()` e `int()`
- Si `_datos` esta vacio, los metodos deben llamar a `cargar_datos()` automaticamente
- `contar_alertas()` es solo `return len(self.detectar_alertas(limite))`

**Para empezar:** abri `tests/test_procesador.py` y lee los tests de a uno.

---

## Criterios de evaluacion

| Modulo              | Tests        | Para aprobar            |
| ------------------- | ------------ | ----------------------- |
| 1 — `procesar.py`   | 12 tests     | Pasan los 12            |
| 2 — `analisis.py`   | 17 tests     | Pasan los 17            |
| 3 — `procesador.py` | 19 tests     | Pasan los 19            |
| **Total**           | **48 tests** | **Evaluacion completa** |

Cada modulo se aprueba independiente. Si solo llegas al modulo 2,
ya demostraste lo basico.

---

## Reglas importantes

- **No modifiques** ningun archivo dentro de `tests/`
- **No modifiques** `datos/lecturas.csv`
- **No modifiques** `corregir.py`
- Los archivos `.py` los creas VOS en la raiz del proyecto
- No cambies los nombres de funciones, clases ni parametros
  (los tests los verifican y si no coinciden, fallan)

---

## Tips finales

1. **Empeza por el modulo 1.** Es el mas facil y te da confianza.
2. **Un test a la vez.** No intentes escribir todo el modulo de una.
   Corre los tests, fijate cual falla, implementa solo eso, volve a correr.
3. **Lee el mensaje de error.** Esta en español y dice exactamente
   que se esperaba y que se obtuvo.
4. **Usa `print()` para entender que pasa.** Con `-s` lo ves en pantalla.
5. **No te quemes la cabeza.** Si un modulo no sale, busca en tus apuntes
   o preguntale a una IA que te explique el concepto, no que escriba
   el codigo por vos. Mostra primero tu intento.
6. **Los tests tambien pasan si no hay errores.** Algunos tests verifican
   casos borde (listas vacias, limites altos) y pueden pasar aunque no
   hayas implementado nada. No te confies: enfocate en los que fallan.
