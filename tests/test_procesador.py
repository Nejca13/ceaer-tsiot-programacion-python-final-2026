"""
Tests para el Modulo 3 — procesador.py
Temas: class, __init__, self, metodos, csv.DictReader

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
def p(csv_path):
    """Crea un Procesador listo para usar."""
    from procesador import Procesador
    return Procesador(csv_path)


# ─────────────────────────────────────────────────
# TEST: __init__ y atributos basicos
# ─────────────────────────────────────────────────

class Test_CrearProcesador:
    """Verifica que se pueda crear un Procesador y tenga los atributos basicos."""

    def test_se_puede_crear(self, csv_path):
        """Crear un Procesador no debe lanzar error."""
        from procesador import Procesador
        p = Procesador(csv_path)
        assert p is not None, (
            "No se pudo crear el Procesador. Revisa la clase Procesador "
            "y el metodo __init__."
        )

    def test_guarda_ruta(self, csv_path):
        """El constructor debe guardar la ruta recibida."""
        from procesador import Procesador
        p = Procesador(csv_path)
        assert p.ruta == csv_path, (
            "El atributo 'ruta' no coincide con el valor pasado al constructor. "
            "Revisa que en __init__ hagas: self.ruta = ruta_csv"
        )

    def test_inicia_datos_vacio(self, csv_path):
        """Al crear el Procesador, _datos debe ser una lista vacia."""
        from procesador import Procesador
        p = Procesador(csv_path)
        assert hasattr(p, "_datos"), (
            "Falta el atributo _datos. Revisa que en __init__ "
            "pongas: self._datos = []"
        )
        assert p._datos == [], (
            "Al crear el Procesador, _datos deberia ser [] (lista vacia). "
            f"Pero se encontro: {p._datos}"
        )


# ─────────────────────────────────────────────────
# TEST: cargar_datos
# ─────────────────────────────────────────────────

class Test_CargarDatos:
    """Verifica que cargar_datos() lea el CSV correctamente."""

    def test_devuelve_10_filas(self, p):
        """Debe devolver una lista con 10 elementos."""
        resultado = p.cargar_datos()
        assert isinstance(resultado, list), (
            "cargar_datos() deberia devolver una lista, pero devolvio "
            f"{type(resultado).__name__}."
        )
        assert len(resultado) == 10, (
            f"cargar_datos() deberia devolver 10 filas, pero devolvio "
            f"{len(resultado)}. Revisa que recorra todo el CSV."
        )

    def test_devuelve_diccionarios(self, p):
        """Cada fila debe ser un diccionario con las columnas como claves."""
        resultado = p.cargar_datos()
        for i, fila in enumerate(resultado):
            assert isinstance(fila, dict), (
                f"La fila {i} deberia ser un dict, pero es "
                f"{type(fila).__name__}. Revisa que uses DictReader."
            )
            for col in ("temperatura", "humedad", "luz"):
                assert col in fila, (
                    f"Fila {i}: falta la clave '{col}' en el diccionario. "
                    f"Claves encontradas: {list(fila.keys())}"
                )

    def test_convierte_tipos_correctamente(self, p):
        """temperatura debe ser float, humedad y luz deben ser int."""
        resultado = p.cargar_datos()
        for i, fila in enumerate(resultado):
            assert isinstance(fila["temperatura"], float), (
                f"Fila {i}: temperatura deberia ser float, pero es "
                f"{type(fila['temperatura']).__name__}. "
                "Revisa que conviertas con float()."
            )
            assert isinstance(fila["humedad"], int), (
                f"Fila {i}: humedad deberia ser int, pero es "
                f"{type(fila['humedad']).__name__}."
            )
            assert isinstance(fila["luz"], int), (
                f"Fila {i}: luz deberia ser int, pero es "
                f"{type(fila['luz']).__name__}."
            )

    def test_guarda_en_self_datos(self, p):
        """Ademas de devolverlos, debe guardar los datos en self._datos."""
        resultado = p.cargar_datos()
        assert p._datos is resultado, (
            "cargar_datos() debe guardar los datos en self._datos "
            "(deberia ser el mismo objeto que el devuelto). "
            "Revisa que hagas self._datos = ..."
        )


# ─────────────────────────────────────────────────
# TEST: calcular_estadisticas
# ─────────────────────────────────────────────────

class Test_CalcularEstadisticas:
    """Verifica que calcular_estadisticas() funcione correctamente."""

    def test_devuelve_diccionario_con_tres_columnas(self, p):
        """Debe devolver un dict con claves temperatura, humedad, luz."""
        p.cargar_datos()
        est = p.calcular_estadisticas()
        assert isinstance(est, dict), (
            "calcular_estadisticas() deberia devolver un dict, pero devolvio "
            f"{type(est).__name__}."
        )
        for col in ("temperatura", "humedad", "luz"):
            assert col in est, (
                f"Falta la columna '{col}' en el resultado. "
                f"Claves encontradas: {list(est.keys())}"
            )

    def test_cada_columna_tiene_promedio_max_min(self, p):
        """Cada columna debe tener las claves promedio, max y min."""
        p.cargar_datos()
        est = p.calcular_estadisticas()
        for col in ("temperatura", "humedad", "luz"):
            for key in ("promedio", "max", "min"):
                assert key in est[col], (
                    f"Falta la clave '{key}' en las estadisticas de '{col}'."
                )

    def test_temperatura_valores_correctos(self, p):
        """Verifica promedio, max y min de temperatura."""
        p.cargar_datos()
        est = p.calcular_estadisticas()
        t = est["temperatura"]
        assert abs(t["promedio"] - 25.84) < 0.01, (
            f"El promedio de temperatura deberia ser 25.84, "
            f"pero se obtuvo {t['promedio']}."
        )
        assert t["max"] == 30.2, (
            f"La temperatura maxima deberia ser 30.2, "
            f"pero se obtuvo {t['max']}."
        )
        assert t["min"] == 21.0, (
            f"La temperatura minima deberia ser 21.0, "
            f"pero se obtuvo {t['min']}."
        )

    def test_llama_cargar_datos_si_vacio(self, csv_path):
        """Si _datos esta vacio, debe llamar a cargar_datos() automaticamente."""
        from procesador import Procesador
        p = Procesador(csv_path)
        # No llamamos a cargar_datos() directamente
        est = p.calcular_estadisticas()
        assert len(p._datos) == 10, (
            "calcular_estadisticas() deberia llamar a cargar_datos() "
            "si _datos esta vacio. Revisa el if al inicio del metodo."
        )


# ─────────────────────────────────────────────────
# TEST: detectar_alertas
# ─────────────────────────────────────────────────

class Test_DetectarAlertas:
    """Verifica que detectar_alertas() filtre correctamente."""

    def test_devuelve_lista(self, p):
        """Siempre debe devolver una lista."""
        p.cargar_datos()
        resultado = p.detectar_alertas(27)
        assert isinstance(resultado, list), (
            "detectar_alertas() deberia devolver una lista."
        )

    def test_filtra_por_limite_275(self, p):
        """temperatura > 27.5 debe devolver 3 filas."""
        p.cargar_datos()
        resultado = p.detectar_alertas(27.5)
        assert len(resultado) == 3, (
            f"detectar_alertas(27.5) deberia devolver 3 alertas, "
            f"pero devolvio {len(resultado)}."
        )
        for fila in resultado:
            assert fila["temperatura"] > 27.5, (
                f"Fila con temperatura {fila['temperatura']} NO supera 27.5."
            )

    def test_limite_alto_devuelve_vacio(self, p):
        """Ninguna temperatura supera 100."""
        p.cargar_datos()
        resultado = p.detectar_alertas(100)
        assert resultado == [], (
            f"detectar_alertas(100) deberia devolver lista vacia, "
            f"pero devolvio {len(resultado)} elementos."
        )

    def test_usa_limite_por_defecto_35(self, p):
        """Sin pasar limite, debe usar 35 por defecto (ninguna supera 35)."""
        p.cargar_datos()
        resultado = p.detectar_alertas()
        assert len(resultado) == 0, (
            f"detectar_alertas() sin argumentos deberia usar limite=35 "
            f"y devolver 0 alertas (ninguna temperatura supera 35), "
            f"pero devolvio {len(resultado)}. "
            "Revisa el parametro por defecto."
        )


# ─────────────────────────────────────────────────
# TEST: contar_alertas
# ─────────────────────────────────────────────────

class Test_ContarAlertas:
    """Verifica que contar_alertas() devuelva la cantidad."""

    def test_cuenta_correctamente(self, p):
        """contar_alertas(27.5) debe devolver 3."""
        p.cargar_datos()
        assert p.contar_alertas(27.5) == 3, (
            "contar_alertas(27.5) deberia devolver 3."
        )

    def test_cuenta_cero_si_no_hay(self, p):
        """contar_alertas(100) debe devolver 0."""
        p.cargar_datos()
        assert p.contar_alertas(100) == 0, (
            "contar_alertas(100) deberia devolver 0."
        )

    def test_cuenta_total(self, p):
        """contar_alertas(20) debe devolver 10 (todas las filas)."""
        p.cargar_datos()
        assert p.contar_alertas(20) == 10, (
            "contar_alertas(20) deberia devolver 10 (todas las filas)."
        )

    def test_usa_limite_por_defecto(self, p):
        """contar_alertas() sin limite debe devolver 0 (nada supera 35)."""
        p.cargar_datos()
        assert p.contar_alertas() == 0, (
            "contar_alertas() sin argumentos deberia devolver 0 "
            "(ninguna temperatura supera 35)."
        )
