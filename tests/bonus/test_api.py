import sys

import pytest


def _set_estacion(estacion):
    """Inyecta una estacion de prueba en el modulo app."""
    sys.modules["app"].estacion = estacion


@pytest.fixture
def client():
    from app import app
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


@pytest.fixture
def estacion_con_alertas():
    from estacion import EstacionMeteorologica
    from sensor import Sensor
    e = EstacionMeteorologica("Test")
    s1 = Sensor("Normal", "°C")
    s1.leer(25.0)
    s1.leer(26.0)
    s2 = Sensor("Alerta", "°C")
    s2.leer(40.0)
    s2.leer(42.0)
    e.agregar_sensor(s1)
    e.agregar_sensor(s2)
    return e


class TestNivel1_Rutas:

    def test_index_devuelve_200(self, client):
        resp = client.get("/")
        assert resp.status_code == 200

    def test_api_sensores_devuelve_json(self, client):
        from estacion import EstacionMeteorologica
        from sensor import Sensor
        e = EstacionMeteorologica("Test")
        s = Sensor("DHT22", "°C")
        s.leer(25.5)
        e.agregar_sensor(s)
        _set_estacion(e)
        resp = client.get("/api/sensores")
        assert resp.status_code == 200
        assert resp.is_json

    def test_api_alertas_devuelve_json(self, client):
        resp = client.get("/api/alertas")
        assert resp.status_code == 200
        assert resp.is_json


class TestNivel2_Contenido:

    def test_api_sensores_contiene_sensores(self, client):
        from estacion import EstacionMeteorologica
        from sensor import Sensor
        e = EstacionMeteorologica("Test")
        s = Sensor("DHT22", "°C")
        s.leer(25.5)
        e.agregar_sensor(s)
        _set_estacion(e)
        resp = client.get("/api/sensores")
        data = resp.get_json()
        assert "sensores" in data
        assert len(data["sensores"]) == 1
        assert data["sensores"][0]["nombre"] == "DHT22"

    def test_api_alertas_filtra_correctamente(self, client, estacion_con_alertas):
        _set_estacion(estacion_con_alertas)
        resp = client.get("/api/alertas")
        data = resp.get_json()
        assert len(data) == 1
        assert data[0]["nombre"] == "Alerta"

    def test_api_sin_alertas_devuelve_lista_vacia(self, client):
        from estacion import EstacionMeteorologica
        from sensor import Sensor
        e = EstacionMeteorologica("Test")
        s = Sensor("Normal", "°C")
        s.leer(25.0)
        e.agregar_sensor(s)
        _set_estacion(e)
        resp = client.get("/api/alertas")
        data = resp.get_json()
        assert data == []


class TestNivel3_HTML:

    def test_index_contiene_nombre_estacion(self, client):
        from estacion import EstacionMeteorologica
        e = EstacionMeteorologica("Estacion Norte")
        _set_estacion(e)
        resp = client.get("/")
        assert resp.status_code == 200
        html = resp.data.decode()
        assert "Estacion Norte" in html
