capital = 0
tempo = 0 
taxa = 0


while True:
  capital = float(input("Digite o valor investido inicial: "))
  if capital < 0:
    print("Capital não pode ser menor do que zero.")
  else:
    break

while True:
  taxa = float(input("Digite o valor da taxa de juros: "))
  if taxa < 0:
    print("A taxa não pode ser menor do que zero.")
  else:
    break

while True:
  tempo = int(input("Qual o período desejado (em anos): "))
  if tempo < 0:
    print("O período não pode ser menor do que zero.")
  else:
    break  

total = capital * pow((1 + taxa / 100), tempo)

print(f"Total após {tempo} anos: ${total:.2f}")