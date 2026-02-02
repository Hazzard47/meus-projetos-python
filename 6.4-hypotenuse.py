import math

c1 = float(input("Digite o valor de um dos catetos (cm): "))
c2 = float(input("Digite o valor do outro cateto (cm): "))

h = math.sqrt(pow(c1, 2) + pow(c2, 2))

print(f"A hipotenusa tem {round(h, 2)} cm") 