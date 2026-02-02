# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0])

print(credit_number[:4])

print(credit_number[5:9])

print(credit_number[5:])

print(credit_number[-1]) # Último caractere da string ('-2' = penúltimo caractere e assim por diante)

print(credit_number[::2]) # Pega todo segundo caractere da lista (sempre começa do primeiro)

ultimos_digitos = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{ultimos_digitos}")

credit_number = credit_number[::-1] # Pra inverter 
print(credit_number)