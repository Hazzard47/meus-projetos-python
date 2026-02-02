num = int(input("Digite um número entre 1 e 10: ")) 

while num < 1 or num > 10:
  print(f"{num} não é válido!")
  num = int(input("Digite um número entre 1 e 10: ")) 

print(f"O seu número é {num}!")