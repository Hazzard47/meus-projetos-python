# While loop = executa um código enquanto alguma condição permanecer verdadeira

nome = input("D9igite o seu nome: ")

while nome == "": 
  print("Você não digitou o seu nome!")
  nome = input("Digite o seu nome: ")

print(f"Oi {nome}!")