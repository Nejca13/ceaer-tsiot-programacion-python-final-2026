"""
Tests para el Modulo 2 — analisis.py
Temas: funciones con return, parametros, tipos, dict

Si un test falla, lee el mensaje: dice exactamente
que se esperaba y que se obtuvo.
"""

import pytest


# ─────────────────────────────────────────────────
# TEST: calcular_promedio
# ─────────────────────────────────────────────────

class Test_CalcularPromedio:
    """Prueba la funcion calcular_promedio()."""

    def test_promedio_de_tres_numeros(self):
        from analisis import calcular_promedio
        resultado = calcular_promedio([10, 20, 30])
        assert resultado == 20.0, (
            f"El promedio de [10, 20, 30] deberia ser 20.0, "
            f"pero se obtuvo {resultado}."
        )

    def test_promedio_de_un_solo_numero(self):
        from analisis import calcular_promedio
        resultado = calcular_promedio([42])
        assert resultado == 42.0, (
            f"El promedio de [42] deberia ser 42.0, "
            f"pero se obtuvo {resultado}."
        )

    def test_promedio_con_decimales(self):
        from analisis import calcular_promedio
        resultado = calcular_promedio([25.5, 26.1, 24.8])
        assert abs(resultado - 25.47) < 0.01, (
            f"El promedio de [25.5, 26.1, 24.8] deberia ser ~25.47, "
            f"pero se obtuvo {resultado}."
        )

    def test_promedio_lista_vacia(self):
        from analisis import calcular_promedio
        resultado = calcular_promedio([])
        assert resultado == 0.0, (
            "El promedio de una lista vacia deberia ser 0.0, "
            f"pero se obtuvo {resultado}. Revisa el caso borde."
        )


# ─────────────────────────────────────────────────
# TEST: calcular_maximo
# ─────────────────────────────────────────────────

class Test_CalcularMaximo:
    """Prueba la funcion calcular_maximo()."""

    def test_maximo_de_varios_numeros(self):
        from analisis import calcular_maximo
        resultado = calcular_maximo([10, 50, 30, 5])
        assert resultado == 50.0, (
            f"El maximo de [10, 50, 30, 5] deberia ser 50.0, "
            f"pero se obtuvo {resultado}."
        )

    def test_maximo_con_negativos(self):
        from analisis import calcular_maximo
        resultado = calcular_maximo([-10, -5, -20])
        assert resultado == -5.0, (
            f"El maximo de [-10, -5, -20] deberia ser -5.0 (el menos negativo), "
            f"pero se obtuvo {resultado}."
        )

    def test_maximo_lista_vacia(self):
        from analisis import calcular_maximo
        resultado = calcular_maximo([])
        assert resultado == 0.0, (
            "El maximo de una lista vacia deberia ser 0.0."
        )


# ─────────────────────────────────────────────────
# TEST: calcular_minimo
# ─────────────────────────────────────────────────

class Test_CalcularMinimo:
    """Prueba la funcion calcular_minimo()."""

    def test_minimo_de_varios_numeros(self):
        from analisis import calcular_minimo
        resultado = calcular_minimo([10, 50, 30, 5])
        assert resultado == 5.0, (
            f"El minimo de [10, 50, 30, 5] deberia ser 5.0, "
            f"pero se obtuvo {resultado}."
        )

    def test_minimo_con_negativos(self):
        from analisis import calcular_minimo
        resultado = calcular_minimo([-10, -5, -20])
        assert resultado == -20.0, (
            f"El minimo de [-10, -5, -20] deberia ser -20.0, "
            f"pero se obtuvo {resultado}."
        )

    def test_minimo_lista_vacia(self):
        from analisis import calcular_minimo
        resultado = calcular_minimo([])
        assert resultado == 0.0, (
            "El minimo de una lista vacia deberia ser 0.0."
        )


# ─────────────────────────────────────────────────
# TEST: convertir_temperatura
# ─────────────────────────────────────────────────

class Test_ConvertirTemperatura:
    """Prueba la funcion convertir_temperatura()."""

    def test_celsius_a_fahrenheit(self):
        from analisis import convertir_temperatura
        resultado = convertir_temperatura(25.0, "C")
        assert resultado == 77.0, (
            f"25°C deberian ser 77°F, pero se obtuvo {resultado}.\n"
            "Formula: F = C * 9/5 + 32"
        )

    def test_celsius_cero(self):
        from analisis import convertir_temperatura
        resultado = convertir_temperatura(0.0, "C")
        assert resultado == 32.0, (
            f"0°C deberian ser 32°F, pero se obtuvo {resultado}."
        )

    def test_fahrenheit_a_celsius(self):
        from analisis import convertir_temperatura
        resultado = convertir_temperatura(77.0, "F")
        assert abs(resultado - 25.0) < 0.01, (
            f"77°F deberian ser ~25°C, pero se obtuvo {resultado}.\n"
            "Formula: C = (F - 32) * 5/9"
        )


# ─────────────────────────────────────────────────
# TEST: analizar_columna
# ─────────────────────────────────────────────────

class Test_AnalizarColumna:
    """Prueba la funcion analizar_columna()."""

    @pytest.fixture
    def datos_prueba(self):
        """Datos simulados como los de leer_csv() (lista de listas de strings)."""
        return [
            ["25.5", "60", "800"],
            ["26.1", "58", "810"],
            ["24.8", "62", "780"],
            ["27.3", "55", "820"],
        ]

    def test_devuelve_diccionario_con_claves(self, datos_prueba):
        from analisis import analizar_columna
        resultado = analizar_columna(datos_prueba, 0)
        assert isinstance(resultado, dict), (
            "analizar_columna() deberia devolver un dict, pero devolvio "
            f"{type(resultado).__name__}."
        )
        for key in ("promedio", "max", "min"):
            assert key in resultado, (
                f"Falta la clave '{key}' en el diccionario devuelto. "
                f"Claves encontradas: {list(resultado.keys())}"
            )

    def test_temperatura_promedio(self, datos_prueba):
        from analisis import analizar_columna
        resultado = analizar_columna(datos_prueba, 0)
        assert abs(resultado["promedio"] - 25.925) < 0.01, (
            f"El promedio de temperatura deberia ser ~25.925, "
            f"pero se obtuvo {resultado['promedio']}."
        )

    def test_temperatura_max_y_min(self, datos_prueba):
        from analisis import analizar_columna
        resultado = analizar_columna(datos_prueba, 0)
        assert resultado["max"] == 27.3, (
            f"La temperatura maxima deberia ser 27.3, "
            f"pero se obtuvo {resultado['max']}."
        )
        assert resultado["min"] == 24.8, (
            f"La temperatura minima deberia ser 24.8, "
            f"pero se obtuvo {resultado['min']}."
        )

    def test_humedad_resultados(self, datos_prueba):
        from analisis import analizar_columna
        resultado = analizar_columna(datos_prueba, 1)
        assert resultado["promedio"] == 58.75, (
            f"El promedio de humedad deberia ser 58.75, "
            f"pero se obtuvo {resultado['promedio']}."
        )
        assert resultado["max"] == 62.0
        assert resultado["min"] == 55.0
