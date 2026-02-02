# operadores lógicos = avaliam múltiplas condições (or, and, not)
#                      or  = pelo menos um condição deve ser True
#                      and = todas as condições devem ser True
#                      not = inverte a condição (not False, not True)

temperatura = 20
esta_chuvendo =  False

if temperatura > 35 or temperatura < 0 or esta_chuvendo:
  print("O evento fora de casa está cancelado.")
else:
  print("O evento fora de casa ainda está agendado.")

esta_ensolarado = False

if temperatura >= 28 and esta_ensolarado:
  print("Está quente lá fora.")
  print("E está ensolarado.")
elif temperatura <= 0 and esta_ensolarado:
  print("Está frio lá fora.")
  print("E está ensolarado.")
elif 28 > temperatura > 0 and esta_ensolarado:
  print("Está agradável lá fora.")
  print("E está ensolarado.")

# uso do "not" 

elif temperatura >= 28 and not esta_ensolarado:
  print("Está quente lá fora.")
  print("E está nublado.")
elif temperatura <= 0 and not esta_ensolarado:
  print("Está frio lá fora.")
  print("E está nublado.")
elif 28 > temperatura > 0 and not esta_ensolarado:
  print("Está agradável lá fora.")
  print("E está nublado.")