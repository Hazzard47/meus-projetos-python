# Variable = A container foa a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains

# Strings
p_n = "Shayron" # p_n -> primeiro nome
food = "pizza"
email = "shayronjft@gmail.com"

print(p_n)
print(f"Oi {p_n}")
print(f"Você gosta de {food}")
print(f"Seu email é: {email}")

# Integers ou inteiros
age = 25
quantity = 3
n_e = 30

print(f"Você tem {age} anos")
print(f"Você está comprando {quantity} itens")
print(f"Sua classe tem {n_e} estudantes")

# Float ou decimal
preco = 10.99
gpa = 3.2
distance = 5.5

print(f"O preço é ${preco}")
print(f"O seu gpa é: {gpa}") 
print(f"Voçê correu {distance}km")

# Boolean 
estudante = False
sale = True
online = False

if estudante:
  print("Você é um estudante")
else: 
  print("Você não é um estudante")

if sale:
  print("Esse item está à venda")
else: 
  print("Esse item não está à venda")

if online: 
  print("Você está online")
else:
  print("Você está offline")