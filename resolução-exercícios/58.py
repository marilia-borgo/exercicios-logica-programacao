import math

xnum1 = input("ente com o 1 valor")
xnum2 = input("entre com 2 valor")
xnum3 = input("entre com 3 valor")

x = xnum1 + xnum2 / (xnum3 + xnum1) + 2 * (xnum1 - xnum2) + math.log(64)

print("x =", x)