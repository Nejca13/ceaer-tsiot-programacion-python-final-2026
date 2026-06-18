from unittest.mock import patch, MagicMock
import pytest


class TestNivel1_Dispositivo:

    def test_crear_dispositivo_activo_por_defecto(self):
        from gateway import Dispositivo
        d = Dispositivo("Sensor1")
        assert d.nombre == "Sensor1"
        assert d.activo is True

    def test_dispositivo_setter_activo(self):
        from gateway import Dispositivo
        d = Dispositivo("Sensor1", activo=True)
        d.activo = False
        assert d.activo is False


class TestNivel2_Herencia:

    def test_sensor_iot_hereda_de_dispositivo(self):
        from gateway import Dispositivo, SensorIoT
        assert issubclass(SensorIoT, Dispositivo)

    def test_sensor_iot_tiene_nombre_y_unidad(self):
        from gateway import SensorIoT
        s = SensorIoT("DHT22", "°C")
        assert s.nombre == "DHT22"
        assert s.activo is True


class TestNivel3_Gateway:

    def test_gateway_agregar_dispositivo(self):
        from gateway import Gateway, SensorIoT
        g = Gateway("Gateway1")
        s = SensorIoT("DHT22", "°C")
        g.agregar_dispositivo(s)
        assert s in g._dispositivos

    def test_gateway_reporte_devuelve_dict(self):
        from gateway import Gateway, SensorIoT
        g = Gateway("Gateway1")
        g.agregar_dispositivo(SensorIoT("DHT22", "°C"))
        g.agregar_dispositivo(SensorIoT("BH1750", "lux"))
        r = g.reporte()
        assert r["nombre"] == "Gateway1"
        assert len(r["dispositivos"]) == 2
        assert r["dispositivos"][0]["nombre"] == "DHT22"

    def test_gateway_publicar_mqtt_usa_paho(self):
        from gateway import Gateway, SensorIoT
        g = Gateway("Gateway1")
        g.agregar_dispositivo(SensorIoT("DHT22", "°C"))
        with patch("gateway.paho") as mock_paho:
            mock_client = MagicMock()
            mock_paho.Client.return_value = mock_client
            g.publicar_mqtt("casa/sensor")
            mock_client.connect.assert_called_once()
            mock_client.publish.assert_called_once()
            args, _ = mock_client.publish.call_args
            assert args[0] == "casa/sensor"
