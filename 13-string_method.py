# nome = input("Digite o seu nome completo: ")
phone_number = input("Digite o seu número de telefone: ") # ex: 1-234-567-890

# result = len(nome) # Quantidade de caracteres de uma string
# result = nome.find("A") # Posição do primeiro "A" (começa do zero)
# result = nome.rfind("A") # Posição do último "A" (começa do zero)
# nome = nome.capitalize() # Coloca a primeira letra em maiúscula
# nome = nome.upper() # Coloca tudo em maiúsculo
# nome = nome.lower() # Coloca tudo em minúsculo
# result = nome.isdigit() # Devolve True se a string fornecida conter somente dígitos (espaço não é dígito)
# result = nome.isalpha() # Devolve True se a string conter somente caracteres do alfabeto (espaço não é do alfabeto)
result = phone_number.count("-") # Conta a quantidade do caractere especificado
# result = phone_number.replace("-", " ") # Substitui o caractere especificado pelo outro 

print(result)