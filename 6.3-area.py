import math

r = float(input("Qual o raio do círculo? (cm): "))
# a = math.pi * r **2
#     ou assim 
a = math.pi * pow(r, 2)

print(f"A área desse círculo é de {round(a, 2)}cm^2")