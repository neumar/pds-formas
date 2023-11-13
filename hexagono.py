import math

def calcular_area_hexagono(comprimento_lado):
    
    area = (3 * math.sqrt(3) * comprimento_lado**2) / 2
    return area
    
comprimento_lado = float(input("Digite o comprimento de um lado do hexágono: "))
area_resultante = calcular_area_hexagono(comprimento_lado)

print(area_resultante)



# calcula o perimetro de um hexagono regular
def perimetro(lado):
    perimetro = 6 * comprimento_lado
    return perimetro

perimetro_resultante = perimetro(comprimento_lado) 

print (perimetro_resultante)
    #
    return
