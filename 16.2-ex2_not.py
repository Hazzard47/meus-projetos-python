food = input("Digite uma comida que você gosta (s pra sair): ")

while not food == "s":
  print(f"Você gosta de {food}!")
  food = input("Digite outra comida que você gosta (s para sair): ")

print("Tchau!")