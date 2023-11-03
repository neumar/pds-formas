import circulo
import quadrado
import hexagono

print("Área e comprimento de formas geométricas")

print("Circulo")
raio = float(input("Informe o raio do círculo: "))
print("Area: %f" %circulo.area(raio))
print("Comprimento: %f" %circulo.comprimento_circunferencia(raio))
print()

print("Quadrado")
lado = float(input("Informe o lado do quadrado: "))
print("Area: %f" %quadrado.area(lado))
print("Perimetro: %f" %quadrado.perimetro(lado))
print()

print("Hexagono Regular")
lado = float(input("Informe o lado do Hexagono: "))
print("Area: %f" %hexagono.area(lado))
print("Perimetro: %f" %hexagono.perimetro(lado))
print()
