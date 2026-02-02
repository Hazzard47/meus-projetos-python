# format specifiers = {:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

price1 = 3.14159
price2 = -987.65
price3 = 12.34
price4 = 3000.34241

print("Exemplo 1:")
print(f"Price 1 is ${price1:.2f}") # 2 caracteres decimais
print(f"Price 2 is ${price2:.1f}")
print(f"Price 3 is ${price3:.3f}")

print("Exemplo 2:")
print(f"Price 1 is ${price1:10}") # Preenche com espaço até formar 10 caracteres na string
print(f"Price 2 is ${price2:010}") # Preenche com o que você digitar até formar 10 caracteres na string
print(f"Price 3 is ${price3:<010}") # Preenche com o que você digitar na direita até formar 10 caracteres na string

print("Exemplo 3:")
print(f"Price 1 is ${price1:^10}") # Alinha a string, nesse caso, em um espaço de 10 caracteres
print(f"Price 4 is ${price4:,}") # Separa os milhares com vírgula
print(f"Price 4 is ${price4:,.2f}") #  Separa os milhares com vírgula E até 2 caracteres decimais

print("Exemplo 4:")
print(f"Price 1 is ${price1:+}") # Indica números positivos
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3: }") # Ou só coloca o espaço pra ficar organizado