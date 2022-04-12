jogador_1 = input("Jogador 1: Jogar? ")
if jogador_1 != 'r' and jogador_1 != 'p' and jogador_1 != 't':
  print("Símbolos inválidos foram digitados.")
  exit()

jogador_2 = input("Jogador 2: Jogar? ")
if jogador_2 != 'r' and jogador_2 != 'p' and jogador_2 != 't':
  print("Símbolos inválidos foram digitados.")
  exit()

if (jogador_1 == 'r' and jogador_2 == 't') or (jogador_1 == 't' and jogador_2 == 'p') or (jogador_1 == 'p' and jogador_2 == 'r'):
  print("Jogador1 venceu!")
elif (jogador_1 == 't' and jogador_2 == 'r') or (jogador_1 == 'p' and jogador_2 == 't') or (jogador_1 == 'r' and jogador_2 == 'p'):
  print("Jogador1 venceu!")
else:
  print("Deu empate!")
