import pytest


CSV_CONTENT = """\
temperatura,humedad,luz
25.5,60,800
26.1,58,810
24.8,62,780
27.3,55,820
"""


@pytest.fixture
def csv_path(tmp_path):
    path = tmp_path / "lecturas.csv"
    path.write_text(CSV_CONTENT)
    return path


@pytest.fixture
def sensor_temp():
    from sensor import Sensor
    return Sensor("DHT22", "°C")


@pytest.fixture
def sensor_luz():
    from sensor import Sensor
    return Sensor("BH1750", "lux")


class TestNivel1_CrearYAgregar:

    def test_crear_estacion(self):
        from estacion import EstacionMeteorologica
        e = EstacionMeteorologica("Central")
        assert e.nombre == "Central"

    def test_agregar_sensor(self, sensor_temp):
        from estacion import EstacionMeteorologica
        e = EstacionMeteorologica("Central")
        e.agregar_sensor(sensor_temp)
        assert sensor_temp in e._sensores


class TestNivel2_Reporte:

    def test_reporte_estructura(self, sensor_temp, sensor_luz):
        from estacion import EstacionMeteorologica
        e = EstacionMeteorologica("Central")
        e.agregar_sensor(sensor_temp)
        e.agregar_sensor(sensor_luz)
        sensor_temp.leer(25.5)
        sensor_luz.leer(800)
        r = e.reporte()
        assert r["nombre"] == "Central"
        assert "sensores" in r
        assert len(r["sensores"]) == 2

    def test_reporte_sensores_tienen_nombre_y_promedio(self, sensor_temp):
        from estacion import EstacionMeteorologica
        e = EstacionMeteorologica("Central")
        e.agregar_sensor(sensor_temp)
        sensor_temp.leer(25.5)
        sensor_temp.leer(26.1)
        r = e.reporte()
        s = r["sensores"][0]
        assert s["nombre"] == "DHT22"
        assert s["promedio"] == 25.8

    def test_reporte_total_lecturas(self, sensor_temp, sensor_luz):
        from estacion import EstacionMeteorologica
        e = EstacionMeteorologica("Central")
        e.agregar_sensor(sensor_temp)
        e.agregar_sensor(sensor_luz)
        sensor_temp.leer(25.5)
        sensor_luz.leer(800)
        sensor_luz.leer(810)
        r = e.reporte()
        assert r["total_lecturas"] == 3


class TestNivel3_CargarCSV:

    def test_cargar_csv_puebla_sensores(self, csv_path):
        from estacion import EstacionMeteorologica
        from sensor import Sensor
        e = EstacionMeteorologica("Central")
        e.agregar_sensor(Sensor("temperatura", "°C"))
        e.agregar_sensor(Sensor("humedad", "%"))
        e.agregar_sensor(Sensor("luz", "lux"))
        e.cargar_csv(str(csv_path))
        for s in e._sensores:
            assert len(s._lecturas) == 4

    def test_cargar_csv_archivo_inexistente_no_crash(self):
        from estacion import EstacionMeteorologica
        e = EstacionMeteorologica("Central")
        e.cargar_csv("/no/existe.csv")
