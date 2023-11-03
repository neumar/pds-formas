import pytest
import circulo
import quadrado
import hexagono

PRECISION = 1e-3

def test_circulo_1():
    raio = 5.0
    area = circulo.area(raio)
    comprimento = circulo.comprimento_circunferencia(raio)
    assert area == pytest.approx(78.5375, PRECISION)
    assert comprimento == pytest.approx(31.415, PRECISION)

def test_circulo_2():
    raio = 3.5
    area = circulo.area(raio)
    comprimento = circulo.comprimento_circunferencia(raio)
    assert area == pytest.approx(38.483375, PRECISION)
    assert comprimento == pytest.approx(21.990500, PRECISION)

def test_quadrado_1():
    lado = 7.0
    area = quadrado.area(lado)
    perimetro = quadrado.perimetro(lado)
    assert area == pytest.approx(49.0, PRECISION)
    assert perimetro == pytest.approx(28.0, PRECISION)

def test_quadrado_2():
    lado = 2.0
    area = quadrado.area(lado)
    perimetro = quadrado.perimetro(lado)
    assert area == pytest.approx(4.0, PRECISION)
    assert perimetro == pytest.approx(8.0, PRECISION)

def test_hexagono_1():
    lado = 5.0
    area = hexagono.area(lado)
    perimetro = hexagono.perimetro(lado)
    assert area == pytest.approx(64.951905, PRECISION)
    assert perimetro == pytest.approx(30.0, PRECISION)

def test_hexagono_2():
    lado = 10.0
    area = hexagono.area(lado)
    perimetro = hexagono.perimetro(lado)
    assert area == pytest.approx(259.807621, PRECISION)
    assert perimetro == pytest.approx(60.0, PRECISION)
