# Typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()

nome = "Shayron"
idade = 17 
gpa = 3.2
estudante = True

print(type(nome))
print(type(idade))
print(type(gpa))
print(type(estudante))

gpa = int(gpa)
print(gpa)

id = float(idade)
print(id)

id = str(idade)
print(type(idade))

nome = bool(nome)
print(nome)

nome2 = "" # Bom pra ver se o user inseriu os dados ou nao
nome2 = bool(nome2)
print(nome2)