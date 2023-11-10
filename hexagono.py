import math

# calcula a area de um hexagono regular
def area(lado):
    area =(6*lado**2*math.sqrt(3))/4
    
    return area

# calcula o perimetro de um hexagono regular
def perimetro(lado):
    perimetro=6*lado
    return perimetro
