pr1 = input("digite pr1")
pr2 = input("digite a pr2")

mf = (pr1 + pr2) /2

print(f"media truncada {int((mf - 0.5)+ 0.0001)}")
print(f"media arredondada {int(mf+ 0.0001)}")

