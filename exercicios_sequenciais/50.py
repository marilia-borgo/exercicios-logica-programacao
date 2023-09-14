import math
base = input("entre com a base do triangulo")
altura = input("entre com a altura do triangulo")

perimetro = (base+altura)*2
area = base * altura
diagonal = math.sqrt(base**2 + altura**2)

print("perimetro", perimetro)
print("area", area)
print("diagonal", diagonal)