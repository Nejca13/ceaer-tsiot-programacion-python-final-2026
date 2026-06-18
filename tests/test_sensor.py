import pytest


class TestNivel1_CrearYLeer:

    def test_crear_sensor_tiene_nombre(self):
        from sensor import Sensor
        s = Sensor("DHT22", "°C")
        assert s.nombre == "DHT22"

    def test_leer_almacena_lectura(self):
        from sensor import Sensor
        s = Sensor("DHT22", "°C")
        s.leer(25.5)
        assert s.ultima_lectura == 25.5

    def test_leer_multiples_acumula(self):
        from sensor import Sensor
        s = Sensor("DHT22", "°C")
        s.leer(25.5)
        s.leer(26.1)
        s.leer(24.8)
        assert s.ultima_lectura == 24.8


class TestNivel2_Estadisticas:

    def test_promedio(self):
        from sensor import Sensor
        s = Sensor("DHT22", "°C")
        s.leer(10.0)
        s.leer(20.0)
        s.leer(30.0)
        assert s.promedio == 20.0

    def test_promedio_sin_lecturas(self):
        from sensor import Sensor
        s = Sensor("DHT22", "°C")
        assert s.promedio == 0.0

    def test_maximo_y_minimo(self):
        from sensor import Sensor
        s = Sensor("DHT22", "°C")
        s.leer(10.0)
        s.leer(30.0)
        s.leer(20.0)
        assert s.maximo == 30.0
        assert s.minimo == 10.0

    def test_maximo_sin_lecturas(self):
        from sensor import Sensor
        s = Sensor("DHT22", "°C")
        assert s.maximo == 0.0
        assert s.minimo == 0.0


class TestNivel3_RepresentacionYControl:

    def test_str(self):
        from sensor import Sensor
        s = Sensor("DHT22", "°C")
        s.leer(25.5)
        s.leer(26.1)
        assert str(s) == "DHT22 | 25.8°C promedio | 2 lecturas"

    def test_reset_limpia_lecturas(self):
        from sensor import Sensor
        s = Sensor("DHT22", "°C")
        s.leer(25.5)
        s.leer(26.1)
        s.reset()
        assert s.promedio == 0.0
        assert s.ultima_lectura is None


class TestNivel4_Excepciones:

    def test_dato_invalido_existe(self):
        from sensor import DatoInvalido
        assert issubclass(DatoInvalido, Exception)

    def test_leer_valor_no_numerico_lanza_excepcion(self):
        from sensor import Sensor, DatoInvalido
        s = Sensor("DHT22", "°C")
        with pytest.raises(DatoInvalido):
            s.leer("abc")

    def test_leer_none_lanza_excepcion(self):
        from sensor import Sensor, DatoInvalido
        s = Sensor("DHT22", "°C")
        with pytest.raises(DatoInvalido):
            s.leer(None)

    def test_dato_invalido_mensaje_incluye_valor(self):
        from sensor import Sensor, DatoInvalido
        s = Sensor("DHT22", "°C")
        with pytest.raises(DatoInvalido) as exc:
            s.leer("abc")
        assert "abc" in str(exc.value)
