"""
Modulo 1 — Procesar datos CSV con print, for, if, >

COMPLETA el codigo donde dice "TODO".
No cambies los nombres de funciones ni sus parametros.
Los tests verifican que imprimas exactamente el formato pedido.

CONTENIDO DEL ARCHIVO datos/lecturas.csv:
    temperatura,humedad,luz
    25.5,60,800
    26.1,58,810
    ... (10 filas en total)

Modo de uso de IA: podes consultarle dudas concretas, pedirle que te
explique un concepto o que revise tu codigo, pero NO le pidas que
escriba las funciones por vos. El objetivo es que practiques.
Si le pedis ayuda, mostra primero tu intento.
"""

import csv


def leer_csv(ruta):
    """Leer un CSV y mostrar cada fila formateada en pantalla.

    El CSV tiene encabezado en la primera fila (temperatura,humedad,luz)
    y 10 filas de datos. Cada fila tiene 3 valores separados por coma.

    Pasos:
        1. Abrir el archivo con open(ruta, newline="")
        2. Crear un csv.reader(archivo)
        3. Saltar el encabezado con next(reader)
        4. Por cada fila, imprimir:
               T: 25.5°C  H: 60%  L: 800lm
           (fila[0] es temperatura, fila[1] es humedad, fila[2] es luz)
        5. Al final, devolver la lista de filas leidas

    Returns:
        list[list]: cada fila es [temp_str, hum_str, luz_str]

    Ejemplo de salida en pantalla:
        T: 25.5°C  H: 60%  L: 800lm
        T: 26.1°C  H: 58%  L: 810lm
        ...
    """
    # TODO: importar csv, abrir el archivo, crear reader, saltar header,
    #       recorrer con for, imprimir, guardar en lista, devolver
    raise NotImplementedError("TODO: implementar leer_csv")


def mostrar_resumen(datos):
    """Imprimir cuantas filas se leyeron.

    Usar len() sobre la lista de datos.

    Formato exacto:
        Se leyeron 10 registros.
    """
    # TODO: imprimir la cantidad de filas con el formato indicado
    raise NotImplementedError("TODO: implementar mostrar_resumen")


def contar_superan(datos, columna, limite):
    """Contar cuantas filas superan un valor limite en una columna.

    Los valores en datos son strings (ej: "25.5"), hay que convertirlos
    a float con float() para poder comparar.

    Args:
        datos: lista de filas (cada fila es [temp, hum, luz])
        columna: indice 0 = temperatura, 1 = humedad, 2 = luz
        limite: valor numerico a comparar

    Returns:
        int: cantidad de filas donde float(fila[columna]) > limite

    Ejemplo:
        contar_superan(datos, 0, 27)  # filas con temperatura > 27
    """
    # TODO: recorrer datos, convertir a float, comparar, contar
    raise NotImplementedError("TODO: implementar contar_superan")


def filtrar_por(datos, columna, limite):
    """Filtrar filas donde el valor supere el limite.

    Similar a contar_superan(), pero devuelve las filas completas
    en vez de solo la cantidad.

    Args:
        datos: lista de filas
        columna: indice de columna (0, 1, 2)
        limite: valor numerico

    Returns:
        list[list]: filas que cumplen la condicion
    """
    # TODO: recorrer datos, comparar, armar lista con las que cumplen
    raise NotImplementedError("TODO: implementar filtrar_por")
