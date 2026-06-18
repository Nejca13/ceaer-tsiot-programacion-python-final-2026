import csv
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
    path = tmp_path / "lecturas.csv"
    path.write_text(CSV_CONTENT)
    return path


@pytest.fixture
def p(csv_path):
    from procesador import Procesador
    return Procesador(str(csv_path))


class TestNivel1_CrearYCargar:

    def test_crear_procesador(self, csv_path):
        from procesador import Procesador
        p = Procesador(str(csv_path))
        assert p is not None

    def test_cargar_datos_longitud(self, p):
        datos = p.cargar_datos()
        assert len(datos) == 10

    def test_cargar_datos_columnas(self, p):
        datos = p.cargar_datos()
        fila = datos[0]
        assert "temperatura" in fila
        assert "humedad" in fila
        assert "luz" in fila

    def test_cargar_datos_valores_float(self, p):
        datos = p.cargar_datos()
        for fila in datos:
            assert isinstance(fila["temperatura"], float)
            assert isinstance(fila["humedad"], int)
            assert isinstance(fila["luz"], int)


class TestNivel2_Estadisticas:

    def test_calcular_estadisticas_estructura(self, p):
        est = p.calcular_estadisticas()
        for col in ("temperatura", "humedad", "luz"):
            assert col in est
            for key in ("promedio", "max", "min"):
                assert key in est[col]

    def test_calcular_estadisticas_temperatura(self, p):
        est = p.calcular_estadisticas()
        t = est["temperatura"]
        assert abs(t["promedio"] - 25.84) < 0.01
        assert t["max"] == 30.2
        assert t["min"] == 21.0


class TestNivel3_Alertas:

    def test_detectar_alertas_superan_limite(self, p):
        alertas = p.detectar_alertas(limite=27)
        for a in alertas:
            assert a["temperatura"] > 27

    def test_detectar_alertas_cantidad(self, p):
        alertas = p.detectar_alertas(limite=27.5)
        assert len(alertas) == 3

    def test_contar_alertas(self, p):
        assert p.contar_alertas(limite=27.5) == 3
        assert p.contar_alertas(limite=100) == 0
        assert p.contar_alertas(limite=20) == 10
