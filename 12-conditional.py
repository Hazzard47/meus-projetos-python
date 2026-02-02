# expressões condicionais = Um atalho de uma linha pro if-else (operador ternário)
#                           Digitar ou atribuir um de dois valores com base em uma condição
#                           X if condição else Y
#                           (elif não funciona)

num = -6
a = 6
b = 7
idade = 17
temperatura = 25
funcao = "admin"

# print("Positivo." if num > 0 else "Negativo.")
# result = "Par." if num % 2 == 0 else "Ímpar." 
# maior_num = a if a > b else b
# menor_num = a if a < b else b
# status = "Maior de idade." if idade >= 18 else "Menor de idade."
# clima = "QUENTE." if temperatura > 25 else "FRIO."
nivel_acesso = "Acesso máximo." if funcao == "admin" else "Acesso limitado."

print(nivel_acesso)