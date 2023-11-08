import math

# calcula a area de um hexagono regular
def areaHexagono(lado):
    areaHexagono = 6 * (((lado*lado) * math.sqrt(3)) / 4 )
    return areaHexagono

# calcula o perimetro de um hexagono regular
def perimetroHexagono(lado):
    perimetroHexagono = 6 * lado
    return perimetroHexagono

