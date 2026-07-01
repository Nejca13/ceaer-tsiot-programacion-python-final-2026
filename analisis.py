"""
Modulo 2 — Analisis de datos con funciones y return

COMPLETA el codigo donde dice "TODO".
No cambies los nombres de funciones ni sus parametros.
Cada funcion debe devolver un valor (usar return).

Modo de uso de IA: podes consultarle dudas concretas, pedirle que te
explique un concepto o que revise tu codigo, pero NO le pidas que
escriba las funciones por vos. El objetivo es que practiques.
Si le pedis ayuda, mostra primero tu intento.
"""


def calcular_promedio(valores):
    """Calcular el promedio de una lista de numeros.

    Promedio = suma de todos los valores / cantidad de valores.

    Si la lista esta vacia, devolver 0.0.

    Args:
        valores: lista de numeros (int o float)

    Returns:
        float: el promedio

    Ejemplo:
        calcular_promedio([10, 20, 30]) → 20.0
    """
    # TODO: calcular y devolver el promedio
    pass


def calcular_maximo(valores):
    """Encontrar el valor maximo de una lista de numeros.

    Si la lista esta vacia, devolver 0.0.

    Args:
        valores: lista de numeros

    Returns:
        float: el maximo
    """
    # TODO: calcular y devolver el maximo
    raise NotImplementedError("TODO: implementar calcular_maximo")


def calcular_minimo(valores):
    """Encontrar el valor minimo de una lista de numeros.

    Si la lista esta vacia, devolver 0.0.

    Args:
        valores: lista de numeros

    Returns:
        float: el minimo
    """
    # TODO: calcular y devolver el minimo
    raise NotImplementedError("TODO: implementar calcular_minimo")


def convertir_temperatura(valor, origen):
    """Convertir temperatura entre Celsius y Fahrenheit.

    Formulas:
        Celsius -> Fahrenheit:  F = C * 9/5 + 32
        Fahrenheit -> Celsius:  C = (F - 32) * 5/9

    Args:
        valor: la temperatura a convertir (float)
        origen: "C" si el valor esta en Celsius, "F" si esta en Fahrenheit

    Returns:
        float: la temperatura convertida

    Ejemplo:
        convertir_temperatura(25.0, "C") → 77.0
        convertir_temperatura(77.0, "F") → 25.0
    """
    # TODO: convertir segun origen y devolver
    raise NotImplementedError("TODO: implementar convertir_temperatura")


def analizar_columna(datos, columna):
    """Analizar una columna del CSV y devolver estadisticas.

    Los datos vienen del formato que usa leer_csv() del modulo procesar:
    una lista de filas, cada fila es [temp_str, hum_str, luz_str].

    Esta funcion debe:
        1. Extraer los valores de la columna indicada
        2. Convertirlos a float
        3. Calcular promedio, maximo y minimo
        4. Devolver un diccionario con esos tres valores

    Args:
        datos: lista de filas (strings)
        columna: indice 0, 1 o 2

    Returns:
        dict: {"promedio": 25.84, "max": 30.2, "min": 21.0}

    Pista: reutilizar las funciones calcular_promedio, calcular_maximo
    y calcular_minimo que ya escribiste arriba.
    """
    # TODO: extraer columna, convertir, llamar a las funciones, devolver dict
    raise NotImplementedError("TODO: implementar analizar_columna")
