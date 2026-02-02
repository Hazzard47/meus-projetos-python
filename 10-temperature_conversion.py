print("=======================================================")
print("           Conversor de Temperatura (C<>F)             ")
print("=======================================================")

while True: 
 unidade = input("Essa temperatura está em Celsius ou Farenheit? (C/F): ")
 temp = float(input("Digite a temperatura: "))
 
 if unidade == "C":
   resultado = (temp * 9/5) + 32
   unidade = "F."
   break
 elif unidade == "F":
   resultado = (temp - 32) * 5/9
   unidade = "C."
   break
 else:
   print("Erro! Insira uma unidade válida e tente novamente.")

print(f"O temp de é de {round(resultado, 2)}{unidade}")