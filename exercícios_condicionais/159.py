import math

x = int(input("digite o valor de x"))

if x>4 or x < (-4):
    fx = (5*x+3)/math.sqrt(x**2 - 16)
    print(f"f(x) = {fx}")
else:
    print("NÂO PODE SER FEITA")