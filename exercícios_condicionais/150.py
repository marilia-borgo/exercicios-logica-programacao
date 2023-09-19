import math

ang = int(input("DIgite angulo em graus"))
pi = 3.14
rang = ang*pi/180

if (rang > pi//2 and rang <=pi) or (rang > 3*pi/2 and rang <= 2*pi):
    print("seno", math.sin(rang))
else:
    print("cosseno", math.cos(rang))