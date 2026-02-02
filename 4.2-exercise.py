# shopping cart program

item = input("Qual item você quer comprar?: ")
preco = float(input("Qual o preço do item?: "))
quantidade = int(input("Quantos você gostaria de comprar?: "))

total = preco * quantidade

print(f"Você comprou {quantidade} x {item}/s")
print(f"O valor total é de ${total} reais")