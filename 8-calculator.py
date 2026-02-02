""" Primeira tentativa sem ver a resolução: 

op = int(input("Qual tipo de operação você quer fazer? (1-soma/2-subtração/3-divisão/4-multiplicação): "))
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: ")) 

if op == 1:
  print(f"O resultado dessa operação é de {round(n1 + n2, 2)}")
elif op == 2:
  print(f"O resultado dessa operação é de {round(n1 - n2, 2)}")
elif op == 3:
  print(f"O resultado dessa operação é de {round(n1 / n2, 2)}")
elif op == 4:
  print(f"O resultado dessa operação é de {round(n1 * n2, 2)}")
else:
  print("Erro! Insira uma opção válida.") 

"""

""" Segunda tentativa após ver a resolução 

op = int(input("Qual tipo de operação você quer fazer? (1-soma/2-subtração/3-divisão/4-multiplicação): "))
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: ")) 

if op == 1:
  resultado = n1 + n2
elif op == 2:
  resultado = n1 - n2
elif op == 3:
  resultado = n1 / n2
elif op == 4:
  resultado = n1 * n2
else:
  print("Erro! Insira um operador válido. (1-4)") 

print(f"O resultado dessa operação é {round(resultado, 2)}")

""" 
# Dessa segunda forma é melhor pois se quiser trocar o "print" só precisa mudar uma linha de código ao invés de quatro, mas percebi que se eu colocar um operador inválido, dá erro, pois a variável "resultado" nunca é criada. Mas eu lembrei que eu já vi um comando que o programa se repete, então eu pesquisei. 

# Terceira e última tentativa.

print("========================================================================================")
print("                                     Calculadora                                        ")
print("========================================================================================")

while True:
  op = int(input("Qual tipo de operação você quer fazer? (1-soma/2-subtração/3-divisão/4-multiplicação): "))
  n1 = float(input("Digite o primeiro número: "))
  n2 = float(input("Digite o segundo número: ")) 

  if op == 1:
    resultado = n1 + n2
    break
  elif op == 2:
    resultado = n1 - n2
    break
  elif op == 3:
    resultado = n1 / n2
    break
  elif op == 4:
    resultado = n1 * n2
    break
  else:
    print("Erro! Tente novamente e insira um operador válido. (1-4)") 

print(f"O resultado dessa operação é {round(resultado, 2)}")

# Fique em mente que ainda tem alguns casos para adicionar para que o código não tenha nenhum tipo de problema, mas por enquanto é o suficiente, eu ainda tenho que revisar o uso devido de While. 