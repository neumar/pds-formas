def area(lado):
    quadrado_formula = lado * lado
    return quadrado_formula 

lado = float(input("Valor do lado do quadrado: "))
quadrado_resultado = area(lado) 
print("Área do quadrado:", quadrado_resultado)
