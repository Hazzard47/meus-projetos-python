# input() = A function that prompts the user to enter data
#           Returns the entered data as a STRING

nome = input("Qual o seu nome?: ")
id = int(input("Qual a sua idade?: "))

# faz isso pra transformar em inteiro -> id = int(id) 
# ou da maneira que coloca esse comando junto com o input
id = id + 1

print(f"Oi {nome}!")
print("Feliz aniversário!")
print(f"Você tem {id} anos!")