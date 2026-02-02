print("=====================================================")
print("           Conversor de Massa (kg<>lbs)              ")
print("=====================================================")

while True: 
 peso = float(input("Qual é o peso da masssa que você deseja converter?: "))
 unidade = input("Qual a unidade dessa massa (kg/lbs): ")

 if unidade == "kg":
   resultado = peso * 2.205
   unidade = "lbs."
   break
 elif unidade == "lbs":
   resultado = peso / 2.205
   unidade = "kg."
   break
 else:
   print("Erro! Insira uma unidade válida e tente novamente.")

print(f"O peso de é de {round(resultado, 2)}{unidade}")

# A resolução me deu a ideia de trocar a unidade dentro do "if" pra fazer somente um print. Não devia ter apagado, mas esse código ainda está um pouco melhor do que a resolução por causa do uso do "while". Fique em mente que ainda tem alguns casos para adicionar para que o código não tenha nenhum tipo de problema, mas por enquanto é o suficiente. 
