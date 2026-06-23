"""
Tests para el Modulo 1 — procesar.py
Temas: print, for, if, >, listas, indices, csv.reader

Si un test falla, lee el mensaje con atencion:
ahi dice exactamente que salio mal y donde revisar.
"""

import pytest

CSV_CONTENT = """\
temperatura,humedad,luz
25.5,60,800
26.1,58,810
24.8,62,780
27.3,55,820
23.9,65,750
28.0,50,840
22.1,70,720
29.5,48,860
21.0,72,700
30.2,45,880
"""


@pytest.fixture
def csv_path(tmp_path):
    """Crea un archivo CSV temporal para las pruebas."""
    path = tmp_path / "lecturas.csv"
    path.write_text(CSV_CONTENT)
    return str(path)


@pytest.fixture
def datos(csv_path):
    """Llama a leer_csv y devuelve los datos para usarlos en otros tests."""
    from procesar import leer_csv
    return leer_csv(csv_path)


# ─────────────────────────────────────────────────
# TEST: leer_csv
# ─────────────────────────────────────────────────

class Test_LeerCSV:
    """Verifica que leer_csv() lea bien el archivo y muestre las filas."""

    def test_devuelve_lista_con_10_filas(self, csv_path):
        """Debe devolver una lista con las 10 filas del CSV."""
        from procesar import leer_csv
        resultado = leer_csv(csv_path)
        assert isinstance(resultado, list), (
            "leer_csv() deberia devolver una lista, pero devolvio "
            f"{type(resultado).__name__}. Revisa que uses return."
        )
        assert len(resultado) == 10, (
            f"leer_csv() deberia devolver 10 filas, pero devolvio "
            f"{len(resultado)}. Revisa que el for recorra todas las filas "
            "y que saltes el encabezado con next(reader)."
        )

    def test_devuelve_listas_de_strings(self, csv_path):
        """Cada fila debe ser una lista de 3 strings (sin convertir tipos)."""
        from procesar import leer_csv
        resultado = leer_csv(csv_path)
        for i, fila in enumerate(resultado):
            assert isinstance(fila, list), (
                f"La fila {i} deberia ser una lista, pero es "
                f"{type(fila).__name__}."
            )
            assert len(fila) == 3, (
                f"La fila {i} tiene {len(fila)} elementos, deberia tener 3 "
                "(temperatura, humedad, luz)."
            )
            assert isinstance(fila[0], str), (
                f"Fila {i}: el primer elemento deberia ser string (sin convertir), "
                f"pero es {type(fila[0]).__name__}."
            )

    def test_imprime_formato_correcto(self, csv_path):
        """Debe imprimir cada fila con el formato T: ...°C  H: ...%  L: ...lm."""
        from procesar import leer_csv
        import io
        import sys

        # Capturar la salida de print()
        captura = io.StringIO()
        sys.stdout = captura
        try:
            leer_csv(csv_path)
        finally:
            sys.stdout = sys.__stdout__

        salida = captura.getvalue()
        lineas = salida.strip().split("\n")
        assert len(lineas) == 10, (
            f"Deberian imprimirse 10 lineas (una por fila), pero se imprimieron "
            f"{len(lineas)}. Revisa que el print() este dentro del for."
        )

        # Verificar el formato de la primera linea
        primera = lineas[0]
        assert "T:" in primera and "°C" in primera, (
            f"La primera linea impresa no tiene el formato esperado.\n"
            f"Se imprimio: '{primera}'\n"
            f"Se esperaba algo como: 'T: 25.5°C  H: 60%  L: 800lm'\n"
            f"Revisa el formato del print()."
        )
        assert "25.5" in primera, (
            f"La primera linea deberia contener el valor 25.5 (primera temperatura), "
            f"pero se imprimio: '{primera}'. Revisa que uses fila[0]."
        )


# ─────────────────────────────────────────────────
# TEST: mostrar_resumen
# ─────────────────────────────────────────────────

