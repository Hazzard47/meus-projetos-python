age = int(input("Digite a sua idade: "))

while age < 0:
   print("Idade não pode ser negativa!")
   age = int(input("Digite a sua idade: "))

print(f"Você tem {age} anos!")