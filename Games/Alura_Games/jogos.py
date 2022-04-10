import forca
import adivinhacao

print("***********************************")
print("********Escolha o seu jogo!********")
print("***********************************")

print("(1) Forca (2) Adivinhação")

game = int(input("Qual o jogo? "))

while (game >= 3):
    print("Jogo inválido!")
    game = int(input("Qual o jogo? "))
    continue

if (game == 1):
    print("Jogando forca")
    forca.play()
elif (game == 2):
    print("Jogando advinhança")
    adivinhacao.play()

