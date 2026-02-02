""" Primeira tentativa sem ver a resolução: 

while True:
 username = input("Digite o seu username (apenas letras, máximo de 12 caracteres, sem espaços e sem dígitos): ")
 qtd = len(username)
 esp = username.isalpha()

 if qtd > 12 or not esp:
   print("Por favor insira um username válido.")
 else:
   print("Username criado com sucesso!")
   break
   
Deu certo, mas eu vou mais eu vou tentar deixar mais detalhado.
""" 
while True:
 username = input("Digite o seu username (apenas letras, máximo de 12 caracteres, sem espaços e sem dígitos): ")

 if len(username) > 12:
   print("Username muito longo. Tente novamente.")
 elif " " in username: # Podia também ser 'username.count(" ") != 0:' ou 'username.find(" ") != -1:'
   print("Username não deve conter espaços. Tente novamente.")
 elif not username.isalpha():
   print("Username deve conter somente caracteres do alfabeto. Tente novamente.")
 else: 
   print("Username criado com sucesso!")
   break
 
# Tinha achado meio estranho ainda, mas eu fiz igual ao que ele fez sem ver a resolução. 