class Test_MostrarResumen:
    """Verifica que mostrar_resumen() imprima la cantidad correcta."""

    def test_imprime_cantidad_correcta(self, datos):
        """Debe imprimir 'Se leyeron N registros.' con la cantidad de filas."""
        from procesar import mostrar_resumen
        import io
        import sys

        captura = io.StringIO()
        sys.stdout = captura
        try:
            mostrar_resumen(datos)
        finally:
            sys.stdout = sys.__stdout__

        salida = captura.getvalue().strip()
        assert "Se leyeron" in salida and "registros" in salida, (
            f"La funcion deberia imprimir 'Se leyeron N registros.' pero "
            f"se imprimio: '{salida}'."
        )
        assert "10" in salida, (
            f"Hay 10 filas, pero el resumen no muestra el numero 10. "
            f"Se imprimio: '{salida}'. Revisa que uses len(datos)."
        )


# ─────────────────────────────────────────────────
# TEST: contar_superan
# ─────────────────────────────────────────────────

class Test_ContarSuperan:
    """Verifica que contar_superan() cuente correctamente."""

    def test_cuenta_temperatura_mayor_a_27(self, datos):
        """temperatura > 27 deberia dar 4 resultados."""
        from procesar import contar_superan
        resultado = contar_superan(datos, 0, 27)
        assert resultado == 4, (
            f"Temperatura > 27: se esperaban 4 filas, pero contar_superan() "
            f"devolvio {resultado}.\n"
            f"Revisa que conviertas fila[0] a float antes de comparar."
        )

    def test_cuenta_sin_resultados(self, datos):
        """Si el limite es muy alto, debe devolver 0."""
        from procesar import contar_superan
        resultado = contar_superan(datos, 0, 100)
        assert resultado == 0, (
            f"Ninguna temperatura supera 100, pero contar_superan() "
            f"devolvio {resultado}. Revisa la condicion >."
        )

    def test_cuenta_todas_las_filas(self, datos):
        """Si el limite es muy bajo, debe devolver 10."""
        from procesar import contar_superan
        resultado = contar_superan(datos, 0, 20)
        assert resultado == 10, (
            f"Todas las temperaturas superan 20, pero contar_superan() "
            f"devolvio {resultado}. Revisa que recorras todas las filas."
        )

    def test_humedad_mayor_a_60(self, datos):
        """humedad > 60 (columna 1) deberia dar 4 resultados."""
        from procesar import contar_superan
        resultado = contar_superan(datos, 1, 60)
        assert resultado == 4, (
            f"Humedad > 60: se esperaban 4 filas, pero contar_superan() "
            f"devolvio {resultado}. Revisa el indice de columna (humedad=1)."
        )


# ─────────────────────────────────────────────────
# TEST: filtrar_por
# ─────────────────────────────────────────────────

class Test_FiltrarPor:
    """Verifica que filtrar_por() devuelva las filas correctas."""

    def test_devuelve_lista(self, datos):
        """Siempre debe devolver una lista (aunque este vacia)."""
        from procesar import filtrar_por
        resultado = filtrar_por(datos, 0, 100)
        assert isinstance(resultado, list), (
            "filtrar_por() deberia devolver una lista, pero devolvio "
            f"{type(resultado).__name__}."
        )

    def test_filtra_temperatura_mayor_275(self, datos):
        """temperatura > 27.5 debe devolver las 3 filas que superan 27.5."""
        from procesar import filtrar_por
        resultado = filtrar_por(datos, 0, 27.5)
        assert len(resultado) == 3, (
            f"Temperatura > 27.5: deberia devolver 3 filas, pero devolvio "
            f"{len(resultado)}."
        )
        for fila in resultado:
            assert float(fila[0]) > 27.5, (
                f"Una fila con temperatura {fila[0]} NO supera 27.5. "
                f"Revisa la condicion en filtrar_por()."
            )

    def test_filtra_devuelve_filas_completas(self, datos):
        """Cada fila filtrada debe tener los 3 valores originales."""
        from procesar import filtrar_por
        resultado = filtrar_por(datos, 0, 28)
        for fila in resultado:
            assert len(fila) == 3, (
                "Cada fila filtrada deberia tener 3 elementos "
                "(temperatura, humedad, luz)."
            )

    def test_sin_resultados_devuelve_lista_vacia(self, datos):
        """Si nada supera el limite, devolver lista vacia."""
        from procesar import filtrar_por
        resultado = filtrar_por(datos, 0, 100)
        assert resultado == [], (
            "Si ninguna fila supera el limite, deberia devolver []."
        )
