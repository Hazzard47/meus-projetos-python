# If = do some code only if some confition is True
#      Else do something else

age = int(input("Digite a sua idade: "))


if age >= 100:
  print("Como você ainda tá vivo???")
elif age >= 18: 
  print("Você é maior de idade!")
elif age < 0:
  print("Você nâo nasceu ainda!")
else: 
  print("Você é menor de idade!")