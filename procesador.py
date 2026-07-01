"""
Modulo 3 — Procesador con POO basico (clase, __init__, self)

COMPLETA el codigo donde dice "TODO".
No cambies los nombres de la clase ni de los metodos.
Los tests verifican nombres, tipos de datos y valores exactos.

Modo de uso de IA: podes consultarle dudas concretas, pedirle que te
explique un concepto o que revise tu codigo, pero NO le pidas que
escriba las funciones por vos. El objetivo es que practiques.
Si le pedis ayuda, mostra primero tu intento.
"""

import csv


class Procesador:
    """Lee un archivo CSV de sensores y calcula estadisticas.

    Esta clase envuelve la logica de los modulos anteriores (procesar, analisis)
    pero usando csv.DictReader en vez de csv.reader, y guardando los datos
    como atributo del objeto.

    El CSV tiene columnas: temperatura, humedad, luz
    """

    def __init__(self, ruta_csv):
        """Guardar la ruta del archivo e inicializar _datos como lista vacia.

        Args:
            ruta_csv: ruta al archivo CSV (string)
        """
        # TODO: guardar self.ruta = ruta_csv y self._datos = []
        raise NotImplementedError("TODO: implementar __init__")

    def cargar_datos(self):
        """Leer el CSV con DictReader, convertir tipos y guardar en self._datos.

        DictReader automaticamente salta el encabezado y devuelve diccionarios
        con las columnas como claves: {"temperatura": "25.5", ...}

        Pasos:
            1. Abrir el archivo con open()
            2. Crear csv.DictReader(archivo)
            3. Recorrer con for, convertir tipos y guardar en self._datos
            4. Devolver self._datos

        Tipos:
            - temperatura: float
            - humedad: int
            - luz: int

        Returns:
            list[dict]: [{"temperatura": 25.5, "humedad": 60, "luz": 800}, ...]
        """
        # TODO: completar
        raise NotImplementedError("TODO: implementar cargar_datos")

    def calcular_estadisticas(self):
        """Calcular promedio, max y min para cada columna.

        Si self._datos esta vacio, llamar primero a self.cargar_datos().

        Returns:
            dict: {
                "temperatura": {"promedio": 25.84, "max": 30.2, "min": 21.0},
                "humedad": {"promedio": ..., "max": ..., "min": ...},
                "luz": {"promedio": ..., "max": ..., "min": ...},
            }
        """
        # TODO: completar
        raise NotImplementedError("TODO: implementar calcular_estadisticas")

    def detectar_alertas(self, limite=35):
        """Filtrar filas donde temperatura supere el limite.

        Si self._datos esta vacio, llamar primero a self.cargar_datos().

        Args:
            limite: valor a partir del cual se considera alerta

        Returns:
            list[dict]: filas que superan el limite
        """
        # TODO: completar
        raise NotImplementedError("TODO: implementar detectar_alertas")

    def contar_alertas(self, limite=35):
        """Cuantas alertas hay (usar detectar_alertas).

        Args:
            limite: valor a partir del cual se considera alerta

        Returns:
            int: cantidad de filas en alerta
        """
        # TODO: completar
        raise NotImplementedError("TODO: implementar contar_alertas")
