# calcula a area de um circulo
def area(raio):
    Pi = 3.1415
    area_calculo = Pi * raio * raio
    return area_calculo

raio = float(input("Valor do raio para área: "))
area_resultado = area(raio)
print(area_resultado)

#calcula o comprimenot do circunferencia
def perimetro(raio):
    Pi = 3.1415
    perimetro_calculo = (2 * Pi) * raio
    return perimetro_calculo

raio = float(input("Valor do raio para Perimetro: "))
perimetro_resultado = perimetro(raio)
print(perimetro_resultado)